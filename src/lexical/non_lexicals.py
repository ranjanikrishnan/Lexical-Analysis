from db.find_all import db_find_all
from db.collections import non_lex_collection


def get_non_lex():
    collection = non_lex_collection()
    results = db_find_all(collection)
    for result in results:
        non_lex = result['words']
    return non_lex
