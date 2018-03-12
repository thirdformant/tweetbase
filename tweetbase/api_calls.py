import os
import json

import tweepy

def twitter_auth():
    """
    Sets up OAuth for Twitter API
    """
    auth = tweepy.OAuthHandler(os.environ.get("CONSUMER_KEY"),
                               os.environ.get("CONSUMER_SECRET"))
    auth.set_access_token(os.environ.get("ACCESS_TOKEN"),
                          os.environ.get("ACCESS_SECRET"))

    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    return api


def get_tweets(api, query, geocode, tweet_mode="extended", count=100):
    """
    Fetches tweets
    """
    tweets_fetched = api.search(q=query,
                                geocode=geocode,
                                tweet_mode=tweet_mode,
                                count=count)

    return tweets_fetched
