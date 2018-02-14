import unittest
from newsapi.app import create_app
import sys
import json
from newsapi.user import UserModel


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()   

    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(json.loads(response.get_data().decode(sys.getdefaultencoding())), "Please visit our documentation kumparan.aifor.fun/docs")

