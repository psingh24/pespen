import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from pepsn import app, db, bcrypt
from pepsn.forms import RegistrationForm, LoginForm, UpdateAccountForm
from pepsn.models import User, Post, Comments, Bets, Picks
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime

# import http.client

# conn = http.client.HTTPSConnection("api.sportradar.us")

# conn.request("GET", "/nba/trial/v5/en/games/2019/REG/schedule.json?api_key=3tqauj3fcs5bn5sn2ajaafth")

# res = conn.getresponse()
# data = res.read()

# print(data.decode("utf-8"))




# # Need to move this stuff to another file#################################
from sportsreference.nba.boxscore import Boxscores
import twitter
import numpy as np
# # env file
from dotenv import load_dotenv
load_dotenv()

# nba box score for yesterday
games = Boxscores(datetime(2020, 1, 14))
# print(games)
# print(games.games)
api = twitter.Api(consumer_key=os.getenv("TWITTER_CONSUMER_KEY"),
                  consumer_secret=os.getenv("TWITTER_CONSUMER_SECRET"),
                  access_token_key=os.getenv("TWITTER_ACCESS_TOKEN_KEY"),
                  access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_SECRET"))
# # twitter calls
ShamsCharania = api.GetUserTimeline(screen_name="ShamsCharania", count=5)
wojespn = api.GetUserTimeline(screen_name="wojespn", count=5)
nba = api.GetUserTimeline(screen_name="NBA", count=5)
combined_tweets = ShamsCharania + wojespn + nba
# # shuffle tweets
np.random.shuffle(combined_tweets)
# # Need to move this stuff to another file#################################


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
    return render_template('scores.html', scores=games.games['1-14-2020'])


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful, Please check Email and Password.', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
   logout_user()
   return redirect(url_for('home'))

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    # throwing away first variable thus using _
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/images/profile_pics', picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Your account has been updated!", 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='images/profile_pics/' + current_user.image )
    return render_template('account.html', title='Account', image_file=image_file, form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pass)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}! You can now log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


date = "01-10-2019"
gamess = [{"Home": "LAL", "Away": "BOS", "GameNumber": 1}, {"Home": "TOR", "Away": "SAS", "GameNumber": 2}, {"Home": "DAL", "Away": "POR", "GameNumber": 3}, {"Home": "ATL", "Away": "NYK", "GameNumber": 4}]

@app.route("/picks")
def picks():
    return render_template('picks.html', title='Picks', gamess=gamess, date=date)

@app.route("/standings")
def standings():
    users = User.query.all()
    print(users)
    return render_template('standings.html', title='Standings', users=users)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/discussion")
def discussion():
    return render_template('discussion.html', title='Discussion', posts=posts)