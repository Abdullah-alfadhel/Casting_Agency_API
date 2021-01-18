import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from flaskr.database.models import setup_db, Movie, Actor, create_and_drop_all
from flaskr import create_app

TEST_DATABASE_URI = os.getenv('TEST_DATABASE_URI')
ASSISTANT_TOKEN = os.getenv('ASSISTANT_TOKEN')
DIRECTOR_TOKEN = os.getenv('DIRECTOR_TOKEN')
PRODUCER_TOKEN = os.getenv('PRODUCER_TOKEN')


class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the casting agency test case"""

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app, TEST_DATABASE_URI)
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



if __name__ == "__main__":
    unittest.main()
