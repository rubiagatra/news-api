from flask import Flask
from flask_restful import Api
from newsapi.home import Home 
from flask_jwt import JWT
from newsapi.security import authenticate, identity
from newsapi.db import create_user

def create_app():
    
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.settings')
    app.config.from_pyfile('settings.py', silent=True)

    JWT(app, authenticate, identity)

    api = Api(app)
    api.add_resource(Home, '/') 

    return app