from flask import Flask, flash, request, redirect, abort
from flask.helpers import url_for
from flask.templating import render_template
from importlib_metadata import re
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Interest
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from functions import *

app = Flask(__name__)
#app.config.from_json('config.json')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite+pysqlite:///database.db'
app.config['SECRET_KEY'] = "INTENTIONALLY INSECURE"

db.init_app(app)
db.create_all(app=app)
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@app.get('/items')
def items():
    def key(x):
        return matching_algo(current_user, x)
    users = User.query.filter(User.id != current_user.id).all()
    users.sort(key=key, reverse=True)
    return render_template('items.html', users=users)

@app.post('/signup')
def signup_post():
    user_email = request.form.get('user_email')
    user_password = request.form.get('user_password')
    user_name = request.form.get('user_name')
    user_age = request.form.get('user_age')
    user_interests = request.form.getlist('user_interests')
    user_bio = request.form.get('user_bio')
    

    user = User.query.filter_by(email=user_email).first()
    if user:
        return redirect(url_for('signup'))
    
    user_interests = [Interest(name=interest) for interest in user_interests]
    user = User(email=user_email, password=generate_password_hash(user_password, method='sha256'), name=user_name, age=user_age, interests=user_interests, bio=user_bio)
    db.session.add(user)
    db.session.commit()
    return render_template('create_account_success.html')


@app.get('/')
def signup():
    return render_template('create_account.html')

@app.get('/login')
def login():
    return render_template('login.html')

@app.post('/login')
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password, password):  
        login_user(user)
        return redirect(url_for('items'))
    else:
        return redirect(url_for('login'))

@app.get('/profile')
@login_required
def profile():
    print(current_user)
    return f"<h1>User: {current_user.name}</h1>"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


if __name__ == '__main__':
    app.run()