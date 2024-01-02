from flask import *

app = Flask(__name__)


@app.route('/BE')
def be():
    return '<h1>BE<h1>'


@app.route('/MTECH')
def mtech():
    return '<h1>M-Tech<h1>'


@app.route('/study/<name>')
def user(name):
    if name == 'BE':
        return redirect(url_for('be'))
    if name == 'MTECH':
        return redirect(url_for('mtech'))

if __name__ == '__main__':
    app.run(debug=True)
