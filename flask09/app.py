from flask import * 

# Initializing the Flask application
app = Flask(__name__)
@app.route('/') 
def home (): 
   return render_template("index.html") 
@app.route('/login') 
def login(): 
   return render_template("login.html"); 
@app.route('/validate', methods = ['POST']) 
def validate(): 
   if request.method == 'POST' and request.form['pass'] == 'ninja': 
       return redirect(url_for("success")) 
   return redirect(url_for("login")) 
@app.route('/success') 
def success(): 
   return "You have logged in successfully!" 

if __name__ == '__main__': 
   app.run(debug = True)