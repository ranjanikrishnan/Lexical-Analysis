import os
import pymongo
import urllib
from mongo.non_lex import non_lexical_words


non_lexical_words = {'words': non_lexical_words}

mongo_uri = "mongodb+srv://" + os.environ.get('MONGO_USERNAME') + ":" + urllib.parse.quote(os.environ.get('MONGO_PASSWORD')) + "@cluster0-lsocm.mongodb.net/test?retryWrites=true&w=majority"
client = pymongo.MongoClient(mongo_uri)

lexical_db = client['non_lexicals']
lexical_collection = lexical_db['non_lexical_words']
non_lex = lexical_collection.insert_one(non_lexical_words)
