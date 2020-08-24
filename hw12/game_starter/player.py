from random import randint
from board import Board


class Player:
    '''A player, click on the board where he decides to create a disk'''
    def __init__(self, board):
        self.board = board

    def human_move(self, x, y, color):
        '''human player takes a move,
        creates a corresponding disk'''
        self.board.create_disk(x, y, color)

    def ai_move(self, row, col, color):
        '''ai player takes a move,
        creates a corresponding disk'''
        self.board.create_disk(col * self.board.CELL_WIDTH +
                               self.board.CELL_WIDTH/2,
                               row * self.board.CELL_WIDTH +
                               self.board.CELL_WIDTH/2, color)
