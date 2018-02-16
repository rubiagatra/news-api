from newsapi.app import create_app
import unittest
import json
from pymongo import MongoClient
from config.settings import MONGO_PORT

class HomeTest(unittest.TestCase):

    params = {
        'DEBUG': False,
        'TESTING': True,
        'MONGO_DBNAME': 'testing',
        'MONGO_HOST': 'localhost' #Using Your machine/travis for testing Delete this if using docker for testing 
    }

    def setUp(self):
        app = create_app(settings_override=HomeTest.params)
        self.app = app.test_client()

    @classmethod
    def tearDownClass(cls):
        client =  MongoClient(HomeTest.params['MONGO_HOST'], MONGO_PORT)
        client.drop_database(HomeTest.params['MONGO_DBNAME'])
        client.close()

    def test_home_view(self):
        response = self.app.get("/")
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data, 'Please visit our documentation kumparan.aifor.fun/docs')

    def test_home_response_code(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)