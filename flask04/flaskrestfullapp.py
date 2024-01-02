from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)

api = Api(app)


class JSONResponse(Resource):
    def get(self):
        name = {
            "fname": "Ashwin",
            "lname": "Chavan",
        }
        return name


api.add_resource(JSONResponse, '/jsonresponse')

if __name__ == '__main__':
    app.run(debug=True)
