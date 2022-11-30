import streamlit as st
import sys
import Backend_logic as BCL
import cartest
import numpy as np
import statistics as stat
import random
import math as m

sys.path.insert(0, '\Applications of Python\Final Project\Final-Project---Tinder-for-Cars-main\tindercar')

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

def logic_output():
    
    #st.write(str(BCL.car))
    pass

with col3 :
    pass


def yes_car():
    global response
    response = 1
    print(response)
    #st.write(str(BCL.run_logic2(a)))
    

    

col1, col2, col3 , col4, col5,col6, col7, col8 = st.columns(8)
with col1:
    pass
with col4:
   #yes_button= st.button('Yes', on_click = yes_car)
   pass
with col5:
    #no_button = st.button('No')
    pass
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



def logic(all_cars):
    if 'liked_cars' not in st.session_state:
        st.session_state['liked_cars'] = []
    
    q_cars = all_cars.copy()
    #print(len(all_cars))
    datapoints = 0
    drawn_id = []
    cont = 1
    end = 0
    count = 0

    st.session_state['i'] = 0
    #while cont ==  1:
    datapoints += 5
    
    #for z in range(datapoints):
    rand_int = random.randint(0, len(q_cars)-1)
    while rand_int in drawn_id:
        rand_int = random.randint(0, len(q_cars)-1)
    drawn_id.append(rand_int)
    show_car = all_cars[rand_int]
    st.write('randomly chosen car',st.session_state['i'], show_car)
    st.session_state['i']+=1
    
    
    if 'nice' not in st.session_state:
        st.session_state['nice'] = ''
    
    count+=1
    responseY = st.button('Yes answer',key = count)
    responseN = st.button('No',key = count+1000)
    if responseY:
        
        #st.session_state['liked_cars'].append(q_cars[rand_int])
        st.session_state.liked_cars.append(q_cars[rand_int])

        
    if responseN:
        nice = 0
        
    #nice = st.session_state['nice']
    #if nice == 1:
    #    liked_cars.append(q_cars[rand_int])
    end = len(st.session_state['liked_cars'])
    st.write("Number of liked cars:" ,end)
        
        
        
    if len(st.session_state.liked_cars) %5 ==0 and len(st.session_state.liked_cars) != 0 :
        contY = st.button("Continue? yes ") 
        contN = st.button("Continue? No ")
        if contN:
            car_ranges = BCL.analysis_cars(np.array(st.session_state['liked_cars'],dtype=object).T[2], np.array(st.session_state['liked_cars'],dtype=object).T[3], np.array(st.session_state['liked_cars'],dtype=object).T[4])
            q_cars = BCL.find_q_cars(all_cars, car_ranges,drawn_id)
            
            st.write( BCL.find_perfect_car(all_cars,stat.mean(car_ranges[0]),stat.mean(car_ranges[1]),stat.mean(car_ranges[2])))


all_cars = st.session_state['AllCar']
logic(all_cars)
