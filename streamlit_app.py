from pymongo import MongoClient
import streamlit as st
    
client = MongoClient(**st.secrets['mongo'])

def get_db():
    db = client.Car
    cars = db.CarFeatures
    return cars

cars = get_db()

car_makers = cars.distinct("Make")

st.write(""" # Car Features """)

def search_by_maker_model():
    researched_makers = cars.find({'Make': maker_input, 'Model': model_input}, {'_id': 0})
    for i in researched_makers:
        try:
            st.write(f"""La {i['Make']} {i['Model']} {i['Vehicle Style']},
            de {i['Year']} a {i['Engine HP']} chevaux 
            et {i['Engine Cylinders']} cylindres.
            Sa consommation sur autoroute est de {int(i['Highway L/100 km'])} L au 100 km 
            et de {int(i['City L/100 km'])} L au 100km en ville.""")
        except:
            st.write(f"""La {i['Make']} {i['Model']} {i['Vehicle Style']},
            de {i['Year']} est une voiture électrique.""")
   
maker_input = st.sidebar.selectbox("Search by Maker", car_makers)

if maker_input:
    car_models = cars.distinct('Model', {'Make': maker_input})  
    model_input= st.sidebar.selectbox("Search by Model", car_models)
    
if maker_input and model_input:
    search_by_maker_model()

form = st.form(key='my_form', clear_on_submit=True)
make = form.text_input('Constructeur')
model = form.text_input('Modèle')
year = form.number_input('Année', min_value=1900, max_value=2022, step=1)
hp = form.number_input('Chevaux', min_value=1, max_value=1200, step=1)
cylinders = form.number_input('Cylindres', min_value=1, max_value=16, step=1)
submit = form.form_submit_button('Submit')
st.text_input()
def add_car():
    cars.insert_one(
        {
            'Make': make,
            'Model': model,
            'Year': year,
            'Engine Fuel Type' : '',
            'Engine HP': hp,
            'Engine Cylinders' : cylinders,
            'Transmission Type': '',
            'Driven_Wheels': '', 
            'Number of Doors': 0,
            'Market Category': '',
            'Vehicle Size': '',
            'Vehicle Style': '',
            'Popularity': 3000, 
            'MSRP': 35000,
            'City L/100 km': 10,
            'Highway L/100 km': 14,
            'HP/Cylinders': hp/cylinders
        }
    )
    created_car = cars.find_one(
        {
            'Make': make, 
            'Model': model, 
            'Year': year, 
            'Engine HP': hp, 
            'Engine Cylinders' : cylinders,
        }
    )
    return created_car


if submit:
    your_new_car = add_car()
    st.success(f"The {your_new_car['Model']} from {your_new_car['Make']} have been added")
