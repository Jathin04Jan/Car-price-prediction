import pickle
import streamlit as st

# Loading the saved pickle model
model = pickle.load(open('car_predictor.sav', 'rb'))

st.title('Car Price Predictor')

option = st.selectbox('How would you like to be contacted ? ', ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected: ', option)