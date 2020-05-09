from db.connect import connect_db


def db_find_all(collection):
    results = collection.find()
    return results
