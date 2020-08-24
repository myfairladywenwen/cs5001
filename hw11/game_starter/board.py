from disks import Disks


class Board:
    def __init__(self, WIDTH, HEIGHT, CELL_WIDTH, EDGE, game_controller):
        '''draw the chess board and handles interaction
        between game controller, player, and disks'''
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.CELL_WIDTH = CELL_WIDTH
        self.EDGE = EDGE
        self.gc = game_controller
        self.disks = Disks(WIDTH, HEIGHT, CELL_WIDTH, EDGE)
        # create the beginning 4 disks in the middle
        self.disks.create(WIDTH/2 + CELL_WIDTH/2,
                          HEIGHT/2 - CELL_WIDTH/2)
        self.disks.create(WIDTH/2 - CELL_WIDTH/2,
                          HEIGHT/2 - CELL_WIDTH/2)
        self.disks.create(WIDTH/2 - CELL_WIDTH/2,
                          HEIGHT/2 + CELL_WIDTH/2)
        self.disks.create(WIDTH/2 + CELL_WIDTH/2,
                          HEIGHT/2 + CELL_WIDTH/2)

    def create_disk(self, playerX, playerY):
        '''call the disks' create method,
        passing the desired place to disks'''
        self.disks.create(playerX, playerY)

    def update(self):
        '''make necessary changes'''
        # check whether the board is full
        if self.disks.is_full():
            # tell gc what happened
            self.gc.game_over = True
            self.gc.black_count = self.disks.black_count
            self.gc.white_count = self.disks.black_count
            if self.disks.black_count > self.disks.white_count:
                self.gc.black_wins = True
            elif self.disks.black_count < self.disks.white_count:
                self.gc.black_count = self.disks.black_count
            else:
                self.gc.a_tie = True

    def display(self):
        '''display the board'''
        self.update()
        # display the disks
        self.disks.display()
        # draw the cross lines
        stroke(0.0, 0.0, 0.0)
        strokeWeight(5)
        for i in range(self.WIDTH//self.CELL_WIDTH + 1):
            line(0, self.CELL_WIDTH * i, self.WIDTH, self.CELL_WIDTH * i)
        for i in range(self.HEIGHT//self.CELL_WIDTH + 1):
            line(self.CELL_WIDTH * i, 0, self.CELL_WIDTH * i, self.HEIGHT)