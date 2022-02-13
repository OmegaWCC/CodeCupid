from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    name = db.Column(db.Text, unique=False, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    interests = db.relationship('Interest', backref='user', lazy=True)
    def __repr__(self):
        return f'<User {self.name}>'

class Interest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return f'<Interest {self.name}>'
