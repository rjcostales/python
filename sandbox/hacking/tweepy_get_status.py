#!/usr/bin/env python

import tweepy

from keys0 import ACCOUNT, API_KEY, API_SECRET, TOKEN_KEY, TOKEN_SECRET
from tweepy_func import print_tweet

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(TOKEN_KEY, TOKEN_SECRET)
api = tweepy.API(auth)

# for id in [732249046333689856, 732136778782654464, 729020752117280768, 728262733565702148, 728150562185699328]:
#     api.retweet(id)
#
# for id in [738992657163161601, 738991142818058240, 738989883012743168]:
#     api.destroy_status(id)

for tweet in api.user_timeline(ACCOUNT):
    print_tweet(tweet)

print()

tweets = api.home_timeline(count=100)
for tweet in tweets:
    print_tweet(tweet)

print(len(tweets))
