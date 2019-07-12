import os
import pymongo
from dotenv import find_dotenv, load_dotenv

def mongodb_connect():
    """
    Connects to the 'tweetbase' database
    """
    # Load environment variables
    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)
    # Connect to the db
    # DB will be created if it doesn't already exist
    client = pymongo.MongoClient(os.environ.get("DATABASE_URL"), 27017)
    db = client.tweetbase
    return db

def mongodb_init():
    """
    MongoDB automatically creates new databases and collections if they do not already exist. However, I want to specify several custom unique indices to prevent insertion of duplicate tweet documents. This can be done with e.g. db.collection.upsert(), but that replaces the existing document with the new version which is not always desirable.
    """
    # Load environment variables
    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)

    # Connect to the db
    # DB will be created if it doesn't already exist
    client = pymongo.MongoClient(os.environ.get("DATABASE_URL"), 27017)
    # 'tweetbase' is the database name
    db = client.tweetbase

    #Sets both the tweet ID and user ID strings as unique indexes
    db.tweets.create_index([("id_str", 1),
                            ("user.id_str", 1)],
                            unique=True)

    # The db is only actually created when something is inserted
    # So this inserts a test document and immediately deletes it...
    # AND EVERYTHING ELSE
    # DO NOT RUN THIS ON A DB YOU WANT TO KEEP. SERIOUSLY.
    db.tweets.insert_one({"id_str": 1, "user": {"id_str": 5}})
    db.tweets.remove()


def mongodb_drop():
    """
    Quick helper function to drop the tweetbase db via Python
    """
    # Load environment variables
    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)
    # Connect to the db
    # DB will be created if it doesn't already exist
    client = pymongo.MongoClient(os.environ.get("DATABASE_URL"), 27017)
    client = client.drop_database("tweetbase")
