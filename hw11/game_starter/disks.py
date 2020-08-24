from disk import Disk


class Disks:
    "List of list, consisting of disks"

    def __init__(self, WIDTH, HEIGHT, CELL_WIDTH, EDGE):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.CELL_WIDTH = CELL_WIDTH
        self.EDGE = EDGE
        self.num_of_rows = self.HEIGHT/CELL_WIDTH
        self.num_of_cols = self.WIDTH/CELL_WIDTH
        self.matrix = [[None] * self.num_of_cols
                       for i in range(self.num_of_rows)]
        self.black_count = 0
        self.white_count = 0
        self.total_step = 0
        self.total_disks = 0

    def create(self, playerX, playerY):
        '''create a disk on desired, legal place'''
        if not self.is_full():
            curr_col = playerX//self.CELL_WIDTH
            curr_row = playerY//self.CELL_WIDTH
            if self.cell_is_empty(curr_row, curr_col):
                # decide the color
                if self.total_step % 2 == 0:
                    color = (0, 0, 0)
                else:
                    color = (1, 1, 1)
                self.matrix[curr_row][curr_col] = Disk(curr_row, curr_col,
                                                       color,
                                                       self.CELL_WIDTH,
                                                       self.EDGE)
                self.total_step += 1
                self.total_disks += 1
                if color == (0, 0, 0):
                    self.black_count += 1
                else:
                    self.white_count += 1

    def cell_is_empty(self, row, col):
        '''check whether the cell is empty'''
        if self.matrix[row][col] is None:
            return True
        else:
            return False

    def is_full(self):
        '''check whether all cells have been taken up'''
        if self.total_disks == self.num_of_rows * self.num_of_cols:
            return True
        else:
            return False

    def display(self):
        '''call each disk's display method'''
        for row in range(self.num_of_rows):
            for col in range(self.num_of_cols):
                if not self.cell_is_empty(row, col):
                    self.matrix[row][col].display()
