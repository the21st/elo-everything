import unittest
from elo_everything import website, utils

class TestWebsite(unittest.TestCase):

    def setUp(self):
        self.app = website.app.test_client()
        self.app.testing = True 

    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_leaderboard_page(self):
        response = self.app.get('/leaderboard')
        self.assertEqual(response.status_code, 200)

    def test_get_random_concepts(self):
        concepts = utils.get_random_concepts()
        self.assertEqual(len(concepts), 2)
        self.assertNotEqual(concepts[0], concepts[1])

    def test_vote(self):
        response = self.app.post('/vote', data=dict(concept_id=1))
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()