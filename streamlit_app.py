from pymongo import MongoClient
import streamlit_app as st

def get_database():
    CONNECTION_STRING = 'mongodb+srv://f-abgrall:admin@cluster0.2saqp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
    client = MongoClient(CONNECTION_STRING)
    return client['Car']

db = get_database()
carfeatures = db['CarFeatures']


cars = [i for i in carfeatures.find()]

st.write(cars)