import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from models import setup_db, Movies, Actors, create_and_drop_all
from app import create_app

DATABASE_URL = os.getenv('DATABASE_URL')
ASSISTANT_TOKEN = os.getenv('ASSISTANT_TOKEN')
DIRECTOR_TOKEN = os.getenv('DIRECTOR_TOKEN')
PRODUCER_TOKEN = os.getenv('PRODUCER_TOKEN')

movie = {
            "title": "my life",
            "release_date": "2001-01-01",
        }

actor = {
            "name": "Abdullah",
            "age": "30",
            "gender": "male"
        }

class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the casting agency test case"""

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app, DATABASE_URL)
        self.casting_assistant = ASSISTANT_TOKEN
        self.casting_director = DIRECTOR_TOKEN
        self.executive_producer = PRODUCER_TOKEN
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            create_and_drop_all()
            # self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass
    
    def test_get_movies(self):
        res = self.client().get('/movies',
                                headers={
                                    "Authorization": "Bearer {}"
                                    .format(self.casting_assistant)
                                })
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(len(data['movies']), 0)
    
    def test_get_movie_by_id(self):
        res = self.client().get('/movies/2',
                                headers={
                                    "Authorization": "Bearer {}"
                                    .format(self.casting_assistant)
                                })
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(len(data['movie']), 1)
    
    def test_get_movie_by_id_error(self):
        res = self.client().get('/movies/2')
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])
        
    
    def test_get_movies_error(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])
    
    def test_get_actors(self):
        res = self.client().get('/actors',
                                headers={
                                    "Authorization": "Bearer {}"
                                    .format(self.executive_producer)
                                })
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(len(data['actors']), 0)
    
    def test_get_actors_error(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])
    
    def test_get_actor_by_id(self):
        res = self.client().get('/actors/2',
                                headers={
                                    "Authorization": "Bearer {}"
                                    .format(self.executive_producer)
                                })
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(len(data['actor']), 1)
    
    def test_get_actor_by_id_error(self):
        res = self.client().get('/actors/2')
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])
    
    def test_delete_movie_by_id(self):
        res = self.client().delete('/movies/2',
                                headers={
                                    "Authorization": "Bearer {}"
                                    .format(self.executive_producer)
                                })
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsNotNone(data['delete'])
    
    def test_delete_movie_by_id_error(self):
        res = self.client().delete('/movies/2')
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])
    
    def test_delete_actor_by_id(self):
        res = self.client().delete('/actors/2',
                                headers={
                                    "Authorization": "Bearer {}"
                                    .format(self.executive_producer)
                                })
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsNotNone(data['delete'])
    
    def test_delete_actor_by_id_error(self):
        res = self.client().delete('/actors/2')
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code, 401)
        self.assertFalse(data['success'])
    
    def test_post_movies(self):
        res = self.client().post('/movies',
                                headers={
                                    "Authorization": "Bearer {}"
                                    .format(self.executive_producer)
                                }, json = movie)
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsNotNone(data['movie'])
    
    def test_post_movies_error(self):
        res = self.client().post('/movies',
                                headers={
                                    "Authorization": "Bearer {}"
                                    .format(self.executive_producer)
                                })
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code, 400)
        self.assertFalse(data['success'])
        
    
    def test_post_actors(self):
        res = self.client().post('/actors',
                                headers={
                                    "Authorization": "Bearer {}"
                                    .format(self.casting_director)
                                }, json = actor)
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsNotNone(data['actor'])
    
    def test_post_actors_error(self):
        res = self.client().post('/actors',
                                headers={
                                    "Authorization": "Bearer {}"
                                    .format(self.casting_director)
                                })
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code, 400)
        self.assertFalse(data['success'])
    
    def test_patch_movies(self):
        res = self.client().patch('/movies/2',
                                headers={
                                    "Authorization": "Bearer {}"
                                    .format(self.executive_producer)
                                }, json = movie)
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsNotNone(data['movie'])
    
    def test_patch_movies_error(self):
        res = self.client().patch('/movies/2',
                                headers={
                                    "Authorization": "Bearer {}"
                                    .format(self.executive_producer)
                                })
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code, 400)
        self.assertFalse(data['success'])
    
    def test_patch_actors(self):
        res = self.client().patch('/actors/2',
                                headers={
                                    "Authorization": "Bearer {}"
                                    .format(self.executive_producer)
                                }, json = actor)
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertIsNotNone(data['actor'])
    
    def test_patch_actors_error(self):
        res = self.client().patch('/actors/2',
                                headers={
                                    "Authorization": "Bearer {}"
                                    .format(self.executive_producer)
                                })
        data = json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code, 400)
        self.assertFalse(data['success'])
        
        
    



if __name__ == "__main__":
    unittest.main()
