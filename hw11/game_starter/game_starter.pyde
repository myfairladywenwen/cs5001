from board import Board
from game_controller import GameController
from player import Player

WIDTH = 800
HEIGHT = 800
CELL_WIDTH = 200  # change this to control how many cells you want
EDGE = 20  # the space left for disk and cell "walls"

game_controller = GameController(WIDTH, HEIGHT)
board = Board(WIDTH, HEIGHT, CELL_WIDTH, EDGE, game_controller)
player = Player(board)


def setup():
    size(WIDTH, HEIGHT)
    colorMode(RGB, 1)

def draw():
    background(0, 0.5, 0)
    board.display()
    game_controller.update()

def mousePressed():
    player.control(mouseX, mouseY)
