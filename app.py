from flask import Flask, request, redirect, abort
from flask.helpers import url_for
from flask.templating import render_template

from models import db, Item

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
    return render_template('items.html', items=Item.query.all())

@app.post('/submit_item')
def post():
    item_name = request.form.get('item')
    item = Item(name=item_name)
    db.session.add(item)
    db.session.commit()
    return render_template('submit_item.html')

if __name__ == '__main__':
    app.run()