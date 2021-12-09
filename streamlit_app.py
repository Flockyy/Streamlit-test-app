from pymongo import MongoClient
import streamlit as st
import pandas as pd

def get_database():
    CONNECTION_STRING = 'mongodb+srv://f-abgrall:admin@cluster0.2saqp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
    client = MongoClient(CONNECTION_STRING)
    return client['Car']

db = get_database()
carfeatures = db['CarFeatures']


cars_constructor = [i for i in carfeatures.find({}, {'Make':1, '_id':0})]

st.write(""" # Car Features """)

st.write(cars_constructor)