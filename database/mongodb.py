from pymongo import MongoClient


class MongoDB:
    def __init__(self, db_name):
        self.db = MongoClient("localhost", 27017)[db_name]

    def insert(self, collection, data):
        return self.db[collection].insert_one(data).inserted_id

    def find(self, collection, query):
        return self.db[collection].find(query)

    def find_one(self, collection, query):
        return self.db[collection].find_one(query)

    def update(self, collection, query, data):
        return self.db[collection].update_one(query, data)
