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

    def get(self, id):
        result = NewsModel.find_by_id(id)
        if result:
            return result.json(), 200
        else:
            return {'news': 'News not found'}, 404


    def put(self, id):
        result = NewsModel.find_by_id(id)
        if result:
            pass
        pass
            

    def delete(self, id):
        pass

class NewsTopic(Resource):

    def get(self, topic):
        result = NewsModel.find_by_topic(topic)
        if result:
            return result, 200 
        return {'topic': 'topic was not found'}, 404
    

class NewsStatus(Resource):

    def get(self, status):
        result = NewsModel.find_by_status(status)
        if result:
            return result, 200
        return {status: "news with {} status was not found".format(status)}, 404    
            
        
