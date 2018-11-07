#!/usr/bin/env python

import tweepy

from keys0 import API_KEY, API_SECRET, TOKEN_KEY, TOKEN_SECRET

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(TOKEN_KEY, TOKEN_SECRET)
api = tweepy.API(auth)

f = open('unfriend0.txt')
for l in f:
    if len(l) == 0: break
    id, junk = l.strip().split(' ', maxsplit=1)
    print(id)
    api.destroy_friendship(id=id)
