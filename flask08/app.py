from flask import Flask, session, redirect, url_for, request

app = Flask(__name__)

# Set a secret key for your application to use sessions
app.secret_key = 'Ashu'

# This route sets a session variable 'username'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Assuming the form has an input field with name 'username'
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

# This route retrieves the 'username' from the session


@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as ' + session['username'] + '<br>' + \
               "<b><a href = '/logout'>click here to log out</a></b>"
    return "You are not logged in <br><a href = '/login'></b>" + \
           "click here to log in</b></a>"

# This route removes the 'username' from the session


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
