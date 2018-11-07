#!/usr/bin/env python

import tweepy

from keys2 import ACCOUNT, API_KEY, API_SECRET, TOKEN_KEY, TOKEN_SECRET
from tweepy_func import print_tweet, print_user

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(TOKEN_KEY, TOKEN_SECRET)
api = tweepy.API(auth)


def list_followers():
    followers = []
    for user in api.followers():
        print_user(user)
        followers.append(user.id)
    return followers


print(ACCOUNT)

for tweet in api.retweets_of_me():
    print_tweet(tweet)

print()
print('Followers')
list_followers()
