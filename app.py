from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Movie(Resource):
    def get(self, name):
        return {'movie': name}


api.add_resource(Movie, '/movie/<string:name>')

app.run(port=5000)




