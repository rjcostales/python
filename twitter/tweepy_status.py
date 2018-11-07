#!/usr/bin/env python
import tweepy

from hacking.keys0 import API_KEY, API_SECRET, TOKEN_KEY, TOKEN_SECRET


def print_tweet(tweet):
    out = "%i\t%s\t%s" % \
          (tweet.id,
           tweet.user.name,
           tweet.text
           .replace('\n', ' ')
           .replace('\r', ' ')
           .replace('\t', ' '))
    print(out)


def print_user(user):
    out = "%i\t%s\t%s\t%s\t%s" % \
          (user.id,
           user.name,
           user.screen_name,
           user.description
           .replace('\n', ' ')
           .replace('\r', ' ')
           .replace('\t', ' '),
           user.location)
    print(out)


# for id in [732249046333689856, 732136778782654464, 729020752117280768, 728262733565702148, 728150562185699328]:
#     api.retweet(id)

# for id in [738992657163161601, 738991142818058240, 738989883012743168]:
#     api.destroy_status(id)

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(TOKEN_KEY, TOKEN_SECRET)
api = tweepy.API(auth)

# for tweet in api.user_timeline(ACCOUNT):
#     print_tweet(tweet)

tweets = api.home_timeline(count=100)
for tweet in tweets:
    #    print_tweet(tweet)
    print(tweet)
    print()
print(len(tweets))
