from pymongo import MongoClient

MONGO_URI = 'localhost'

class NewsModel:

    def __init__(self, status, topic, title):
        self._id = None
        self.status = status
        self.topic = topic
        self.title = title

    def saveto_db(self):
        client = MongoClient(MONGO_URI, 27017)
        db = client['news-api']    
        count = db['counter'].find_one()['count']
        new_count = count + 1
        db['counter'].find_and_modify({"count": count}, {"count": new_count})
        collection_news = db['news']
        if type(self.topic) is str:
            self.topic = [self.topic]
        data = collection_news.insert({'_id': new_count, 'status': self.status,
                                'topic': self.topic, 'title': self.title})
        self._id = data
        client.close()

    def json(self):
        return {'news': {'_id': self._id,
                        'topic': self.topic, 'status': self.status, 'title':self.title}}

    @classmethod
    def find_all_publish(cls):
        client = MongoClient(MONGO_URI, 27017)
        db = client['news-api']
        collection_news = db['news']
        result = [x for x in collection_news.find({'topic': 'publish'})]
        return {'published_news': result}
