from newsapi.app import create_app
import unittest
import json
from pymongo import MongoClient
from config.settings import MONGO_PORT


class NewsTest(unittest.TestCase):

    params = {
        'DEBUG': False,
        'TESTING': True,
        'MONGO_DBNAME': 'testing',
        'MONGO_HOST': 'localhost'   #Using Your machine/travis for testing Delete this if using docker for testing 
    }
    def auth(self, username, password):
        response = self.app.post('/auth', data=json.dumps(dict(
            username=username,
            password=password
        )), content_type='application/json')    
        data = json.loads(response.get_data(as_text=True))
        return  data['access_token']

    def setUp(self):
        app = create_app(settings_override=NewsTest.params)
        self.app = app.test_client()
        self.token = self.auth('sandbox', 'sandbox')

    def tearDown(self):
        client =  MongoClient(NewsTest.params['MONGO_HOST'], MONGO_PORT)
        client.drop_database(NewsTest.params['MONGO_DBNAME'])
        client.close()

    def test_get_empty_news(self):
        response = self.app.get('/api/news')   
        data = json.loads(response.get_data())
        self.assertEqual(len(data["published_news"]), 0)

    def post_news(self, status, topic, title):
        return self.app.post('/api/news', data=json.dumps(dict(
            status=status,
            topic=topic,
            title=title
        )), headers={
                'Authorization': 'JWT ' + self.token,
                'content-type': 'application/json'})

    def test_post_news(self):
        response = self.post_news("publish", "car",  "New Car Released this Month")
        data = json.loads(response.get_data(as_text=True))['news']
        self.assertEqual(type(data['id']), int)
        self.assertEqual(data['status'], 'publish')
        self.assertEqual(data['topic'], 'car')
        self.assertEqual(data['title'], "New Car Released this Month" )

    def test_get_news_and_publish(self):
        self.post_news("publish", "car",  "New Car Released this Month")
        response = self.app.get('/api/news')   
        data = json.loads(response.get_data())
        self.assertEqual(len(data["published_news"]), 1)
        self.assertEqual(data['published_news'][0]['status'], 'publish')

    def test_get_news_empty_draft(self):
        self.post_news("draft", "car",  "New Car Released this Month")
        response = self.app.get('/api/news')   
        data = json.loads(response.get_data())
        self.assertEqual(len(data["published_news"]), 0)