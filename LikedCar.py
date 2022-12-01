# from Liked import *
import streamlit as st
import sys
import Backend_logic as BCL
import cartest
import streamlit as st

#test of two cars
liked_cars = st.session_state.liked_cars
# yes_car()



def Add_car(likelist):


    # 1,2,3,4,5,6,7,8 = st.columns(8)
    info_car=likelist
    # st.write(info_car[0])
    
    
    for i in range(len(info_car)):
    #     cols = st.
    #     with col[i]:
        col1, col2, col3 , col4, = st.columns(4)
        with col1:
            with st.container():
                st.write('***Car Make:***')
                st.write(str(info_car[i][1]))
                st.write("***Car Type:***")
                st.write(str(info_car[i][4]))
                st.write('***Year:***') 
                st.write(str(info_car[i][2]))
                st.write('***Mileage:***')
                st.write(str(info_car[i][5]))
                st.write('***Price:***')
                st.write(str(info_car[i][3]))
                
                
        
                        
        with col2: 
            st.image(
              info_car[i][8],
              width=400, # Manually Adjust the width of the image as per requirement
          )   
            
        with col4:
            pass
        
        with col3 :
            
            pass
        st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)
    
    # for i in len(info_car)
    #         col1, col2, col3, col4, col5 = st.columns(5)
    #         with col:
    #             with st.container():
    #                 st.write("Car Make: ")
    #                 st.write(str(matched_car[1]))
    #                 st.write('Year: ') 
    #                 st.write(str(matched_car[2]))
    #                 st.write('Mileage: ')
    #                 st.write(str(matched_car[3]))
    #                 st.write('Price: ')
    #                 st.write(str(matched_car[5]))
    

    # for i in range(len(liked_cars)):
    #     info_car.append([liked_cars[i][1],liked_cars[i][2],liked_cars[i][5]])
        
    
    # #, col6, col7, col8
    # col1, col2, col3, col4, col5 = st.columns(5)
    # with col1:   
    #         st.write(info_car[1][1])
    #         st.write(info_car[2])
    #         st.write(info_car[3])
       
        
    # with col2:  
    #         st.write(liked_cars[i][1])
    #         st.write(liked_cars[i][2])
    #         st.write(liked_cars[i][5])   
    # with col3:
    #         pass
    # with col4:
    #         pass
    # with col5:
    #         pass



a=st.session_state['liked_cars']
Add_car(a)
        
        