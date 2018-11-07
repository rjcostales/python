#!/usr/bin/env python

import tweepy

from keys0 import ACCOUNT, API_KEY, API_SECRET, TOKEN_KEY, TOKEN_SECRET
from tweepy_func import print_tweet, print_user


def home_timeline():
    for tweet in api.home_timeline(count=100):
        if not tweet.text.startswith("RT"):
            print_tweet(tweet)


def user_timeline(user):
    for tweet in api.user_timeline(user):
        if not tweet.text.startswith("RT"):
            print_tweet(tweet)


def search_user(query):
    for user in api.search_users(q=query):
        print_user(user)


def list_followers():
    ids = []
    for user in tweepy.Cursor(api.followers).items():
        print_user(user)
        ids.append(user.id)
    return ids


def list_friends():
    ids = []
    friends = tweepy.Cursor(api.friends).items()
    for friend in friends:
        print_user(friend)
        ids.append(friend.id)
    return ids


def list_timelines():
    for tweet in api.home_timeline(count=50):
        if not tweet.text.startswith("RT"):
            print_tweet(tweet)

    for list in api.lists_all():
        print("\n%s %s" % (list.name, list.id))
        # for member in api.list_members(list_id=list.id):
        #     print('-' + member.name)
        for tweet in api.list_timeline(list_id=list.id):
            if not tweet.text.startswith("RT"):
                print_tweet(tweet)


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

# f = open('politics.csv')
# for l in f:
#     id, name = l.split(',')
#     api.remove_list_member(list_id=845790314195382272, id=id)
#     print(name)

# f = open('temp')
# for l in f:
#     id, name = l.split('\t')
#     api.create_friendship(id=id)

# objs = api.lists_all()
# for obj in objs:
#     print('%s-%s\t%i' % (ACCOUNT, obj.name, obj.id))
#     members = list_list(obj.id)
#     print(len(members))


print(ACCOUNT)
# list_friends()

user_timeline(726523902252306432)

user_timeline(742155114488565760)

user_timeline(24870482)
