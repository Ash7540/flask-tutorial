from flask import Flask, render_template
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)

app.secret_key = 'CODINGNINJAS'

app.config['SERVER_NAME'] = 'localhost:5000'

# Initializing OAuth with the following command
oauth = OAuth(app)


@app.route('/')
def index():
    return render_template('welcome.html')


if __name__ == "__main__":
    app.run(debug=True)


# Setting up OAuth in Flask for Instagram

# from flask import Flask, render_template, url_for, redirect
# from authlib.integrations.flask_client import OAuth
# import os
 
# app = Flask(__name__)
# app.secret_key = 'ASHU'
 
# '''
#     Set SERVER_NAME to localhost as an Instagram callback
#     URL does not accept 127.0.0.1
#     Tip: Set the callback origin(site) for Facebook and Instagram to http://domain.com (or your domain name) because this service does not support 127.0.0.1 or localhost.
# '''
 
# app.config['SERVER_NAME'] = 'localhost:5000'
 
# oauth = OAuth(app)
 
# @app.route('/')
# def index():
#     return render_template('welcome.html')
   
# @app.route('/instagram/')
# def instagram():
   
#     # Instagram Oauth Config
#     INSTAGRAM_CLIENT_ID = os.environ.get('INSTAGRAM_CLIENT_ID')
#     INSTAGRAM_CLIENT_SECRET = os.environ.get('INSTAGRAM_CLIENT_SECRET')
#     oauth.register(
#         name='instagram',
#         client_id=INSTAGRAM_CLIENT_ID,
#  request_token_url='https://api.instagram.com/oauth/request_token',
#         request_token_params=None,
#         access_token_url='https://api.instagram.com/oauth/access_token',
#         access_token_params=None,
#         authorize_url='https://api.instagram.com/oauth/authenticate',
#         authorize_params=None,
#         api_base_url='https://api.instagram.com/1.1/',
#         client_kwargs=None,
#     )
#     redirect_uri = url_for('instagram_auth', _external=True)
#     return oauth.instagram.authorize_redirect(redirect_uri)
 
# @app.route('/instagram/auth/')
# def instagram_auth():
#     token = oauth.instagram.authorize_access_token()
#     resp = oauth.instagram.get('account/verify_credentials.json')
#     profile = resp.json()
#     print(" instagram User", profile)
#     return redirect('/')
 
# if __name__ == "__main__":
#     app.run(debug=True)
    
# Setting up OAuth in Flask for Facebook
# Facebook Oauth Configuration
#     FACEBOOK_CLIENT_ID = os.environ.get('FACEBOOK_CLIENT_ID')
#     FACEBOOK_CLIENT_SECRET = os.environ.get('FACEBOOK_CLIENT_SECRET')
#     oauth.register(
#         name='facebook',
#         client_id=FACEBOOK_CLIENT_ID,
#         client_secret=FACEBOOK_CLIENT_SECRET,
#         access_token_url='https://graph.facebook.com/oauth/access_token',
#         access_token_params=None,
#         authorize_url='https://www.facebook.com/dialog/oauth',
#         authorize_params=None,
#         api_base_url='https://graph.facebook.com/',
#         client_kwargs={'scope': 'email'},WSGI
#     )
#     redirect_uri = url_for('facebook_auth', _external=True)
#     return oauth.facebook.authorize_redirect(redirect_uri)
#     @app.route('/facebook/auth/')
# def facebook_auth():
#     token = oauth.facebook.authorize_access_token()
#     resp = oauth.facebook.get(
#         'https://graph.facebook.com/me?fields=id,name,email,picture{url}')
#     profile = resp.json()
#     print("Facebook User ", profile)
#     return redirect('/')
 
# if __name__ == "__main__":
#     app.run(debug=True)
    

# Setting up OAuth in Flask for Google
# from flask import Flask, render_template, url_for, redirect
# from authlib.integrations.flask_client import OAuth
# import os
 
# app = Flask(__name__)
# app.secret_key = 'CODINGNINJAS'
 
# '''
#     Set SERVER_NAME to localhost as twitter callback
#     URL does not accept 127.0.0.1
#     Tip: set callback origin(site) for Facebook and Instagram
#     as http://domain.com (or use your domain name) as this provider
#     don't accept 127.0.0.1 / localhost
# '''
 
# app.config['SERVER_NAME'] = 'localhost:5000'
# oauth = OAuth(app)
 
# @app.route('/')
# def index():
#     return render_template('welcome.html')
 
# @app.route('/google/')
# def google():GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
#     GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET')
     
#     CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
#     oauth.register(
#         name='google',
#         client_id=GOOGLE_CLIENT_ID,
#         client_secret=GOOGLE_CLIENT_SECRET,
#         server_metadata_url=CONF_URL,
#         client_kwargs={
#             'scope': 'openid email profile'
#         }
#     )
     
#     # Redirect to google_auth function
#     redirect_uri = url_for('google_auth', _external=True)
#     return oauth.google.authorize_redirect(redirect_uri)
 
# @app.route('/google/auth/')
# def google_auth():
#     token = oauth.google.authorize_access_token()
#     user = oauth.google.parse_id_token(token)
#     print(" Google User ", user)
#     return redirect('/')
 
# if __name__ == "__main__":
#     app.run(debug=True)