from pymongo import MongoClient

def get_database():
    CONNECTION_STRING = 'mongodb+srv://username:password@cluster0.2saqp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
    client = MongoClient(CONNECTION_STRING)
    return client['Car']

db = get_database()
carfeatures = db['CarFeatures']