from flask_restful import Resource


class Home(Resource):

    def get(self):
        return "Please visit our documentation kumparan.aifor.fun/docs"