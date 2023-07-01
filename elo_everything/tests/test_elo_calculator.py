import unittest
from elo_everything.elo_calculator import calculate_elo

class TestEloCalculator(unittest.TestCase):
    def setUp(self):
        self.score1 = 1200
        self.score2 = 1000

    def test_calculate_elo(self):
        new_score1, new_score2 = calculate_elo(self.score1, self.score2, 1)
        self.assertTrue(new_score1 > self.score1)
        self.assertTrue(new_score2 < self.score2)

        new_score1, new_score2 = calculate_elo(self.score1, self.score2, 0)
        self.assertTrue(new_score1 < self.score1)
        self.assertTrue(new_score2 > self.score2)

if __name__ == '__main__':
    unittest.main()