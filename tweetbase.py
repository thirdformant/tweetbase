import pymongo
from dotenv import find_dotenv, load_dotenv
from pprint import pprint

from tweetbase import api_calls, db_handlers

def tweets_abdn(api, db):
    """
    Fetch tweets from Aberdeen
    """
    query = "-filter:retweets -from:blobrana -from:Gospel4Grampian"
    geocode = "57.1526,-2.11,40mi"
    tweets_fetched = api_calls.get_tweets(api, query, geocode, count=100)

    # Store tweets in tweets_abdn db collection
    tweets = []
    for tweet in tweets_fetched['statuses']:
        tweet.update({"search_metadata": tweets_fetched['search_metadata']})
        tweets.append(tweet)
    # skip document because it already exists in new collection
    try:
        inserted = db.tweets_abdn.insert_many(tweets, ordered=False)
    except pymongo.errors.BulkWriteError as e:
        # pprint(e.details["writeErrors"]["errmsg"])
        pass

def tweets_hsmith(api, db):
    """
    Fetch tweets from Hammersmith
    """
    query = "-filter:retweets"
    geocode = "51.4928,-0.2229,3mi"
    tweets_fetched = api_calls.get_tweets(api, query, geocode, count=100)

    # Store tweets in tweets_hsmith db collection
    tweets = []
    for tweet in tweets_fetched['statuses']:
        tweet.update({"search_metadata": tweets_fetched['search_metadata']})
        tweets.append(tweet)
    # skip document because it already exists in new collection
    try:
        inserted = db.tweets_hsmith.insert_many(tweets, ordered=False)
    except pymongo.errors.BulkWriteError as e:
        # pprint(e.details["writeErrors"]["errmsg"])
        pass


if __name__ == "__main__":
    print("Something")
    # Find the .env file and load it
    dotenv_path = find_dotenv()
    print(dotenv_path)
    load_dotenv(dotenv_path)

    # Twitter api authentication
    api = api_calls.twitter_auth()

    # Connect to the db
    db = db_handlers.mongodb_connect()

    # Fetch and store tweets from Aberdeen and Hammersmith
    tweets_abdn(api, db)
    tweets_hsmith(api, db)
