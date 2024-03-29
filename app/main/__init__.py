from flask import Blueprint
from flask_oauthlib.client import OAuth
import os

main = Blueprint('', __name__)
oauth = OAuth()

twitter = oauth.remote_app

twitter = oauth.remote_app('twitter',
    base_url='https://api.twitter.com/1.1/',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authenticate',
    consumer_key=os.getenv("CONSUMER"),
    consumer_secret=os.getenv("SECRET")
)


from . import views
