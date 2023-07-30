import pymongo
connection_string = "mongodb://localhost:27017"
db_client = pymongo.MongoClient(connection_string)
DB_NAME="budgetgpt"
db_client = db_client.get_database("users")