from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/jsonresponse', methods=['GET'])
def JSONResponse():
    if (request.method == 'GET'):
        name = {
            "fname": "Ashwin",
            "lname": "Chavan",
        }
    return jsonify(name)


if __name__=='__main__':
    app.run(debug=True)