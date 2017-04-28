import json
import os
import sys
import time
import math
from tweepy import Cursor
from twitter_one.client import *

def printProfile(client, screen_name="tigerwan2008"):
    profile = client.get_user(screen_name=screen_name)
    print(json.dumps(profile._json, indent=4))



MAX_FRIENDS = 15000



def paginate(items, n):
    """Generate n-sized chunks from items"""
    for i in range(0, len(items), n):
        yield items[i:i+n]

def followers(client,screen_name):
    dirname = "users/"+screen_name
    max_pages = math.ceil(MAX_FRIENDS / 5000)
    try:
        os.makedirs(dirname, mode=0o755, exist_ok=True)
    except OSError:
        print("Directory {} already exists".format(dirname))
    except Exception as e:
        print("Error while creating directory {}".format(dirname))
        print(e)
        sys.exit(1)


    fname = "users/"+screen_name+"/followers.jsonl"
    with open(fname, 'w') as f:
        for followers in Cursor(client.followers_ids, screen_name=screen_name).pages(max_pages):
            for chunk in paginate(followers, 100):
                users = client.lookup_users(user_ids=chunk)
                for user in users:
                    f.write(json.dumps(user._json)+"\n")
            if len(followers) == 5000:
                print("More results available. Sleeping for 60 seconds to avoid rate limit")
                time.sleep(60)

def friends(client,screen_name):
    # get friends for a given user
    max_pages = math.ceil(MAX_FRIENDS / 5000)
    dirname = "users/" + screen_name
    try:
        os.makedirs(dirname, mode=0o755, exist_ok=True)
    except OSError:
        print("Directory {} already exists".format(dirname))
    except Exception as e:
        print("Error while creating directory {}".format(dirname))
        print(e)
        sys.exit(1)
    fname = "users/"+screen_name+"/friends.jsonl"
    with open(fname, 'w') as f:
        for friends in Cursor(client.friends_ids, screen_name=screen_name).pages(max_pages):
            for chunk in paginate(friends, 100):
                users = client.lookup_users(user_ids=chunk)
                for user in users:
                    f.write(json.dumps(user._json)+"\n")
            if len(friends) == 5000:
                print("More results available. Sleeping for 60 seconds to avoid rate limit")
                time.sleep(60)

def userProfile(client, screen_name):
    max_pages = math.ceil(MAX_FRIENDS / 5000)
    dirname = "users/" + screen_name
    try:
        os.makedirs(dirname, mode=0o755, exist_ok=True)
    except OSError:
        print("Directory {} already exists".format(dirname))
    except Exception as e:
        print("Error while creating directory {}".format(dirname))
        print(e)
        sys.exit(1)

    fname = "users/"+screen_name+"/user_profile.json".format(screen_name)
    with open(fname, 'w') as f:
        profile = client.get_user(screen_name=screen_name)
        f.write(json.dumps(profile._json, indent=4))

