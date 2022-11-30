from Liked import *
import streamlit as st

#test of two cars
liked_cars = [[1, 'Toyota Camry XLE', 1998, 157967, 'Sedan', 3242, ['2.2L 4-Cylinder Gas Engine', '4-Speed Automatic Transmission', '2 wheel drive - front', '20 City / 28 Highway'], 'https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=659651473&minPrice=355&maxPrice=3333&city=Austin&state=TX&zip=78705&searchRadius=50&marketExtension=include&isNewSearch=false&showAccelerateBanner=false&sortBy=relevance&numRecords=100&listingTypes=USED&referrer=%2Fcars-for-sale%2Fcars-between-355-and-3333%2Faustin-tx-78705%3Fdma%3D%26searchRadius%3D50%26priceRange%3D%26location%3D%26marketExtension%3Dinclude%26isNewSearch%3Dfalse%26showAccelerateBanner%3Dfalse%26sortBy%3Drelevance%26numRecords%3D100&clickType=listing', 'https://images.autotrader.com/borderscaler/1500/1125/2d363e/hn/c/65158eba7cb84337900862ab8864e090.jpg'],[2, 'Honda Cam XLE', 3000, 1007, 'MOOOO', 1000, ['2.2L 4-Cylinder Gas Engine', '4-Speed Automatic Transmission', '2 wheel drive - front', '20 City / 28 Highway'], 'https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=659651473&minPrice=355&maxPrice=3333&city=Austin&state=TX&zip=78705&searchRadius=50&marketExtension=include&isNewSearch=false&showAccelerateBanner=false&sortBy=relevance&numRecords=100&listingTypes=USED&referrer=%2Fcars-for-sale%2Fcars-between-355-and-3333%2Faustin-tx-78705%3Fdma%3D%26searchRadius%3D50%26priceRange%3D%26location%3D%26marketExtension%3Dinclude%26isNewSearch%3Dfalse%26showAccelerateBanner%3Dfalse%26sortBy%3Drelevance%26numRecords%3D100&clickType=listing', 'https://images.autotrader.com/borderscaler/1500/1125/2d363e/hn/c/65158eba7cb84337900862ab8864e090.jpg']]
# yes_car()




# 1,2,3,4,5,6,7,8 = st.columns(8)
info_car=[]

for i in range(2):
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

    
        
        