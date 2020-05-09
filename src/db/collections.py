from db.connect import connect_db

DATABASE = 'non_lexicals'
NON_LEXICAL_COLLECTION = 'non_lexical_words'


def non_lex_collection():
    client = connect_db()
    lexical_db = client[DATABASE]
    lexical_collection = lexical_db[NON_LEXICAL_COLLECTION]
    return lexical_collection
