from newsapi.app import create_app
import unittest
import json
from pymongo import MongoClient
from config.settings import MONGO_PORT

class AuthTest(unittest.TestCase):

    params = {
        'DEBUG': False,
        'TESTING': True,
        'MONGO_DBNAME': 'testing',
        'MONGO_HOST': 'localhost'
    }

    def setUp(self):
        app = create_app(settings_override=AuthTest.params)
        self.app = app.test_client()

    @classmethod
    def tearDownClass(cls):
        client =  MongoClient(AuthTest.params['MONGO_HOST'], MONGO_PORT)
        client.drop_database(AuthTest.params['MONGO_DBNAME'])
        client.close()
