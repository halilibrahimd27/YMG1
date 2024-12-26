from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {"message": "Hello, World!"}, 200

class Add(Resource):
    def get(self):
        num1 = request.args.get('num1', type=int)
        num2 = request.args.get('num2', type=int)

        if num1 is None or num2 is None:
            return {"message": "Hem num1 hem de num2 tam sayı olarak gereklidir."}, 400

        result = num1 + num2
        return {"result": result}, 200

class Multiply(Resource):
    def post(self):
        data = request.get_json()
        try:
            num1 = int(data.get("num1"))
            num2 = int(data.get("num2"))
        except (TypeError, ValueError):
            return {"message": "Hem num1 hem de num2 tam sayı olmalıdır."}, 400

        result = num1 * num2
        return {"result": result}, 200

api.add_resource(HelloWorld, '/')
api.add_resource(Add, '/add')
api.add_resource(Multiply, '/multiply')

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=2700)
