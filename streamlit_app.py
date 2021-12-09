from pymongo import MongoClient
import streamlit as st
import pandas as pd
    
CONNECTION_STRING = 'mongodb+srv://f-abgrall:admin@cluster0.2saqp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
client = MongoClient(CONNECTION_STRING)
db = client.Car
cars = db.CarFeatures
car_makers = cars.aggregate([{'$group':{"_id": {"Make": "$Make"}}}])

st.write(""" # Car Features """)
makers = []
for i in car_makers:
    makers.append(i['_id']['Make'])

my_cont = st.container() 

search_by_maker = st.sidebar.selectbox("Search by Maker", makers)
search_by_model= st.sidebar.text_input("Search by Model")

with my_cont:
    if search_by_maker:
        pass
    if search_by_model:
        pass