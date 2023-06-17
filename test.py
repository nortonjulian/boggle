from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage_route(self):
        with self.client:
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Boggle', response.data)
            self.assertIn(b'High Score:', response.data)
            self.assertIn(b'Score:', response.data)
            self.assertIn(b'Seconds Left:', response.data)

    def test_check_word_route_valid_word(self):
        with self.client:
            with app.test_request_context():
                session['board'] = [['A', 'B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'J', 'K', 'L'], ['M', 'N', 'O', 'P']]
            response = self.client.get('/check-word?word=ABC')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['response'], True)

    def test_check_word_route_invalid_word(self):
        with self.client:
            with app.test_request_context():
                session['board'] = [['A', 'B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'J', 'K', 'L'], ['M', 'N', 'O', 'P']]
            response = self.client.get('/check-word?word=XYZ')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['response'], False)

    def test_post_score_route_high_score_broken(self):
        with self.client:
            with app.test_request_context():
                session['high_score'] = 100
                session['num_of_plays'] = 5
            response = self.client.post('/post-score', json={'score': 150})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['brokeRecord'], True)
            with app.test_request_context():
                self.assertEqual(session['num_of_plays'], 6)
                self.assertEqual(session['high_score'], 150)

    def test_post_score_route_high_score_not_broken(self):
        with self.client:
            with app.test_request_context():
                session['high_score'] = 100
                session['num_of_plays'] = 5
            response = self.client.post('/post-score', json={'score': 80})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json['brokeRecord'], False)
            with app.test_request_context():
                self.assertEqual(session['num_of_plays'], 6)
                self.assertEqual(session['high_score'], 100)
