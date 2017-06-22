#!/usr/bin/env python

import tweepy


def print_tweet(tweet):
    print("%s\t%s\t%s" %
          (tweet.created_at,
           tweet.user.name.ljust(20),
           tweet.text.replace('&amp;', '$')
           .replace('\n', ' ')
           .replace('\a', ' ')
           .replace('\t', ' ')
           .replace(' *', ' ')))


def print_user(user):
    print("%i\t%s" %
          (user.id, user.name))


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


def remove_friend(friends):
    for friend in friends:
        try:
            api.destroy_friendship(friend)
        except:
            print(friend)


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


def add_to_list(lid, users):
    for user in users:
        api.add_list_member(list_id=lid, user_id=user)


def remove_from_list(lid, users):
    for user in users:
        try:
            api.remove_list_member(list_id=lid, user_id=user)
        except:
            print(user)


from keys import ACCOUNT, API_KEY, API_SECRET, TOKEN_KEY, TOKEN_SECRET

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

# remove_friend((10350, 1688461, 14203895, 17783001))
# friends = list_friends()
# print(len(friends))
# print(friends)

print(ACCOUNT)
# list_friends()

user_timeline(10350)
