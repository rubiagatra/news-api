from flask_restful import Resource, reqparse
from pymongo import MongoClient
from newsapi.news import NewsModel
from flask import request
from flask_jwt import jwt_required


class News(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('status', type=str, required=True,  
                        help="status = ['draft', 'publish', 'deleted']")
    parser.add_argument('topic', type=str, required=True,  
                        help="Please Insert Your Topic")
    parser.add_argument('title', type=str, required=True,
                        help="Please enter your title")


    def get(self):
        return NewsModel.find_all_publish(), 200 

    @jwt_required()
    def post(self):
        data = News.parser.parse_args()
        topic = request.json['topic']
        news = NewsModel(status=data['status'], topic=topic, title=data['title']) 
        news.saveto_db()
        return news.json(), 201


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
        
