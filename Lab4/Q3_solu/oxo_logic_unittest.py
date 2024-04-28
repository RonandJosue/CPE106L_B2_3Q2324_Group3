import os
import random

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

    def _generate_move(self):
        options = [i for i in range(len(self.board)) if self.board[i] == " "]
        if options:
            return random.choice(options)
        else:
            return -1

    def _is_winning_move(self):
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
        if self._is_winning_move():
            return 'X'
        else:
            return ""

    def computer_move(self):
        cell = self._generate_move()
        if cell == -1:
            return 'D'
        self.board[cell] = 'O'
        if self._is_winning_move():
            return 'O'
        else:
            return ""

    def test(self):
        result = ""
        game = self.new_game()
        while not result:
            print(game)
            try:
                result = self.user_move(self._generate_move())
            except ValueError:
                print("Oops, that shouldn't happen")
            if not result:
                result = self.computer_move()
                
            if not result:
                continue
            elif result == 'D':
                print("It's a draw")
            else:
                print("Winner is:", result)
            print(game)

    def run_tests(self):
        import unittest

        class TestOxoLogic(unittest.TestCase):
            def setUp(self):
                self.game = Game()

            def test_new_game(self):
                self.assertEqual(len(self.game.board), 9)
                self.assertEqual(self.game.board.count(' '), 9)

            def test_user_move(self):
                self.assertEqual(self.game.user_move(0), '')
                self.assertEqual(self.game.user_move(0), 'X')

            def test_computer_move(self):
                self.assertEqual(self.game.computer_move(), '')
                self.assertEqual(self.game.computer_move(), 'O')

            def test_is_winning_move(self):
                self.game.board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
                self.assertTrue(self.game._is_winning_move())

                self.game.board = ['O', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' ']
                self.assertTrue(self.game._is_winning_move())

                self.game.board = ['X', ' ', ' ', 'X', ' ', ' ', 'X', ' ', ' ']
                self.assertTrue(self.game._is_winning_move())

                self.game.board = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
                self.assertTrue(self.game._is_winning_move())

            def test_generate_move(self):
                self.game.board = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
                self.assertEqual(self.game._generate_move(), -1)

        unittest.main()

if __name__ == "__main__":
    game = Game()
    game.run_tests()

