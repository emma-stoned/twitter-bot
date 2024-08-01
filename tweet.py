import tweepy
import time

# Authentication
auth = tweepy.OAuth1UserHandler(
    '10wgIULYcyy5vmVqsgVvHvoMX', 'snORrYBreKpKPFdfPtveGMQnUtMLPbuxKfxKW7IDqyxbdd2DJc')
auth.set_access_token('1684143886640492545-M6O3ZndY891IHb6Jz1jeWXbeEtyG7h',
                      'pnjJGGcFNJt2vUJZfZosu4FYYN0IS1njIPXt1LIp0cfgB')

api = tweepy.API(auth, timeout=120)

# Verify credentials
try:
    user = api.verify_credentials()
    print(user.name)
except tweepy.TweepyException as e:
    print(f"Error verifying credentials: {e}")


def limit_handle(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.TooManyRequests:
            print("Rate limit exceeded. Sleeping...")
            time.sleep(500)
        except StopIteration:
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(60)  # Sleep for a while before retrying


# Narcissistic bot
search2 = 'Hamza khan'
number_of_tweets = 5

try:
    for tweet in limit_handle(tweepy.Cursor(api.search_tweets, search2).items(number_of_tweets)):
        try:
            tweet.favorite()
            print('I liked that')
        except tweepy.TweepyException as error:
            print(f"Error liking tweet: {error.reason}")
except tweepy.TweepyException as e:
    print(f"Error during search: {e}")

# Generous bot
try:
    for follower in limit_handle(tweepy.Cursor(api.get_followers).items()):
        try:
            follower.follow()
            print(f"Followed {follower.screen_name}")
            break  # Breaking after the first follow for demonstration
        except tweepy.TweepyException as error:
            print(f"Error following user: {error.reason}")
except tweepy.TweepyException as e:
    print(f"Error during follower retrieval: {e}")
