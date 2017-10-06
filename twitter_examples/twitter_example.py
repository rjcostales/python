#!/usr/bin/env python3

from twitter import Twitter, OAuth

from keys import TOKEN_KEY, TOKEN_SECRET, API_KEY, API_SECRET

oauth = OAuth(TOKEN_KEY, TOKEN_SECRET, API_KEY, API_SECRET)
twitter = Twitter(auth=oauth)


def print_status(status):
    text = status['text'].replace('\n', ' ').replace('&amp;', '&')
    print('%s\t%s\t%s' %
          (status['id_str'],
           status['user']['name'],
           text))


def print_statuses(statuses):
    for status in statuses:
        if not (status['text'].startswith("RT") or
                    status['text'].startswith(".@") or
                    status['text'].startswith("@")):
            print_status(status)


statuses = twitter.statuses.home_timeline()
print_statuses(statuses)

statuses = twitter.statuses.user_timeline(screen_name="@MaesterHacker")
print_statuses(statuses)

print('-----')
since = 800000000000000000

tweets = twitter.search.tweets(q="#RaspberryPi", since=since, count=500, lang="en")
print_statuses(tweets['statuses'])
