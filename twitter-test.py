import tweepy

consumer_key = '<your_consumer_key>'
consumer_secret = '<your_consumer_secret>'

access_token = '<your_access_token>'
access_token_secret = '<your_access_token_secret>'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

trends = api.home_timeline()

print(trends[-1].text)

api.update_status("This is a new tweet from Tweepy")
