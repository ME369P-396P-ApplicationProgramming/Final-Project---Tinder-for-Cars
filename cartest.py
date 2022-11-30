import streamlit as st
import main
import Backend_logic as BCL

def input_page():
    
    st.set_page_config(page_title = "Car Tinder")
    st.sidebar.success("Pages")    
    
    st.title('Car Tinder')
    price = st.slider("Price", min_value = 0, max_value = 50000,value = [0,50000], step = 1000)
    zipcode = st.text_input("Zip Code")
    radius = st.slider("Radius", min_value = 0, max_value = 250, step = 5)
    submit_button = st.button("SubmitX")
    
    MinPrice = price[0]
    MaxPrice = price[1]
    
    info = [MinPrice,MaxPrice,zipcode,radius]
    
    if 'AllCar' not in st.session_state:
        st.session_state['AllCar'] = ''
    
    if submit_button:
        all_CarDet = BCL.run_logic(info)
        st.session_state['AllCar'] = all_CarDet
        

input_page()