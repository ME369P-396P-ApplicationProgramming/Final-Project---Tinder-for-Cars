import streamlit as st

x = 0 
st.title('Car Tinder')
col1, col2, col3 , col4, = st.columns(4)
with col1:
    pass
with col4:
    pass
with col2:
   st.image(
    "https://s3-us-west-2.amazonaws.com/uw-s3-cdn/wp-content/uploads/sites/6/2017/11/04133712/waterfall.jpg",
    width=400, # Manually Adjust the width of the image as per requirement
) 
st.caption("Price:{}",x)
st.caption("Mileage:")

with col3 :
    pass


def yes_car():
    global response
    response = 1
    print(response)
    


col1, col2, col3 , col4, col5,col6, col7, col8 = st.columns(8)
with col1:
    pass
with col4:
   yes_button= st.button('Yes', on_click = yes_car)
with col5:
    no_button = st.button('No')
with col2:
    pass
with col3 :
    pass
with col6 :
    pass
with col7 :
    pass
with col8 :
    pass

