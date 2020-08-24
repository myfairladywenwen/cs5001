from disks import Disks


class Board:
    def __init__(self, WIDTH, HEIGHT, CELL_WIDTH, EDGE, game_controller,
                 HUMAN_COLOR, AI_COLOR):
        '''draw the chess board and handles interaction
        between game controller, player, and disks'''
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.CELL_WIDTH = CELL_WIDTH
        self.EDGE = EDGE
        self.gc = game_controller
        self.disks = Disks(WIDTH, HEIGHT, CELL_WIDTH, EDGE,
                           HUMAN_COLOR, AI_COLOR)
        self.human_color = HUMAN_COLOR
        self.ai_color = AI_COLOR
        # create the beginning 4 disks in the middle
        self.initial_four(WIDTH, HEIGHT, CELL_WIDTH, HUMAN_COLOR, AI_COLOR)

    def initial_four(self, WIDTH, HEIGHT, CELL_WIDTH, color1, color2):
        self.disks.create(WIDTH/2 + CELL_WIDTH/2,
                          HEIGHT/2 - CELL_WIDTH/2, color1)
        self.disks.create(WIDTH/2 - CELL_WIDTH/2,
                          HEIGHT/2 - CELL_WIDTH/2, color2)
        self.disks.create(WIDTH/2 - CELL_WIDTH/2,
                          HEIGHT/2 + CELL_WIDTH/2, color1)
        self.disks.create(WIDTH/2 + CELL_WIDTH/2,
                          HEIGHT/2 + CELL_WIDTH/2, color2)

    def create_disk(self, playerX, playerY, color):
        '''call the disks' create method,
        passing the desired place to disks'''
        self.disks.create(playerX, playerY, color)

    def update(self):
        '''make necessary changes'''
        # check whether the board is full
        if self.disks.is_full():
            # tell gc what happened
            self.gc.game_over = True
            self.gc.black_count = self.disks.black_count
            self.gc.white_count = self.disks.white_count
            if self.disks.black_count > self.disks.white_count:
                self.gc.black_wins = True
            elif self.disks.black_count < self.disks.white_count:
                self.gc.white_wins = True
            else:
                self.gc.a_tie = True
        else:
            if self.gc.game_over:
                self.gc.black_count = self.disks.black_count
                self.gc.white_count = self.disks.white_count
                if self.disks.black_count > self.disks.white_count:
                    self.gc.black_wins = True
                elif self.disks.black_count < self.disks.white_count:
                    self.gc.white_wins = True
                else:
                    self.gc.a_tie = True

    def display(self):
        '''display the board'''
        # display the disks
        self.update()
        self.disks.display()
        # draw the cross lines
        stroke(0.0, 0.0, 0.0)
        strokeWeight(5)
        for i in range(self.WIDTH//self.CELL_WIDTH + 1):
            line(0, self.CELL_WIDTH * i, self.WIDTH, self.CELL_WIDTH * i)
        for i in range(self.HEIGHT//self.CELL_WIDTH + 1):
            line(self.CELL_WIDTH * i, 0, self.CELL_WIDTH * i, self.HEIGHT)
