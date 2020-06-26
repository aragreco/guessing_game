import unittest
import guess_game


class TestGame(unittest.TestCase):
    def test_game(self):
        answer = 5
        guess = 5
        result = guess_game.run_guess(answer, guess)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()