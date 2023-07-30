import pymongo
connection_string = "mongodb://localhost:27017"
db_client = pymongo.MongoClient(connection_string)
DB_NAME="budgetgpt"
db_client = db_client.get_database(DB_NAME)

users_collection = db_client["user_details"]