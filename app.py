from flask import Flask, render_template, redirect, url_for, request, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = "hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.permanent_session_lifetime = timedelta(days=5)


db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))


    def __init__(self, name, email):
        self.name = name
        self.email = email

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/anime')
def anime():
    return render_template('anime.html')

@app.route('/animals')
def animals():
    return render_template('animals.html')

@app.route('/flowers')
def flowers():
    return render_template('flowers.html')

@app.route('/login/<name>')
def user(name):
    flash(f"Welcome {name}")
    return render_template('user.html')


@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['name']
      return redirect(url_for('user', name=user))
   else:
      user = request.args.get('name')
      return render_template('login.html')



if __name__ == "__main__":
    app.run(debug=True)



