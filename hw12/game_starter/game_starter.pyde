from board import Board
from game_controller import GameController
from player import Player
from game_manager import GameManager
import time

SIZE = 8
CELL_WIDTH = 100
WIDTH = 100 * SIZE
HEIGHT = 100 * SIZE
EDGE = 20  # the space left for disk and cell "walls"
HUMAN_COLOR = 0
AI_COLOR = 1
TIME_ECCLIPSE = 60  # set the time period

game_controller = GameController(WIDTH, HEIGHT)
board = Board(WIDTH, HEIGHT, CELL_WIDTH, EDGE, game_controller,
              HUMAN_COLOR, AI_COLOR)
human_player = Player(board)
ai_player = Player(board)
gm = GameManager(human_player, ai_player, board, game_controller)


def setup():
    size(WIDTH, HEIGHT)
    colorMode(RGB, 1)


counting_time = 0


def draw():
    global counting_time
    background(0, 0.5, 0)
    board.display()
    if not gm.human_turn and not game_controller.game_over:
        if counting_time <= TIME_ECCLIPSE:
            game_controller.ai_thinking = True
            counting_time += 1
        else:
            game_controller.ai_thinking = False
            gm.ai_make_move()
            counting_time = 0
    game_controller.update()


def mousePressed():
    if gm.human_turn:
        gm.human_make_move(mouseX, mouseY)
