import json
from tweepy import Cursor



def printHomeLine(client,item_number):
    for status in Cursor(client.home_timeline).items(item_number):
        print(status.text)


def userTimeLine(client,screen_name):
    fname = "user_timeline_{}.jsonl".format(screen_name)
    with open(fname, 'w') as f:
        for page in Cursor(client.user_timeline, screen_name=screen_name, count=200).pages(16):
            for status in page:
                f.write(json.dumps(status._json) + "\n")