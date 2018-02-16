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

    def put_news_by_id(self, id, status=None, topic=None, title=None):
        return self.app.put('/api/news/'+ str(id), data=json.dumps(dict(
            status=status,
            topic=topic,
            title=title
        )), headers={
                'Authorization': 'JWT ' + self.token,
                'content-type': 'application/json'})

    def post_news(self, status, topic, title):
        return self.app.post('/api/news', data=json.dumps(dict(
            status=status,
            topic=topic,
            title=title
        )), headers={
                'Authorization': 'JWT ' + self.token,
                'content-type': 'application/json'})

    def get_news_by_id(self, id):
        return self.app.get('/api/news/' + str(id),
                 headers={'Authorization': 'JWT ' + self.token})

    def test_get_news_by_id(self):
        self.post_news("publish", "car",  "New Car Released this Month")
        response = self.get_news_by_id(1)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['news']['id'], 1)

    def test_get_news_by_id_not_found(self):
        self.post_news("publish", "car",  "New Car Released this Month")
        response = self.get_news_by_id(2)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['news'], 'News not found')

    def delete_news_by_id(self, id):
        return self.app.delete('/api/news/' + str(id),
                 headers={'Authorization': 'JWT ' + self.token})

    def test_delete_news_by_id(self):
        self.post_news("publish", "car",  "New Car Released this Month")
        response = self.delete_news_by_id(1)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['news'], 'News was deleted')

    def test_delete_news_by_id_not_found(self):
        self.post_news("publish", "car",  "New Car Released this Month")
        response = self.delete_news_by_id(2)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['news'], 'News was not found')

    def test_put_news_by_id_not_found(self):
        self.post_news("publish", "car",  "New Car Released this Month")
        response = self.put_news_by_id(2)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['news'], 'News was not found')

    def test_put_one_status_news_by_id(self):
        self.post_news("publish", "car",  "New Car Released this Month")
        response = self.put_news_by_id(1, status='draft')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['news']['status'], 'draft')

    def test_put_one_topic_news_by_id(self):
        self.post_news("publish", "car",  "New Car Released this Month")
        response = self.put_news_by_id(1, topic='auto')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['news']['topic'], 'auto')

    def test_put_one_title_news_by_id(self):
        self.post_news("publish", "car",  "New Car Released this Month")
        response = self.put_news_by_id(1, title='Honda just Launch a Car')
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['news']['title'], 'Honda just Launch a Car')

    