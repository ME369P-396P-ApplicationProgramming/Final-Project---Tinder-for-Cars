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
    drawn_id = []
    cont = 1
    end = 0
    first = 1

    st.session_state['i'] = 0
    #while cont ==  1:
    datapoints += 5
    
    #for z in range(datapoints):
    rand_int = random.randint(0, len(q_cars)-1)
    while rand_int in drawn_id:
        rand_int = random.randint(0, len(q_cars)-1)
    drawn_id.append(rand_int)
    show_car = all_cars[rand_int]
    
    if st.session_state.submit_button:
        with st.empty():
            car_obj = show_car
            col1, col2, col3 , col4, = st.columns(4)
            with col1:
                with st.container():
                    st.write("Car Make: ")
                    st.write(str(car_obj[1]))
                    st.write('Year: ') 
                    st.write(str(car_obj[2]))
                    st.write('Mileage: ')
                    st.write(str(car_obj[5]))
                    st.write('Price: ')
                    st.write(str(car_obj[3]))  
                        
            with col2: 
                st.image(
                 car_obj[8],
                 width=400, # Manually Adjust the width of the image as per requirement
             )   
                
            with col4:
                pass
            
            with col3 :
                
                pass
            
            #st.session_state['liked_cars'].append(q_cars[rand_int])
            st.session_state.liked_cars.append(q_cars[rand_int])
        
    
    
    
    # st.write('randomly chosen car',st.session_state['i'], show_car)
    st.session_state['i']+=1
    
    
    if 'nice' not in st.session_state:
        st.session_state['nice'] = ''
    
    count+=1
    responseY = st.button('Yes answer',key = count)
    responseN = st.button('No',key = count+1000)
    # def_next_car()
    if responseY:
        with st.empty():

            car_obj = all_cars[rand_int]
            col1, col2, col3 , col4, = st.columns(4)
            with col1:
                with st.container():
                    st.write("Car Make: ")
                    st.write(str(car_obj[1]))
                    st.write('Year: ') 
                    st.write(str(car_obj[2]))
                    st.write('Mileage: ')
                    st.write(str(car_obj[5]))
                    st.write('Price: ')
                    st.write(str(car_obj[3]))  
            
                            
            with col2: 
                st.image(
                 car_obj[8],
                 width=400, # Manually Adjust the width of the image as per requirement
             )   
                
            with col4:
                pass
            
            with col3 :
                
                pass
            #st.session_state['liked_cars'].append(q_cars[rand_int])
            st.session_state.liked_cars.append(q_cars[rand_int])
        
        
    if responseN:
        with st.empty():
            nice = 0
            car_obj = all_cars[rand_int]
            col1, col2, col3 , col4, = st.columns(4)
            with col1:
                with st.container():
                    st.write("Car Make: ")
                    st.write(str(car_obj[1]))
                    st.write('Year: ') 
                    st.write(str(car_obj[2]))
                    st.write('Mileage: ')
                    st.write(str(car_obj[5]))
                    st.write('Price: ')
                    st.write(str(car_obj[3]))  
            
                            
            with col2: 
                st.image(
                 car_obj[8],
                 width=400, # Manually Adjust the width of the image as per requirement
             )
            
        #nice = st.session_state['nice']
        #if nice == 1:
        #    liked_cars.append(q_cars[rand_int])
        end = len(st.session_state['liked_cars'])
        # st.write("Number of liked cars:" ,end)
        
        
        
    if len(st.session_state.liked_cars) %5 == 0 and len(st.session_state.liked_cars) != 0 :
        contY = st.button("Continue? yes ") 
        contN = st.button("Continue? No ")
        if contN:
            car_ranges = BCL.analysis_cars(np.array(st.session_state['liked_cars'],dtype=object).T[2], np.array(st.session_state['liked_cars'],dtype=object).T[3], np.array(st.session_state['liked_cars'],dtype=object).T[4])
            q_cars = BCL.find_q_cars(all_cars, car_ranges,drawn_id)
            
            st.write( BCL.find_perfect_car(all_cars,stat.mean(car_ranges[0]),stat.mean(car_ranges[1]),stat.mean(car_ranges[2])))


# all_cars = st.session_state['AllCar']




def logic_output():
    
    #st.write(str(BCL.car))
    pass




def yes_car():
    global response
    response = 1
    print(response)
    #st.write(str(BCL.run_logic2(a)))
    

    




all_cars = st.session_state['AllCar']
logic(all_cars)
