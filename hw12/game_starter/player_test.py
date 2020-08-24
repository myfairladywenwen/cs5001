from player import Player
from game_controller import GameController
from board import Board


def test_constructor():
    my_gc = GameController(800, 800)
    my_board = Board(800, 800, 200, 20, my_gc, 0, 1)
    my_player = Player(my_board)
    assert my_player.board == my_board


def test_human_move():
    my_gc = GameController(800, 800)
    my_board = Board(800, 800, 200, 20, my_gc, 0, 1)
    my_player = Player(my_board)
    my_player.board.create_disk(50, 50, 0)
    assert my_board.disks.matrix[0][0].color == 0


def test_ai_move():
    my_gc = GameController(800, 800)
    my_board = Board(800, 800, 200, 20, my_gc, 0, 1)
    my_player = Player(my_board)
    my_player.board.create_disk(0, 0, 1)
    assert my_board.disks.matrix[0][0].color == 1
