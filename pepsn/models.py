from pepsn import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    bets = db.relationship('Bets', backref='better', lazy=True)
    picks = db.relationship('Picks', backref='picker', lazy=True)
    comments = db.relationship('Comments', backref='commenter', lazy=True)
    # What is printed
    def __repr__(self): 
        return f"User('{self.username}, {self.email}, {self.image}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    data_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    comments = db.relationship('Comments', backref='comments', lazy=True)
    # What is printed
    def __repr__(self): 
        return f"Post('{self.user_id}, {self.title}, {self.data_posted}, {self.content}, {self.comments}')"

class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    data_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    # What is printed
    def __repr__(self): 
        return f"Comments('{self.user_id}, {self.post_id}, {self.content}, {self.data_posted}')"

class Bets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    winner = db.Column(db.String, default="null")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user_against_id = db.Column(db.Integer, nullable=False)
    content = db.Column(db.Text, nullable=False)
    # What is printed
    def __repr__(self): 
        return f"Comments('{self.user_id}, {self.data_posted}, {self.winner}, {self.user_id}, {self.user_against_id}, {self.content}')"

class Picks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    data_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text)
    # What is printed
    def __repr__(self): 
        return f"User('{self.user_id}, {self.data_posted}, {self.content}')"