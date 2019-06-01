from flask import Flask, render_template, url_for, flash, redirect
form flask_sqlalchmey = SQLAlchemy
from forms import RegistrationForm, LoginForm
from datetime import datetime
# Has one day old scores and sports info. nfl, bball
from sportsreference.nba.boxscore import Boxscores
import twitter
import numpy as np
# env file
from dotenv import load_dotenv
import os
load_dotenv()

# nba box score for yesterday
games = Boxscores(datetime(2019, 4, 20))
# print(games)
# print(games.games)
api = twitter.Api(consumer_key=os.getenv("TWITTER_CONSUMER_KEY"),
                  consumer_secret=os.getenv("TWITTER_CONSUMER_SECRET"),
                  access_token_key=os.getenv("TWITTER_ACCESS_TOKEN_KEY"),
                  access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_SECRET"))

# twitter calls
ShamsCharania = api.GetUserTimeline(screen_name="ShamsCharania", count=5)
wojespn = api.GetUserTimeline(screen_name="wojespn", count=5)
nba = api.GetUserTimeline(screen_name="NBA", count=5)
combined_tweets = ShamsCharania + wojespn + nba
# shuffle tweets
np.random.shuffle(combined_tweets)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHMEY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=true)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=Flase)
    posts = db.relationship('Post', backref='author', lazy=True)
    # What is printed
    def __repr__(self): 
        return f"User('{self.username}, {self.email}, {self.image}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=true)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    data_posted = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow())
    content = db.Column(db.Text, nullable=False)
    comments = db.relationship('Comments', backref='commenter', lazy=True)
    # What is printed
    def __repr__(self): 
        return f"Post('{self.title}, {self.data_posted}, {self.content}')"

class Comments(db.Comments):
    id = db.Column(db.Integer, primary_key=true)
    post_id = db.Column(db.Integer, ForeignKey('post.id'), nullable=False)
    data_posted = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow())
    content = db.Column(db.Text, nullable=False)
    # What is printed
    def __repr__(self): 
        return f"Comments('{self.content}, {self.data_posted}')"


posts = [
    {
    'author': 'X-factor', 
    'title': "How Westbrook's triple doubles are not meaningful.",
    'content': "Coming soon...",
    'date': "04/20/2019"
    },
    {
    'author': 'Jassi A. Smith', 
    'title': "THIS MAN IS A BONAFIDE SCRUB!",
    'content': "Coming soon...",
    'date': "04/22/2019"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', tweets=combined_tweets)

@app.route("/scores")
def scores():
    return render_template('scores.html', scores=games.games['4-20-2019'])


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'test@test.com' and form.password.data == 'test':
            flash(f'You have logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful, Please check Email and Password.', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/picks")
def picks():
    return render_template('picks.html', title='Picks')

@app.route("/standings")
def standings():
    return render_template('standings.html', title='Standings')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/discussion")
def discussion():
    return render_template('discussion.html', title='Discussion', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
