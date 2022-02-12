from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
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
