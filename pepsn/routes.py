import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from pepsn import app, db, bcrypt
from pepsn.forms import RegistrationForm, LoginForm, UpdateAccountForm, PicksForToday
from pepsn.models import User, Post, Comments, Bets, Picks
from flask_login import login_user, current_user, logout_user, login_required
from datetime import date, timezone, timedelta
import datetime
import json
from pytz import timezone
import pytz


# #Load in schedule
with open('/Users/prabhdeepsingh/Personal/PEPSNPY/pepsn/schedule.json') as json_file:
    schedule = json.load(json_file)
local_tz = pytz.timezone('US/Central')
# dates =[]
# for idx,item in enumerate(schedule["games"]):
#     time = datetime.datetime.strptime(item["schedule"],'%Y-%m-%dT%H:%M:%S')
#     gameTimes = local_tz.normalize(time.replace(tzinfo=pytz.utc).astimezone(local_tz)).strftime("%x %I:%M:%S %p")
#     dates.append((idx, gameTimes))
    
# print(dates)

#get game times in human readable format in cst
local_tz = pytz.timezone('US/Central')
#Todays Time and Date formated year time(12hour pm/am)
today = datetime.datetime.now()
todayFormated = today.strftime("%x %I:%M:%S %p")
todaysDate = today.strftime("%x")

# # for games in schedule["games"]:
# #     time = datetime.datetime.strptime(games["schedule"],'%Y-%m-%dT%H:%M:%S')
# #     gameTimes = local_tz.normalize(time.replace(tzinfo=pytz.utc).astimezone(local_tz)).strftime("%x %I:%M:%S %p")

oneHourBeforeFirstGame = ''   
def getTodaysGames(today):
    todaysGames = {"games": []}
    for games in schedule["games"]:
        time = datetime.datetime.strptime(games["schedule"],'%Y-%m-%dT%H:%M:%S')
        gameTimesForCompare = local_tz.normalize(time.replace(tzinfo=pytz.utc).astimezone(local_tz)).date()
        if (gameTimesForCompare == today.date()):
            todaysGames["games"].append(games)
    firstGameOfTheDay = datetime.datetime.strptime(todaysGames["games"][0]["schedule"],'%Y-%m-%dT%H:%M:%S')
    firstGameOfTheDayFormatted = local_tz.normalize(firstGameOfTheDay.replace(tzinfo=pytz.utc).astimezone(local_tz))
    oneHourBeforeFirstGame = firstGameOfTheDayFormatted - timedelta(hours=0, minutes=10)
    todaysGames["pickCutOffTime"] = oneHourBeforeFirstGame.strftime("%I:%M %p")
        
    return todaysGames
# # import http.client

# # conn = http.client.HTTPSConnection("api.sportradar.us")

# # conn.request("GET", "/nba/trial/v5/en/games/2019/REG/schedule.json?api_key=3tqauj3fcs5bn5sn2ajaafth")

# # res = conn.getresponse()
# # data = res.read()

# # print(data.decode("utf-8"))




# # # Need to move this stuff to another file#################################
# from sportsreference.nba.boxscore import Boxscores
import twitter
import numpy as np
# # # env file
from dotenv import load_dotenv
load_dotenv()

# # nba box score for yesterday
# games = Boxscores(datetime(2020, 1, 14))
# # print(games)
# # print(games.games)
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

gamesForToday = getTodaysGames(today)

@app.route("/picks", methods=['GET', 'POST'])
def picks():
    form = PicksForToday()
    todaysPicks = ""
    userPicks = Picks.query.filter_by(user_id=current_user.id, data_posted=todaysDate)
    if (request.method == "POST"):
        if current_user.is_authenticated:
            # save picks into a dict
            data = request.form.to_dict(flat=False)
            pointsBy = data['pointsBy']
            teams = []
            # delete uncessary data
            del data['csrf_token']
            del data['submit']
            del data['pointsBy']

            for key in data:
                teams.append(key)
            # create a list of tuples (team, pointWinBy)
            dataToSaveInDatabase = list(zip(teams, pointsBy))

            todaysCutOffTime = todaysDate + " " + gamesForToday["pickCutOffTime"]
            # if now is 10 mins before first game
            if (datetime.datetime.strptime(todaysCutOffTime,'%m/%d/%y %H:%M %p') > today):
                # if picks havent been made for today
                if not bool(current_user.picks):
                    print("No picks")
                    picks = Picks(user_id=current_user.id, content=str(dataToSaveInDatabase).strip('[]'), data_posted=todaysDate)
                    db.session.add(picks)
                    db.session.commit()
                else:
                    print("Picks have been made but we want to overwrite")
                    print("The current Picks: ")
                    print(dataToSaveInDatabase)
                    Picks.query.filter_by(user_id=current_user.id, data_posted=todaysDate).delete()
                    picks = Picks(user_id=current_user.id, content=str(dataToSaveInDatabase).strip('[]'), data_posted=todaysDate)
                    db.session.add(picks)
                    db.session.commit()
            else:
                flash(f'You have missed the deadline to make picks for today. Picks cut off 10 mins before first game.', 'danger')
            todaysPicks = current_user.picks
        else:
            flash(f'Please Login to Submit Picks', 'danger')
    else:
        if current_user.is_authenticated:
            todaysPicks = userPicks.all()
    if bool(userPicks.all()):
        flash(f'You already have made picks for today, Submitting new pick will override the original.', 'info')
    return render_template('picks.html', title='Picks', gamess=gamesForToday, date=todaysDate, form=form, userLoggedIn=current_user.is_authenticated, todaysPicks=todaysPicks)

@app.route("/standings")
def standings():
    users = User.query.all()
    # print(users)
    return render_template('standings.html', title='Standings', users=users)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/discussion")
def discussion():
    return render_template('discussion.html', title='Discussion', posts=posts)