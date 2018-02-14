from pymongo import MongoClient
import json

MONGO_URI = 'mongo'


class UserModel:

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        client = MongoClient(MONGO_URI,27017)
        db = client['ner-api']
        collection = db['user']
        result = collection.find_one({'username': username}) 
        if result:
            user = cls(_id=result['_id'], username=result['username'], password=result['password'])
        else:
            user = None

        client.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        client = MongoClient(MONGO_URI, 27017)
        db = client['ner-api']
        collection = db['user']
        result = collection.find_one({'_id': _id}) 
        if result:
            user = cls(_id=result['_id'], username=result['username'], password=result['password'])
        else:
            user = None

        client.close()
        return user
