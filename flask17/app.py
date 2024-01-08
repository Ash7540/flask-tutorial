from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']  
collection = db['mycollection']


@app.route('/')
def index():
    return 'Welcome to my Flask-PyMongo App!'


# Route to add data to MongoDB
@app.route('/add', methods=['POST'])
def add_data():
    data = request.json
    collection.insert_one(data)
    return jsonify({'message': 'Data added successfully!'})


# Route to get all data from MongoDB
@app.route('/data', methods=['GET'])
def get_data():
    data = list(collection.find())
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
