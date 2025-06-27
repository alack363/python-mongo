from pymongo import MongoClient

# create and connect database
mongo_online_url = "mongodb+srv://api-python:seispapapa@cluster0.n769dwz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

mongo_Client = MongoClient(mongo_online_url)

# Access and testing
database = mongo_Client['database_test']
collection = database['collection_test']

person = {"name": "Lucca de Enzo", "age": 12}
collection.insert_one(person)