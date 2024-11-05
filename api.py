from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {"message": "Hello, World!"}, 200

api.add_resource(HelloWorld, '/')

class Add(Resource):
    def get(self):
        num1 = request.args.get('num1', type=int)
        num2 = request.args.get('num2', type=int)
        
        if num1 is None or num2 is None:
            return {"message": "Hem num1 hem de num2 tam sayı olarak gereklidir."}, 400

        result = num1 + num2
        return {"result": result}, 200

api.add_resource(Add, '/add')


if __name__ == '__main__':
    app.run(debug=True)
