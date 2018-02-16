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

    def get_topic_news(self, topic):
        return self.app.get('/api/news/topic/' + topic)

    def test_get_news_topic(self):
        self.post_news("publish", "car",  "New Car Released this Month")
        response = self.get_topic_news('car')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(data['car']), 1)

    def test_get_news_different_topic(self):
        self.post_news("publish", "car",  "New Car Released this Month")
        self.post_news("publish", "politik",  "Pemilu 2018")
        response = self.get_topic_news('car')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(data['car']), 1) 

    def test_get_news_topic_not_found(self):
        self.post_news("publish", "politik",  "Pemilu 2018")
        response = self.get_topic_news('car')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['car'], 'topic was not found') 

    def test_get_news_multi_topic(self):
        self.post_news("publish", ["car", "auto"],  "New Car Released this Month")
        response = self.get_topic_news('car')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(data['car']), 1) 
        response = self.get_topic_news('auto')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(data['auto']), 1) 