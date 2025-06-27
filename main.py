from pymongo import MongoClient
from dotenv import dotenv_values

config = dotenv_values('.env')

mongo_online_url = config['URI_MONGO_ATLAS']

# create and connect database

mongo_Client = MongoClient(mongo_online_url)


# Access and testing
database = mongo_Client['database_test']
collection = database['collection_test']

person = {"name": "Lucca de Enzo", "age": 12}
collection.insert_one(person)