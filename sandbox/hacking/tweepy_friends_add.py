#!/usr/bin/env python

import tweepy

from keys0 import API_KEY, API_SECRET, TOKEN_KEY, TOKEN_SECRET

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(TOKEN_KEY, TOKEN_SECRET)
api = tweepy.API(auth)

f = open('friends0.txt')
for l in f:
    id, junk = l.strip().split(' ', maxsplit=1)
    print(id)
    api.create_friendship(id=id)
