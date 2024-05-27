# test_rock_paper_scissors.py

import unittest
from unittest.mock import patch
import rock_paper_scissors

class TestGame(unittest.TestCase):
    @patch('rock_paper_scissors.random.choice')
    def test_game(self, mock_choice):
        mock_choice.side_effect = ['rock', 'scissors']
        rock_paper_scissors.game()
        self.assertEqual(rock_paper_scissors.outcomes['rock'], 1)
        self.assertEqual(rock_paper_scissors.outcomes['scissors'], 0)

if __name__ == '__main__':
    unittest.main()