#!/usr/bin/env python
import tweepy

from keys0 import API_KEY, API_SECRET, TOKEN_KEY, TOKEN_SECRET, ACCOUNT

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(TOKEN_KEY, TOKEN_SECRET)
api = tweepy.API(auth)


def print_tweet(tweet):
    print("%i\t%s\t%s" % (tweet.id, tweet.user.name, tweet.text.replace('\n', '\\n')))


def print_user(user):
    print('%s %s %s %s %s' %
          (str(user.id).ljust(24),
           user.name.ljust(24),
           user.screen_name.ljust(24),
           user.location,
           user.description.replace('\n', ' ')
           .replace('\r', ' ')
           .replace('\t', ' ')
           .replace('  *', ' ')))


def list_followers():
    followers = []
    for user in api.followers():
        print_user(user)
        followers.append(user.id)
    return followers


def list_friends():
    friends = []
    for id in api.friends_ids():
        friend = api.get_user(id)
        print_user(friend)
        friends.append(friend.id)
    return friends


print(ACCOUNT)
for tweet in api.retweets_of_me():
    print_tweet(tweet)
