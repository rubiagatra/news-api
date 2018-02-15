from pymongo import MongoClient
import json
from newsapi.app import db


class UserModel(db.Document):
    _id = db.IntField()
    username = db.StringField()
    password = db.StringField()

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        if result:
            user = cls(_id=result['_id'], username=result['username'], password=result['password'])
        else:
            user = None

        return user

    @classmethod
    def find_by_id(cls, _id):
        if result:
            user = cls(_id=result['_id'], username=result['username'], password=result['password'])
        else:
            user = None

        return user
