from pymongo import MongoClient
import streamlit as st
    
CONNECTION_STRING = 'mongodb+srv://f-abgrall:admin@cluster0.2saqp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
# client = MongoClient(**st.secrets['mongo'])
client = MongoClient(CONNECTION_STRING)

def get_db():
    db = client.Car
    cars = db.CarFeatures
    return cars

cars = get_db()

car_makers = cars.distinct("Make")

st.write(""" # Car Features """)

def search_by_maker_model():
    researched_maker = cars.find_one({'Make': maker_input, 'Model': model_input}, {'_id': 0})
    if researched_maker != None and researched_maker['Highway L/100 km'] != None:
        st.write(f"""La {researched_maker['Make']} {researched_maker['Model']} {researched_maker['Vehicle Style']},
        de {researched_maker['Year']} a {researched_maker['Engine HP']} chevaux 
        et {researched_maker['Engine Cylinders']} cylindres.
        Sa consommation sur autoroute est de {int(researched_maker['Highway L/100 km'])} L au 100 km 
        et de {int(researched_maker['City L/100 km'])} L au 100km en ville.""")
        
def add_car():
    cars.insert(
        {
            'Make': make,
            'Model': model,
            'Year': year,
            'Engine HP': hp,
            'Engine Cylinders' : cylinders,
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
    
maker_input = st.sidebar.selectbox("Search by Maker", car_makers)

form = st.form(key='my_form')
make = form.text_input('Constructeur')
model = form.text_input('Modèle')
year = form.text_input('Année')
hp = form.text_input('Chevaux')
cylinders = form.text_input('Cylindres')
submit = form.form_submit_button('Submit')

if maker_input:
    car_models = cars.distinct('Model', {'Make': maker_input})  
    model_input= st.sidebar.selectbox("Search by Model", car_models)
    
if maker_input and model_input:
    search_by_maker_model()

if submit:
    your_new_car = add_car()
    st.write(f"The {model} from {make} have been added")
