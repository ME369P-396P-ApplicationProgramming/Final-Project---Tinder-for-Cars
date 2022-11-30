# from Liked import *
import streamlit as st
import sys
import Backend_logic as BCL
import cartest
import streamlit as st

#test of two cars
liked_cars = st.session_state.liked_cars
# yes_car()




# 1,2,3,4,5,6,7,8 = st.columns(8)
info_car=[]

for i in range(len(liked_cars)):
    info_car.append([liked_cars[i][1],liked_cars[i][2],liked_cars[i][5]])
    

#, col6, col7, col8
col1, col2, col3, col4, col5 = st.columns(5)
with col1:   
        st.write(info_car[1][1])
        st.write(info_car[2])
        st.write(info_car[3])
   
    
with col2:  
        st.write(liked_cars[i][1])
        st.write(liked_cars[i][2])
        st.write(liked_cars[i][5])   
with col3:
        pass
with col4:
        pass
with col5:
        pass

    
        
        