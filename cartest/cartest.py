import streamlit as st
import main
st.title('Car Tinder')
price = st.slider("Price", min_value = 0, max_value = 100000, step = 1000)
mileage = st.text_input("Mileage")
zipcode = st.text_input("Zip Code")
radius = st.slider("Radius", min_value = 0, max_value = 500, step = 1)
submit_button = st.button("SubmitX")

info = [price,mileage,zipcode,radius]


if submit_button:
    print(main.inputs(info))
    st.write(str(main.inputs(info)))

        