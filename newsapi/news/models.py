from pymongo import MongoClient
from newsapi.database import mongo


class NewsModel:

    def __init__(self, status, topic, title, _id=None):
        self.id = _id 
        self.status = status
        self.topic = topic
        self.title = title

    def saveto_db(self):
        count = mongo.db.counter.find_one()['count']
        new_count = count + 1
        mongo.db.counter.find_one_and_update({"count": count}, {"$set":{"count": new_count}})
        mongo.db.news.insert_one({'_id': new_count, 'status': self.status,
                                'topic': self.topic, 'title': self.title})
        self.id = mongo.db.news.find_one({'title': self.title})['_id']

    def get_json(self):
        return {'news': {'id': self.id,
                        'topic': self.topic, 'status': self.status, 'title':self.title}}

    @classmethod
    def find_all_publish(cls):
        result = [x for x in mongo.db.news.find({'status': 'publish'})]
        return {'published_news': result}

    @classmethod
    def find_by_id(cls, id):
        result = mongo.db.news.find_one({'_id': id})
        if result:
            return cls(status=result['status'], topic=result['topic'], 
                        title=result['title'], _id=id)
        else:
            None

    @classmethod
    def find_by_topic(cls, topic):
        result = mongo.db.news.find({'topic': topic})
        result = [x for x in result]
        if result:
            return {topic: result}
        return None
    
    @classmethod
    def find_by_status(cls, status):
        result = mongo.db.news.find({'status': status})
        result = [x for x in result]
        if result:
            return {status: result}
        return None

    def update_db(self):
        mongo.db.news.find_one_and_update(filter={"_id": self.id}, 
                                          update={'$set' : {'title': self.title,
                                                             'topic':self.topic, 
                                                             'status': self.status}})

    def delete(self):
        mongo.db.news.find_one_and_delete({'_id': self.id})
        

