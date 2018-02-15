from pymongo import MongoClient

MONGO_URI = 'localhost'

class NewsModel:

    def __init__(self, status, topic, title, _id=None):
        self.id = _id 
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
        data = collection_news.insert({'_id': new_count, 'status': self.status,
                                'topic': self.topic, 'title': self.title})
        self._id = data
        client.close()

    def json(self):
        return {'news': {'id': self.id,
                        'topic': self.topic, 'status': self.status, 'title':self.title}}

    @classmethod
    def find_all_publish(cls):
        client = MongoClient(MONGO_URI, 27017)
        db = client['news-api']
        collection_news = db['news']
        result = [x for x in collection_news.find({'status': 'publish'})]
        return {'published_news': result}

    @classmethod
    def find_by_id(cls, id):
        client = MongoClient(MONGO_URI, 27017)
        db = client['news-api']
        collection_news = db['news']
        result = collection_news.find_one({'_id': id})
        if result:
            return cls(status=result['status'], topic=result['topic'], 
                        title=result['title'], _id=id)
        else:
            None

    @classmethod
    def find_by_topic(cls, topic):
        client = MongoClient(MONGO_URI, 27017)
        db = client['news-api']
        collection_news = db['news']
        result = collection_news.find({'topic': topic})
        result = [x for x in result]
        if result:
            return {topic: result}
        return None
    
    @classmethod
    def find_by_status(cls, status):
        client = MongoClient(MONGO_URI, 27017)
        db = client['news-api']
        collection_news = db['news']
        result = collection_news.find({'status': status})
        result = [x for x in result]
        if result:
            return {status: result}
        return None

    def update_db(self, id):
        client = MongoClient(MONGO_URI, 27017)
        db = client['news-api']
        collection = db['news']
        collection.find_one_and_update(filter={"_id": id}, 
                                       update={'$set' : {'title': self.title,
                                                        'topic':self.topic, 'status': self.status}})
        client.close()

    def delete(self, id):
        client = MongoClient(MONGO_URI, 27017)
        db = client['news-api']
        collection = db ['news']
        collection.find_one_and_delete({'_id': id})
        client.close()

