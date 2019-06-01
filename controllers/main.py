from flask import (
    Blueprint, render_template
)
import numpy as np
import twitter
from dotenv import load_dotenv
import os
load_dotenv()

bp = Blueprint('main', __name__)

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


@bp.route('/')
def home():
    return render_template('home.html', tweets=combined_tweets)

if __name__ == '__main__':
    bp.run(debug=True)