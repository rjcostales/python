#!/usr/bin/env python

import sys

import tweepy

from keys import API_KEY, API_SECRET, TOKEN_KEY, TOKEN_SECRET


def print_tweet(tweet):
    print("%s\t%s\t%s" %
          (tweet.created_at,
           tweet.user.name.ljust(20),
           tweet.text.replace('&amp;', '$')
           .replace('\n', ' ')
           .replace('\a', ' ')
           .replace('\t', ' ')
           .replace(' *', ' ')))


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

argv = sys.argv
user = 'rjcostales'
user_timeline(user)
