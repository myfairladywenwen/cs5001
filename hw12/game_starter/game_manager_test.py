from game_manager import GameManager
from player import Player
from game_controller import GameController
from board import Board
from disks import Disks


def test_constructor():
    my_gc = GameController(800, 800)
    my_board = Board(800, 800, 100, 20, my_gc, 0, 1)
    human_player = Player(my_board)
    ai_player = Player(my_board)
    gm = GameManager(human_player, ai_player, my_board, my_gc)
    assert gm.human_player is human_player
    assert gm.ai_player is ai_player
    assert gm.human_turn is True
    assert gm.board is my_board
    assert gm.gc is my_gc


def test_get_legal_cells():
    my_gc = GameController(800, 800)
    my_board = Board(800, 800, 100, 20, my_gc, 0, 1)
    human_player = Player(my_board)
    ai_player = Player(my_board)
    gm = GameManager(human_player, ai_player, my_board, my_gc)
    assert gm.get_legal_cells(0) == {(2, 3): [(3, 3)], (3, 2): [(3, 3)],
                                     (4, 5): [(4, 4)], (5, 4): [(4, 4)]}


def test_human_make_move():
    my_gc = GameController(800, 800)
    my_board = Board(800, 800, 100, 20, my_gc, 0, 1)
    human_player = Player(my_board)
    ai_player = Player(my_board)
    gm = GameManager(human_player, ai_player, my_board, my_gc)
    gm.human_make_move(250, 350)
    assert gm.board.disks.white_count == 1
    assert gm.board.disks.black_count == 4
    assert gm.board.disks.total_disks == 5
    assert gm.human_turn is False


def test_generate_ai_pos():
    gc = GameController(800, 800)
    board = Board(800, 800, 100, 20, gc, 0, 1)
    human_player = Player(board)
    ai_player = Player(board)
    gm = GameManager(human_player, ai_player, board, gc)
    # since we can not predict which cell ai will make move to,
    # so we need to hardcode 7 disks to test the eighth move,
    # which should be the positon we predict,
    # for it will let ai get the longest flip list
    gm.board.disks.create(550, 150, 0)
    gm.board.disks.create(450, 150, 0)
    gm.board.disks.create(250, 350, 0)
    gm.board.disks.create(350, 350, 0)
    gm.board.disks.create(450, 350, 1)
    gm.board.disks.create(350, 450, 0)
    gm.board.disks.create(450, 450, 1)
    legal_cells = gm.get_legal_cells(1)
    ai_pos = gm.generate_ai_pos(legal_cells)
    assert ai_pos == (3, 1)


def test_ai_make_move():
    gc = GameController(800, 800)
    board = Board(800, 800, 100, 20, gc, 0, 1)
    human_player = Player(board)
    ai_player = Player(board)
    gm = GameManager(human_player, ai_player, board, gc)
    gm.board.disks.create(550, 150, 0)
    gm.board.disks.create(450, 250, 0)
    gm.board.disks.create(250, 350, 0)
    gm.board.disks.create(350, 350, 0)
    gm.board.disks.create(450, 350, 1)
    gm.board.disks.create(350, 450, 0)
    gm.board.disks.create(450, 450, 1)
    # manually deduct the hardcode disks which are duplicate with
    # the disks when initialized
    gm.board.disks.total_disks -= 4
    gm.board.disks.black_count -= 2
    gm.board.disks.white_count -= 2
    gm.ai_make_move()
    assert gm.board.disks.total_disks == 8
    assert gm.board.disks.black_count == 3
    assert gm.board.disks.white_count == 5
