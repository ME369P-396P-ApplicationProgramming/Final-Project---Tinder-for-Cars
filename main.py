import streamlit as st
import pandas as pd
st.set_page_config(page_title = "Car Tinder")
st.sidebar.success("Pages")
st.title('Car Tinder')
price = st.slider("Price", min_value = 0, max_value = 100000, step = 1000)
mileage = st.text_input("Mileage")

zipcode = st.text_input("Zip Code")
radius = st.slider("Radius", min_value = 0, max_value = 500, step = 1)
submit_button = st.button("SubmitX", on_click)

info = [price,mileage,zipcode,radius]

def out_info():
    print(info)
    
if submit_button:
    print(info)
