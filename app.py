from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from model.security import authenticate, identity
from resource.books import Book

app = Flask(__name__)
app.secret_key = "abcd1234"
api = Api(app)

jwt = JWT(app=app, authentication_handler=authenticate, identity_handler=identity)

api.add_resource(Book, '/book/<string:isbn>')

app.run(port=5000, debug=True)




