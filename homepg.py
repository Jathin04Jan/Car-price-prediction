import pickle
import streamlit as st
import numpy as np


# Loading the saved pickle model
model = pickle.load(open('car_predictor.sav', 'rb'))


st.title('Car Price Predictor')


# Taking the user input
year = st.number_input(label="Make Year: ", step= 1)
present_price = st.number_input(label="Present price (In lakhs): ", step=1., format= "%.2f")
km_driven = st.number_input(label="Km driven: ", step= 1)

fuel_type = st.selectbox('Whats the fuel type ? ', ('Petrol', 'Diesel', 'CNG'))
seller_type = st.selectbox('Whats the seller type ? ', ('Dealer', 'Individual'))
transmission = st.selectbox('Whats the transmission ? ', ('Automatic', 'Manual'))

owner = st.number_input(label="Owner: ", step= 1)


# Encode the data
if (fuel_type == 'Petrol') :
    fuel_type = 0
elif (fuel_type == 'Diesel'):
    fuel_type = 1
elif (fuel_type == 'CNG'):
    fuel_type = 2

if (seller_type == 'Dealer'):
    seller_type = 0
elif (seller_type == 'Individual'):
    seller_type = 1

if (transmission == 'Automatic'):
    transmission = 1
elif (transmission == 'Manual'):
    transmission = 0


# Creating the input data as a list
input_data = (year, present_price, km_driven, fuel_type, seller_type, transmission, owner)


# Reshaping the input data for prediction
input_data = np.asarray(input_data).reshape(1, -1)


# Creating a button and making prediction
if st.button('Predict Price'):
    predictions = model.predict(input_data)


    #Displaying the predicted prices
    st.success(f"Predicted price of the car is {int(predictions[0]*100000)}")