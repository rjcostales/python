#!/usr/bin/env python

import tweepy

from keys1 import ACCOUNT, API_KEY, API_SECRET, TOKEN_KEY, TOKEN_SECRET


def print_user(user):
    print("%-20i%-20s%-20s" % (user.id, user.screen_name, user.name))


def list_list(lid):
    ids = []
    members = tweepy.Cursor(api.list_members, list_id=lid).items()
    for member in members:
        print_user(member)
        ids.append(member.id)
    return ids


auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(TOKEN_KEY, TOKEN_SECRET)
api = tweepy.API(auth)

objs = api.lists_all()
for obj in objs:
    print('%s-%s\t%i' % (ACCOUNT, obj.name, obj.id))
    members = list_list(obj.id)
    print(len(members))
