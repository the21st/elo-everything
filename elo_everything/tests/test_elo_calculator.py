import unittest
from elo_everything.utils.elo_calculator import calculate_elo

class TestEloCalculator(unittest.TestCase):

    def setUp(self):
        self.current_rating1 = 1200
        self.current_rating2 = 1400

    def test_calculate_elo(self):
        new_rating1, new_rating2 = calculate_elo(self.current_rating1, self.current_rating2, 1)

        # Check if the ratings are updated correctly
        self.assertTrue(new_rating1 > self.current_rating1)
        self.assertTrue(new_rating2 < self.current_rating2)

        new_rating1, new_rating2 = calculate_elo(self.current_rating1, self.current_rating2, 0)

        # Check if the ratings are updated correctly
        self.assertTrue(new_rating1 < self.current_rating1)
        self.assertTrue(new_rating2 > self.current_rating2)

if __name__ == '__main__':
    unittest.main()