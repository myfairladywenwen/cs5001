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
        self.ai_thinking = False
        self.waiting = 0

    def update(self):
        '''carries out necessary actions if game is over or ai is thinking'''
        if not self.game_over:
            if self.ai_thinking:
                fill(1, 1, 0)
                textSize(30)
                text("AI's TURN.\nAI IS THINKING...",
                     self.WIDTH/2 - 140, self.HEIGHT/2)
            else:
                fill(1, 0, 0)
                textSize(30)
                text("PLAYER's TURN.\nPLAYER IS THINKING...",
                     self.WIDTH/2 - 140, self.HEIGHT/2)
        else:
            if self.black_wins:
                fill(1, 0, 0)
                textSize(30)
                text("GAME OVER.\nBLACK WINS.\nBLACK: " +
                     str(self.black_count) + " TILES.\nWHITE: " +
                     str(self.white_count) + " TILES.",
                     self.WIDTH/2 - 140, self.HEIGHT/2)
            elif self.white_wins:
                fill(1, 1, 0)
                textSize(30)
                text("GAME OVER.\nWHITE WINS.\nBLACK: " +
                     str(self.black_count) + " TILES.\nWHITE" +
                     str(self.white_count) + " TILES.",
                     self.WIDTH/2 - 140, self.HEIGHT/2)
            elif self.a_tie:
                fill(1, 0, 0)
                textSize(30)
                text("GAME OVER.\nA TIE.\nEACH HAS " +
                     str(self.white_count) + " TILES.",
                     self.WIDTH/2 - 140, self.HEIGHT/2)
            self.waiting += 1
            if self.waiting > 120:
                self.prompt_user()

    def prompt_user(self):
        """prompt for user name
        and write down in the score.txt according to the score"""
        answer = self.input('enter your name')
        if answer:
            print('hi ' + answer)
        elif answer == '':
            print('[empty string]')
        else:
            print(answer)  # Canceled dialog will print None
        with open("score.txt", 'r+') as score:
            content = score.readline()
            if content:
                current_max = int(content[content.rfind(" ")+1:-1])
                if current_max < self.black_count:
                    copy = answer + " " + str(self.black_count) + "\n"
                    copy += content
                    for line in score:
                        copy += line
                    with open("score.txt", "w") as score_new:
                        score_new.write(copy)
                else:
                    with open("score.txt", "a") as score_new:
                        score_new.write(answer + " "
                                        + str(self.black_count) + "\n")
            else:
                score.write(answer + " " + str(self.black_count) + "\n")
        exit()

    def input(self, message=''):
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)
