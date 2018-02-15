from pymongo import MongoClient

class NewsModel:

    def __init__(self, status, topic, title):
        self.status = status
        self.topic = topic
        self.title = title

    
