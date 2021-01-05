from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {"ayushi": {"age":27, "gender" : "female"},
        "ayon":{"age": 20, "gender" : "male"}}

#override Resource class with some methods
class HelloWorld(Resource):
        def get(self,name):
                return names[name]

api.add_resource(HelloWorld,"/helloworld/<string:name>")



if __name__ == "__main__":
        app.run(debug=True)
