import secrets

def get_database():
    CONNECTION_STRING = 'mongodb+srv://f-abgrall:admin@cluster0.2saqp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
    client = secrets.pymongo.MongoClient(CONNECTION_STRING)
    return client['Car']

db = get_database()
carfeatures = db['CarFeatures']