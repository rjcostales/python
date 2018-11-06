#!/usr/bin/env python

import tweepy

from keys0 import ACCOUNT, API_KEY, API_SECRET, TOKEN_KEY, TOKEN_SECRET


def print_user(user):
    print("%-20i%-20s%-20s" % (user.id, user.screen_name, user.name))


def list_friends():
    ids = []
    friends = tweepy.Cursor(api.friends).items()
    for friend in friends:
        print_user(friend)
        ids.append(friend.id)
    return ids


auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(TOKEN_KEY, TOKEN_SECRET)
api = tweepy.API(auth)

print(ACCOUNT)
list_friends()
