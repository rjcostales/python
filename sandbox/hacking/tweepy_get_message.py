#!/usr/bin/env python

import pprint

import tweepy

from keys0 import API_KEY, API_SECRET, TOKEN_KEY, TOKEN_SECRET

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(TOKEN_KEY, TOKEN_SECRET)
api = tweepy.API(auth)

for msg in api.direct_messages():
    print('------------------------------------------------------------')
    pprint.pprint(msg)
    print('------------------------------------------------------------')
    print(msg.created_at)
    print(msg.sender_screen_name)
    print(msg.recipient_screen_name)
    print(msg.id)
    print(msg.text)

# api.send_direct_message(user="jesse_costales", text="sandbox!")
# api.destroy_direct_message(id=737871231274393603)
