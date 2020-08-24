from player import Player
from board import Board
from random import randint


class GameManager():
    '''control swith of turns and let human/ai player take action'''
    def __init__(self, human_player, ai_player, board, game_controller):
        self.human_player = human_player
        self.ai_player = ai_player
        self.human_turn = True
        self.board = board
        self.gc = game_controller

    def human_make_move(self, x, y):
        """ai player make a move and corresponding flip"""
        legal_cells = self.get_legal_cells(self.board.human_color)
        if len(legal_cells) != 0:
            curr_row = int(y//self.board.CELL_WIDTH)
            curr_col = int(x//self.board.CELL_WIDTH)
            if (curr_row, curr_col) in legal_cells.keys():
                # place a disk of black
                self.human_player.human_move(x, y, self.board.human_color)
                # flip white disk to black
                for (flip_r, flip_c) in (legal_cells[(curr_row, curr_col)]):
                    self.board.disks.create(flip_c * self.board.CELL_WIDTH +
                                            self.board.CELL_WIDTH/2,
                                            flip_r * self.board.CELL_WIDTH +
                                            self.board.CELL_WIDTH/2,
                                            self.board.human_color)
                self.board.disks.white_count -= len(legal_cells[(curr_row,
                                                                 curr_col)])
                self.board.disks.total_disks -= len(legal_cells[(curr_row,
                                                                 curr_col)])
                self.human_turn = False
        # if no legal moves for human, check whether has legal move for ai
        else:
            legal_cells_ai = self.get_legal_cells(self.board.ai_color)
            if len(legal_cells_ai) != 0:
                self.human_turn = False
            else:
                self.gc.game_over = True

    def ai_make_move(self):
        """ai player make a move and corresponding flip"""
        legal_cells = self.get_legal_cells(self.board.ai_color)
        if len(legal_cells.keys()) != 0:
            curr_row, curr_col = self.generate_ai_pos(legal_cells)
            # place a disk of white
            self.ai_player.ai_move(curr_row, curr_col, self.board.ai_color)
            # flip black disk to white
            for (flip_r, flip_c) in (legal_cells[(curr_row, curr_col)]):
                self.board.disks.create(flip_c * self.board.CELL_WIDTH +
                                        self.board.CELL_WIDTH/2,
                                        flip_r * self.board.CELL_WIDTH +
                                        self.board.CELL_WIDTH/2,
                                        self.board.ai_color)
            self.board.disks.black_count -= len(legal_cells[(curr_row,
                                                             curr_col)])
            self.board.disks.total_disks -= len(legal_cells[(curr_row,
                                                             curr_col)])
            # after ai move, check whether human player has legal moves
            legal_cells_human = self.get_legal_cells(self.board.human_color)
            if len(legal_cells_human) != 0:
                self.human_turn = True
            else:
                if len(self.get_legal_cells(self.board.ai_color)) == 0:
                    self.gc.game_over = True
                else:
                    self.human_turn = False
        # if no legal moves for ai, check whether has legal move for human
        else:
            legal_cells_human = self.get_legal_cells(self.board.human_color)
            if len(legal_cells_human) != 0:
                self.human_turn = True
            else:
                self.gc.game_over = True

    def generate_ai_pos(self, legal_cells):
        """generate a legal position for ai,
        with longest list of black disks to flip"""
        max_length = 0
        for pair in legal_cells.items():
            if len(pair[1]) > max_length:
                max_length = len(pair[1])
                ai_pos = pair[0]
        return ai_pos

    def get_legal_cells(self, player_color):
        """return a dictionary of legal cells,
        with legal cell as the key, and
        corresponding cells to flip as the value"""
        # mark the edge as constants
        MAX_EDGE_IDX = int(self.board.WIDTH / self.board.CELL_WIDTH) - 1
        MIN_EDGE_IDX = 0
        legal_cells = {}
        for i in range(MAX_EDGE_IDX + 1):
            for j in range(MAX_EDGE_IDX + 1):
                if self.board.disks.matrix[i][j] is None:
                    # horizon left
                    to_flip_list = []
                    left = j - 1
                    while (left >= MIN_EDGE_IDX):
                        if self.board.disks.matrix[i][left]:
                            if (self.board.disks.matrix[i][left].color !=
                                    player_color):
                                to_flip_list.append((i, left))
                                left -= 1
                            elif (self.board.disks.matrix[i][left].color ==
                                    player_color and len(to_flip_list) != 0):
                                legal_cells[(i, j)] = to_flip_list
                                break
                            else:
                                break
                        else:
                            break
                    # horizon right
                    to_flip_list = []
                    right = j + 1
                    while (right <= MAX_EDGE_IDX):
                        if self.board.disks.matrix[i][right]:
                            if (self.board.disks.matrix[i][right].color !=
                                    player_color):
                                to_flip_list.append((i, right))
                                right += 1
                            elif (self.board.disks.matrix[i][right].color ==
                                    player_color and len(to_flip_list) != 0):
                                if (i, j) in legal_cells.keys():
                                    legal_cells[(i, j)] += to_flip_list
                                else:
                                    legal_cells[(i, j)] = to_flip_list
                                break
                            else:
                                break
                        else:
                            break
                    # straight up
                    to_flip_list = []
                    up = i - 1
                    while (up >= 0):
                        if self.board.disks.matrix[up][j]:
                            if (self.board.disks.matrix[up][j].color !=
                                    player_color):
                                to_flip_list.append((up, j))
                                up -= 1
                            elif (self.board.disks.matrix[up][j].color ==
                                    player_color and len(to_flip_list) != 0):
                                if (i, j) in legal_cells.keys():
                                    legal_cells[(i, j)] += to_flip_list
                                else:
                                    legal_cells[(i, j)] = to_flip_list
                                break
                            else:
                                break
                        else:
                            break
                    # straight down
                    to_flip_list = []
                    down = i + 1
                    while (down <= MAX_EDGE_IDX):
                        if self.board.disks.matrix[down][j]:
                            if (self.board.disks.matrix[down][j].color !=
                                    player_color):
                                to_flip_list.append((down, j))
                                down += 1
                            elif (self.board.disks.matrix[down][j].color ==
                                    player_color and len(to_flip_list) != 0):
                                if (i, j) in legal_cells.keys():
                                    legal_cells[(i, j)] += to_flip_list
                                else:
                                    legal_cells[(i, j)] = to_flip_list
                                break
                            else:
                                break
                        else:
                            break
                    # up left
                    to_flip_list = []
                    left = j - 1
                    up = i - 1
                    while (left >= MIN_EDGE_IDX and up >= MIN_EDGE_IDX):
                        if self.board.disks.matrix[up][left]:
                            if (self.board.disks.matrix[up][left].color !=
                                    player_color):
                                to_flip_list.append((up, left))
                                left -= 1
                                up -= 1
                            elif (self.board.disks.matrix[up][left].color ==
                                    player_color and len(to_flip_list) != 0):
                                if (i, j) in legal_cells.keys():
                                    legal_cells[(i, j)] += to_flip_list
                                else:
                                    legal_cells[(i, j)] = to_flip_list
                                break
                            else:
                                break
                        else:
                            break
                    # up right
                    to_flip_list = []
                    right = j + 1
                    up = i - 1
                    while (right <= MAX_EDGE_IDX and up >= MIN_EDGE_IDX):
                        if self.board.disks.matrix[up][right]:
                            if (self.board.disks.matrix[up][right].color !=
                                    player_color):
                                to_flip_list.append((up, right))
                                right += 1
                                up -= 1
                            elif (self.board.disks.matrix[up][right].color ==
                                    player_color and len(to_flip_list) != 0):
                                if (i, j) in legal_cells.keys():
                                    legal_cells[(i, j)] += to_flip_list
                                else:
                                    legal_cells[(i, j)] = to_flip_list
                                break
                            else:
                                break
                        else:
                            break
                    # down left
                    to_flip_list = []
                    left = j - 1
                    down = i + 1
                    while (left >= MIN_EDGE_IDX and down <= MAX_EDGE_IDX):
                        if self.board.disks.matrix[down][left]:
                            if (self.board.disks.matrix[down][left].color !=
                                    player_color):
                                to_flip_list.append((down, left))
                                left -= 1
                                down += 1
                            elif (self.board.disks.matrix[down][left].color ==
                                    player_color and len(to_flip_list) != 0):
                                if (i, j) in legal_cells.keys():
                                    legal_cells[(i, j)] += to_flip_list
                                else:
                                    legal_cells[(i, j)] = to_flip_list
                                break
                            else:
                                break
                        else:
                            break
                    # down right
                    to_flip_list = []
                    right = j + 1
                    down = i + 1
                    while (right <= MAX_EDGE_IDX and down <= MAX_EDGE_IDX):
                        if self.board.disks.matrix[down][right]:
                            if (self.board.disks.matrix[down][right].color !=
                                    player_color):
                                to_flip_list.append((down, right))
                                right += 1
                                down += 1
                            elif (self.board.disks.matrix[down][right].color ==
                                    player_color and len(to_flip_list) != 0):
                                if (i, j) in legal_cells.keys():
                                    legal_cells[(i, j)] += to_flip_list
                                else:
                                    legal_cells[(i, j)] = to_flip_list
                                break
                            else:
                                break
                        else:
                            break
        return legal_cells
