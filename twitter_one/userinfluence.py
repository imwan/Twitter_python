import sys
import json

def userReach(screen_name):
    followers_file = 'users/{}/followers.jsonl'.format(screen_name)
    with open(followers_file) as f:
        reach = []
        for line in f:
            profile = json.loads(line)
            reach.append((profile['screen_name'], profile['followers_count']))

    profile_file = 'users/{}/user_profile.json'.format(screen_name)
    with open(profile_file) as f:
        profile = json.load(f)
        followers = profile['followers_count']
        tweets = profile['statuses_count']

    timeline_file= 'user_timeline_{}.jsonl'.format(screen_name)
    with open(timeline_file) as f:
        favorite_count, retweet_count = [], []
        for line in f:
            tweet = json.loads(line)
            favorite_count.append(tweet['favorite_count'])
            retweet_count.append(tweet['retweet_count'])
    return (followers,tweets,favorite_count,retweet_count,reach)


def influenceStat(screen_name, followers,tweets,favorite_count,retweet_count,reach):
    sum_reach = sum([x[1] for x in reach])
    avg_followers = round(sum_reach / followers, 2)
    avg_favorite = round(sum(favorite_count) / tweets, 2)
    avg_retweet = round(sum(retweet_count) / tweets, 2)
    favorite_per_user = round(sum(favorite_count) / followers, 2)
    retweet_per_user = round(sum(retweet_count) / followers, 2)

    print("----- Stats {} -----".format(screen_name))
    print("{} followers".format(followers))
    print("{} users reached by 1-degree connections".format(sum_reach))
    print("Average number of followers for {}'s followers: {}".format(screen_name, avg_followers))
    print("Favorited {} times ({} per tweet, {} per user)".format(sum(favorite_count), avg_favorite,
                                                                  favorite_per_user))
    print("Retweeted {} times ({} per tweet, {} per user)".format(sum(retweet_count), avg_retweet, retweet_per_user))

