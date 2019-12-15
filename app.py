from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = "abcd1234"
api = Api(app)

jwt = JWT(app=app, authentication_handler=authenticate, identity_handler=identity)

class Movie(Resource):
    @jwt_required
    def get(self, name):
        return {'movie': name}


api.add_resource(Movie, '/movie/<name>')

app.run(port=5000, debug=True)




