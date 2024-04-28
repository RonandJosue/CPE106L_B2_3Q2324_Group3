import os, random
import oxo_data

class Game:
    def __init__(self):
        self.board = self.new_game()

    def new_game(self):
        return list(" " * 9)

    def save_game(self):
        oxo_data.saveGame(self.board)

    def restore_game(self):
        try:
            game = oxo_data.restoreGame()
            if len(game) == 9:
                return game
            else:
                return self.new_game()
        except IOError:
            return self.new_game()

    def generate_move(self):
        options = [i for i in range(len(self.board)) if self.board[i] == " "]
        if options:
            return random.choice(options)
        else:
            return -1

    def is_winning_move(self):
        wins = ((0,1,2), (3,4,5), (6,7,8),
                (0,3,6), (1,4,7), (2,5,8),
                (0,4,8), (2,4,6))

        for a, b, c in wins:
            chars = self.board[a] + self.board[b] + self.board[c]
            if chars == 'XXX' or chars == 'OOO':
                return True
        return False

    def user_move(self, cell):
        if self.board[cell] != ' ':
            raise ValueError('Invalid cell')
        else:
            self.board[cell] = 'X'
        if self.is_winning_move():
            return 'X'
        else:
            return ""

    def computer_move(self):
        cell = self.generate_move()
        if cell == -1:
            return 'D'
        self.board[cell] = 'O'
        if self.is_winning_move():
            return 'O'
        else:
            return ""

def test():
    result = ""
    game = Game()
    while not result:
        print(game.board)
        try:
           result = game.user_move(game.generate_move())
        except ValueError:
            print("Oops, that shouldn't happen")
        if not result:
            result = game.computer_move()
            
        if not result:
            continue
        elif result == 'D':
            print("It's a draw")
        else:
            print("Winner is:", result)
        print(game.board)

if __name__ == "__main__":
    test()

