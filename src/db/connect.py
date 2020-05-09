import pymongo
import urllib


def connect_db():
    mongo_uri = "mongodb+srv://ranjani:" + urllib.parse.quote("fenderchamp@26") + "@cluster0-lsocm.mongodb.net/test?retryWrites=true&w=majority"
    client = pymongo.MongoClient(mongo_uri)
    return client
