import pymongo
import urllib
from lexical.non_lexicals import non_lexical_words


non_lexical_words = {'words': non_lexical_words}

mongo_uri = "mongodb+srv://ranjani:" + urllib.parse.quote("fenderchamp@26") + "@cluster0-lsocm.mongodb.net/test?retryWrites=true&w=majority"
client = pymongo.MongoClient(mongo_uri)

lexical_db = client['non_lexicals']
lexical_collection = lexical_db['non_lexical_words']
x = lexical_collection.insert_one(non_lexical_words)
print(x)