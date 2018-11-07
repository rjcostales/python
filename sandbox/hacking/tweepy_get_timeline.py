#!/usr/bin/env python

import tweepy

from keys0 import API_KEY, API_SECRET, TOKEN_KEY, TOKEN_SECRET
from tweepy_func import print_tweet


def user_timeline(user):
    count = 0
    for tweet in api.user_timeline(user, count=100):
        if not tweet.text.startswith("RT"):
            print_tweet(tweet)
            count += 1
            if count > 50:
                return


auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(TOKEN_KEY, TOKEN_SECRET)
api = tweepy.API(auth)

user_timeline('rjcostales')

user_timeline('rjsc1024')

user_timeline('CodingAZ')
