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

    def post_news(self, status, topic, title):
        return self.app.post('/api/news', data=json.dumps(dict(
            status=status,
            topic=topic,
            title=title
        )), headers={
                'Authorization': 'JWT ' + self.token,
                'content-type': 'application/json'})

    def get_status_news(self, status):
        return self.app.get('/api/news/status/' + status,
                 headers={'Authorization': 'JWT ' + self.token})

    def test_get_news_topic(self):
        self.post_news("publish", "car",  "New Car Released this Month")
        response = self.get_status_news('publish')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(data['publish']), 1)

    def test_get_news_topic_empty(self):
        self.post_news("publish", "car",  "New Car Released this Month")
        response = self.get_status_news('draft')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['draft'], "news with {} status was not found".format('draft'))

    