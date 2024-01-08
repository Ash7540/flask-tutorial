from flask import Flask, render_template_string
from flask_sijax import Sijax


app = Flask(__name__)
app.config['SIJAX_STATIC_PATH'] = '/static/sijax/'
app.config['SIJAX_JSON_URI'] = '/static/sijax/json2.js'

Sijax(app)


@app.route('/')
def index():
    page_content = '''
    <html>
    <head>
        <script type="text/javascript" src="{{ url_for('static', filename='sijax/sijax.js') }}"></script>
    </head>
    <body>
        <input type="text" id="input_text">
        <button onclick="sijax_request('process_data', ['input_text']);">Submit</button>
        <p id="result"></p>
    </body>
    </html>
    '''

    return render_template_string(page_content)


# Sijax function to process data
def process_data(obj_response, text):
    result = f'You entered: {text}'
    obj_response.html('#result', result)


# Register Sijax callbacks
@Sijax.route(app, '/process_data')
def sijax_process_data(obj_response, text):
    process_data(obj_response, text)


if __name__ == '__main__':
    app.run(debug=True)
