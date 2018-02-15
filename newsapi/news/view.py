from flask_restful import Resource
from pymongo import MongoClient
from newsapi.news import NewsModel


class News(Resource):

    def get(self):
        pass

    def post(self):
        pass


class NewsItem(Resource):

    def get(self, _id):
        pass

    def put(self, _id):
        pass

    def delete(self, _id):
        pass

class NewsTopic(Resource):

    def get(self, topic):

        if not topic:
            pass
    

class NewsStatus(Resource):

    def get(self, status):

        if not status:
            pass
        
