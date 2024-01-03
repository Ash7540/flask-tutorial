from flask import Flask, request

app = Flask(__name__)


@app.route('/query-string_example')
def query_example():
    # returns None if no key is entered
    language = request.args.get('language')
    # returns empty string if key does not exist
    framework = request.args.get('framework', '')
    # returns None if key in not entered
    description = request.args.get('description')
    website = request.args.get('website')  # returns None if key in not entered

    return '''
              <p>The language value is: {}</p>
              <p>The framework value is: {}</p>
              <p>Description: {}</p>
              <p>The website value is: {}</p>'''.format(language, framework, description, website)


if __name__ == '__main__':
    app.run(debug=True)
