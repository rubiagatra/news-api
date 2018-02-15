from flask import Flask
from flask_restful import Api
from newsapi.home import Home 
from flask_jwt import JWT
from newsapi.security import authenticate, identity
from newsapi.db import create_user
from newsapi.news.views import News, NewsItem, NewsStatus, NewsTopic
from newsapi.database import mongo
from newsapi.user import UserModel


def create_app():
    
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    mongo.init_app(app)

    jwt = JWT(app, authenticate, identity)

    @app.before_first_request
    def initiate_mongodb():
        if UserModel.find_by_username('sandbox'):
            return None 
        mongo.db.user.insert_one({'_id': 1, "username": "sandbox", "password": "sandbox"})

    api = Api(app)
    api.add_resource(Home, '/') 
    api.add_resource(News, '/api/news')
    api.add_resource(NewsItem, '/api/news/<int:id>' )
    api.add_resource(NewsTopic, '/api/news/topic/<string:topic>' )
    api.add_resource(NewsStatus, '/api/news/status/<string:status>' )


    return app