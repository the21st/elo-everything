import unittest
from flask import url_for
from elo_everything import app, db
from elo_everything.models.concept import Concept

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_home_page(self):
        response = self.app.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_leaderboard_page(self):
        response = self.app.get(url_for('leaderboard'))
        self.assertEqual(response.status_code, 200)

    def test_vote(self):
        concept1 = Concept(name='Water', elo_score=1000)
        concept2 = Concept(name='Common Cold', elo_score=1000)
        db.session.add(concept1)
        db.session.add(concept2)
        db.session.commit()

        response = self.app.post(url_for('vote'), data={'winner': concept1.id, 'loser': concept2.id})
        self.assertEqual(response.status_code, 200)

        updated_concept1 = Concept.query.get(concept1.id)
        updated_concept2 = Concept.query.get(concept2.id)
        self.assertGreater(updated_concept1.elo_score, 1000)
        self.assertLess(updated_concept2.elo_score, 1000)

if __name__ == "__main__":
    unittest.main()