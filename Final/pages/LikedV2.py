# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 12:52:44 2022

@author: rohi
"""
import streamlit as st
import sys
import Backend_logic as BCL
import cartest
import numpy as np
import statistics as stat
import random
import math as m

sys.path.insert(0, r'C:\Users\hanna\OneDrive\Documents\UT Semester Courses\Fall 2022\Programming\Final Assignment\Final-Project---Tinder-for-Cars-main\Final-Project---Tinder-for-Cars-rohithnath2-FinalWorkingCode')



#Logic on top
def logic(all_cars):
    count=0
    if 'liked_cars' not in st.session_state:
        st.session_state['liked_cars'] = []
    
    q_cars = all_cars.copy()
    #print(len(all_cars))
    datapoints = 0
    if 'drawn_id_total' not in st.session_state:
        st.session_state['drawn_id_total'] = []
    end = 0
    

    st.session_state['i'] = 0
    #while cont ==  1:
    datapoints += 5
    drawn_id = []
    
    if 'counter' not in st.session_state:
        st.session_state['counter'] = 0
    
    if 'cars_left' not in st.session_state:
        st.session_state['cars_left'] = 0
        
    st.session_state.cars_left = len(q_cars) - st.session_state.counter

    
    if st.session_state.cars_left >= 1:
        rand_int = random.randint(0, len(q_cars)-1)
        while rand_int in drawn_id:
            rand_int = random.randint(0, len(q_cars)-1)
        drawn_id.append(rand_int)
        st.session_state.drawn_id_total.append(q_cars[rand_int][0])
        car_obj = q_cars[rand_int]
        


    st.session_state['i']+=1
    

        
    # if st.session_state.show ==1:
    col1, col3 , col4, col5, col6,col7,col8 = st.columns(7)
    with col1:
        with st.container():
            st.write("***Car Make:***")
            st.write(str(car_obj[1]))
            st.write("***Car Type:***")
            st.write(str(car_obj[4]))
            st.write('***Year:***') 
            st.write(str(car_obj[2]))
            st.write('***Mileage:***')
            st.write(str(car_obj[3]))
            st.write('***Price:***')
            st.write(str(car_obj[5]))  
    
                    
    # with col2: 
    #   #   st.image(
    #   #     car_obj[8],
    #   #     width=400, # Manually Adjust the width of the image as per requirement
    #   # )
    #   pass
        
    with col4:
       
        
         st.image(
          car_obj[8],
          width=400, # Manually Adjust the width of the image as per requirement
      )   
    
    with col3 :
       
        # for i in range(20):
        #     st.write(" ")
        # responseY = st.button('❤️',key = count)
        pass

    with col5:
        
        for i in range(20):
           st.write(" ")
        responseY = st.button('❤️',key = count)
    with col6:
        for i in range(20):
            st.write(" ")
        responseN = st.button('❌',key = count+1000)
    with col7:
        pass

    st.markdown("""<hr style="height:10px;border:none;color:#199;background-color:#CC0000;" /> """, unsafe_allow_html=True)


    count+=1
    
    if 'responseY' not in st.session_state:
        st.session_state['responseY'] = '' 
        
    
    if responseY:
                
        st.session_state.liked_cars.append(car_obj)
        st.session_state.counter +=1
        
        
    if responseN:
        nice = 0
        
    end = len(st.session_state['liked_cars'])
        # st.write("Number of liked cars:" ,end)
        
        
        
    if len(st.session_state.liked_cars) %5 == 0 and len(st.session_state.liked_cars) != 0 :
        #contY = st.button("Continue? yes ") 
        contN = st.button("Press Here to Find your Perfect Car ")
        if contN:
            car_ranges = BCL.analysis_cars(np.array(st.session_state.liked_cars,dtype=object).T[2], np.array(st.session_state.liked_cars,dtype=object).T[3], np.array(st.session_state.liked_cars,dtype=object).T[4])
            q_cars = BCL.find_q_cars(all_cars, car_ranges,st.session_state.drawn_id_total)
            #with st.empty():

            nice = 0
            car_obj = all_cars[rand_int]
            col1, col2, col3 , col4, = st.columns(4)
            matched_car = BCL.find_perfect_car(all_cars,stat.mean(car_ranges[0]),stat.mean(car_ranges[1]),stat.mean(car_ranges[2]))
            #st.write(type(matched_car))
            
            # print(matched_car)
            st.error("***THIS IS YOUR PERFECT MATCH!***")
          
            

            
            with col1:
                with st.container():
                    
                    st.write("***Car Make:***")
                    st.write(str(matched_car[1]))
                    st.write("***Car Type:***")
                    st.write(str(car_obj[4]))
                    st.write('***Year:***') 
                    st.write(str(matched_car[2]))
                    st.write('***Mileage:***')
                    st.write(str(matched_car[3]))
                    st.write('***Price:***')
                    st.write(str(matched_car[5]))  
            
                            
            with col2:
                
                st.image(
                  matched_car[8],
                  width=400, # Manually Adjust the width of the image as per requirement
              )
          


            st.markdown("""<hr style="height:10px;border:none;color:#199;background-color:#CC0000;" /> """, unsafe_allow_html=True)


all_cars = st.session_state['AllCar']
logic(all_cars)
