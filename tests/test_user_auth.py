from newsapi.app import create_app
import unittest
import json
from pymongo import MongoClient
from config.settings import MONGO_HOST, MONGO_PORT

class AuthTest(unittest.TestCase):

    params = {
        'DEBUG': False,
        'TESTING': True,
        'MONGO_DBNAME': 'testing'
    }

    def setUp(self):
        app = create_app(settings_override=AuthTest.params)
        self.app = app.test_client()

    @classmethod
    def tearDownClass(cls):
        client =  MongoClient(MONGO_HOST, MONGO_PORT)
        client.drop_database(AuthTest.params['MONGO_DBNAME'])
        client.close()

    def auth(self, username, password):
        return self.app.post('/auth', data=dict(
            username=username,
            password=password
        ))

    def test_token_not_empty(self):
        response = self.auth('sandbox', 'sandbox')
        data = json.loads(response.get_data())
        self.assertNotEqual(data['access_token'], None)
        