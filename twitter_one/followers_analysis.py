import sys
import json
from random import sample
import time
import numpy as np

def followers_count(screen_name):
    followers_file ="users/"+screen_name+"/followers.jsonl"
    friends_file = "users/"+screen_name +"/friends.jsonl"
    with open(followers_file) as f1, open(friends_file) as f2:
        t0 = time.time()
        followers = []
        friends = []
        for line in f1:
            profile = json.loads(line)
            followers.append(profile['screen_name'])
        for line in f2:
            profile = json.loads(line)
            friends.append(profile['screen_name'])
        t1 = time.time()
        mutual_friends = [user for user in friends if user in followers]
        followers_not_following = [user for user in followers if user not in friends]
        friends_not_following = [user for user in friends if user not in followers]
        t2 = time.time()
        print("----- Timing -----")
        print("Initialize data: {}".format(t1 - t0))
        print("Set-based operations: {}".format(t2 - t1))
        print("Total time: {}".format(t2 - t0))

        print("{} has {} followers".format(screen_name, len(followers)))
        print("{} has {} friends".format(screen_name, len(friends)))
        print("{} has {} mutual friends".format(screen_name, len(mutual_friends)))
        print("{} friends are not following {} back".format(len(friends_not_following), screen_name))
        print("{} followers are not followed back by {}".format(len(followers_not_following), screen_name))
    return (followers, friends, mutual_friends,followers_not_following,friends_not_following)


def followers_count2(screen_name):
    followers_file = "users/" + screen_name + "/followers.jsonl"
    friends_file = "users/" + screen_name + "/friends.jsonl"
    with open(followers_file) as f1, open(friends_file) as f2:
        t0 = time.time()
        followers = []
        friends = []
        for line in f1:
            profile = json.loads(line)
            followers.append(profile['screen_name'])
        for line in f2:
            profile = json.loads(line)
            friends.append(profile['screen_name'])
        followers = np.array(followers)
        friends = np.array(friends)
        t1 = time.time()
        mutual_friends = np.intersect1d(friends, followers, assume_unique=True)
        followers_not_following = np.setdiff1d(followers, friends, assume_unique=True)
        friends_not_following = np.setdiff1d(friends, followers, assume_unique=True)
        t2 = time.time()
        print("----- Timing -----")
        print("Initialize data: {}".format(t1 - t0))
        print("Set-based operations: {}".format(t2 - t1))
        print("Total time: {}".format(t2 - t0))
        print("----- Stats -----")
        print("{} has {} followers".format(screen_name, len(followers)))
        print("{} has {} friends".format(screen_name, len(friends)))
        print("{} has {} mutual friends".format(screen_name, len(mutual_friends)))
        print("{} friends are not following {} back".format(len(friends_not_following), screen_name))
        print("{} followers are not followed back by {}".format(len(followers_not_following), screen_name))

    return (followers, friends, mutual_friends, followers_not_following, friends_not_following)