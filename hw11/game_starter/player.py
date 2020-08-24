from board import Board


class Player:
    '''A player, click on the board where he decides to create a disk'''
    def __init__(self, board):
        self.board = board

    def control(self, x, y):
        self.board.create_disk(x, y)