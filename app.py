from flask import Flask, request, redirect, abort
from flask.helpers import url_for
from flask.templating import render_template
from models import db, User, Interest
from functions import *

app = Flask(__name__)
#app.config.from_json('config.json')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite+pysqlite:///database.db'


db.init_app(app)
db.create_all(app=app)

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/items')
def items():
    return render_template('items.html', users=User.query.all())

@app.post('/submit_item')
def post():
    user_name = request.form.get('user_name')
    user_age = request.form.get('user_age')
    user_interests = request.form.getlist('user_interests')
    user_interests = [Interest(name=interest) for interest in user_interests]
    user = User(name=user_name, age=user_age, interests=user_interests)
    db.session.add(user)
    db.session.commit()
    return render_template('submit_item.html')

if __name__ == '__main__':
    app.run()