from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World"

@app.route('/hello/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

@app.route('/hello/<int:age>')
def hello_age(age):
    return 'I am %d years old.' % age

if __name__ == '__main__':
    app.run(debug=True)