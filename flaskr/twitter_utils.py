import tweepy
from credentials import api_key, secret_api_key, access_token, secret_access_token
import geocoder
import time

auth = tweepy.OAuthHandler(api_key, secret_api_key)
auth.set_access_token(access_token, secret_access_token)
api = tweepy.API(auth)


def user_exists(user_name):
    try:
        user = api.get_user(screen_name=user_name)
        return True
    except tweepy.TweepError:
        return False

def get_friends(user_name):
    ids = []
    for user_id in tweepy.Cursor(api.friends_ids, screen_name=user_name).items():
        ids.append(user_id)
    try:
        screen_names = [user.screen_name for user in api.lookup_users(user_ids=ids)]
        locations = [user.location for user in api.lookup_users(user_ids=ids)]
        users = list(zip(screen_names, locations))
        return users
    except tweepy.TweepError:
        return None



def get_coordinates(location):
    coordinates = geocoder.arcgis(location)
    return coordinates.latlng



