from newsapi.app import create_app
import unittest
import json

class HomeTest(unittest.TestCase):

    params = {
        'DEBUG': False,
        'TESTING': True,
        'MONGO_DBNAME': 'testing', 
        'MONGO_HOST': 'localhost'
    }

    def setUp(self):
        app = create_app(settings_override=HomeTest.params)
        self.app = app.test_client()

    def test_home_view(self):
        response = self.app.get("/")
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data, 'Please visit our documentation kumparan.aifor.fun/docs')

    def test_home_response_code(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)