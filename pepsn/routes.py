from flask import render_template, url_for, flash, redirect
from pepsn import app
from pepsn.forms import RegistrationForm, LoginForm
from pepsn.models import User, Post, Comments, Bets, Picks
from datetime import datetime

# Need to move this stuff to another file#################################
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
# Need to move this stuff to another file#################################


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