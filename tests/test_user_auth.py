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

    def test_home_view(self):
        response = self.app.get("/")
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data, 'Please visit our documentation kumparan.aifor.fun/docs')

    def test_home_response_code(self):
        response = self.app.get("/")