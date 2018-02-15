from flask import Flask
from flask_restful import Api
from newsapi.home import Home 
from flask_jwt import JWT
from newsapi.security import authenticate, identity
from newsapi.db import create_user
from newsapi.news.view import News, NewsItem, NewsStatus, NewsTopic


def create_app():
    
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    jwt = JWT(app, authenticate, identity)

    @app.before_first_request
    def initiate_mongodb():
        create_user()


    api = Api(app)
    api.add_resource(Home, '/') 
    api.add_resource(News, '/api/news')
    api.add_resource(NewsItem, '/api/news/<int:_id>' )
    api.add_resource(NewsTopic, '/api/news/topic/<string:topic>' )
    api.add_resource(NewsStatus, '/api/news/status/<string:status>' )


    return app