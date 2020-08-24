from board import Board


class GameController:
    '''maintains the state of the game'''
    def __init__(self, WIDTH, HIGHT):
        self.WIDTH = WIDTH
        self.HEIGHT = HIGHT
        self.game_over = False
        self.black_wins = False
        self.white_wins = False
        self.a_tie = False
        self.black_count = 0
        self.white_count = 0

    def update(self):
        '''carries out necessary actions if game is over'''
        if self.game_over:
            if self.black_wins:
                fill(0.3)
                textSize(30)
                text("GAME OVER.\nBLACK WINS.\nBLACK HAS " +
                     str(self.black_count) + " TILES.",
                     self.WIDTH/2 - 140, self.HEIGHT/2)
            elif self.white_wins:
                fill(0.3)
                textSize(30)
                text("GAME OVER.\nWHITE WINS.\nWHITE HAS " +
                     str(self.white_count) + " TILES.",
                     self.WIDTH/2 - 140, self.HEIGHT/2)
            elif self.a_tie:
                fill(0.3)
                textSize(30)
                text("GAME OVER.\nA TIE.\nEACH HAS " +
                     str(self.white_count) + " TILES.",
                     self.WIDTH/2 - 140, self.HEIGHT/2)