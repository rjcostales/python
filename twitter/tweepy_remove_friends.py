#!/usr/bin/env python

import tweepy

from keys0 import API_KEY, API_SECRET, TOKEN_KEY, TOKEN_SECRET

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(TOKEN_KEY, TOKEN_SECRET)
api = tweepy.API(auth)

f = open('unfriend.txt')
for l in f:
    id = l[:20].strip()
    screen_name = l[20:40].strip()
    name = l[40:].strip()
    print(id, screen_name, name)
    api.destroy_friendship(id=id)
