#!/usr/bin/env python

import tweepy

from keys import API_KEY, API_SECRET, TOKEN_KEY, TOKEN_SECRET


auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(TOKEN_KEY, TOKEN_SECRET)
api = tweepy.API(auth)

f = open('game.txt')
for l in f:
    id = l[:20].strip()
    screen_name = l[20:40].strip()
    name = l[40:].strip()
    print(id, screen_name, name)
    api.create_friendship(id=id)
