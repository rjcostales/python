def print_tweet(tweet):
    out = "%s %-20s %s" % \
          (tweet.created_at,
           tweet.user.name,
           tweet.text
           .replace('\n', ' ')
           .replace('\r', ' ')
           .replace('\t', ' '))
    print(out)


def print_user(user):
    out = "%-20i %-20s %s %s %s" % \
          (user.id,
           user.name,
           user.screen_name,
           user.description
           .replace('\n', ' ')
           .replace('\r', ' ')
           .replace('\t', ' '),
           user.location)
    print(out)
