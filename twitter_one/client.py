import os
import sys
from tweepy import API
from tweepy import OAuthHandler
def get_twitter_auth(code):
    auth=OAuthHandler(code[2],code[3])
    auth.set_access_token(code[0],code[1])
    return auth
def get_twitter_client(client):
    auth=get_twitter_auth(client)
    client=API(auth)
    return client
