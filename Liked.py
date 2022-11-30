import streamlit as st
import numpy as np
from streamlit.components.v1 import html


st.set_page_config(page_title = "liked")

#set initial car option
def import_car():
    car_obj=np.array([1, 'Toyota Camry XLE', 1998, 157967, 'Sedan', 3242, ['2.2L 4-Cylinder Gas Engine', '4-Speed Automatic Transmission', '2 wheel drive - front', '20 City / 28 Highway'], 'https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=659651473&minPrice=355&maxPrice=3333&city=Austin&state=TX&zip=78705&searchRadius=50&marketExtension=include&isNewSearch=false&showAccelerateBanner=false&sortBy=relevance&numRecords=100&listingTypes=USED&referrer=%2Fcars-for-sale%2Fcars-between-355-and-3333%2Faustin-tx-78705%3Fdma%3D%26searchRadius%3D50%26priceRange%3D%26location%3D%26marketExtension%3Dinclude%26isNewSearch%3Dfalse%26showAccelerateBanner%3Dfalse%26sortBy%3Drelevance%26numRecords%3D100&clickType=listing', 'https://images.autotrader.com/borderscaler/1500/1125/2d363e/hn/c/65158eba7cb84337900862ab8864e090.jpg'])
    return car_obj

def next_car():
    car_obj=np.array([2, 'Your MOm', 2000, 100, 'Blue', 7802, ['2.2L 4-Cylinder Gas Engine', '4-Speed Automatic Transmission', '2 wheel drive - front', '20 City / 28 Highway'], 'https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=659651473&minPrice=355&maxPrice=3333&city=Austin&state=TX&zip=78705&searchRadius=50&marketExtension=include&isNewSearch=false&showAccelerateBanner=false&sortBy=relevance&numRecords=100&listingTypes=USED&referrer=%2Fcars-for-sale%2Fcars-between-355-and-3333%2Faustin-tx-78705%3Fdma%3D%26searchRadius%3D50%26priceRange%3D%26location%3D%26marketExtension%3Dinclude%26isNewSearch%3Dfalse%26showAccelerateBanner%3Dfalse%26sortBy%3Drelevance%26numRecords%3D100&clickType=listing', 'https://images.autotrader.com/borderscaler/1500/1125/2d363e/hn/c/65158eba7cb84337900862ab8864e090.jpg'])


car_obj=import_car()
#order: make, year, mileage, price
rel_info=[car_obj[1],car_obj[2],car_obj[3],car_obj[5]]

def nav_page(page_name, timeout_secs=3):
    #call new car object
    car_obj=next_car()
    
    
    nav_script = """
        <script type="text/javascript">
            function attempt_nav_page(page_name, start_time, timeout_secs) {
                var links = window.parent.document.getElementsByTagName("a");
                for (var i = 0; i < links.length; i++) {
                    if (links[i].href.toLowerCase().endsWith("/" + page_name.toLowerCase())) {
                        links[i].click();
                        return;
                    }
                }
                var elasped = new Date() - start_time;
                if (elasped < timeout_secs * 1000) {
                    setTimeout(attempt_nav_page, 100, page_name, start_time, timeout_secs);
                } else {
                    alert("Unable to navigate to page '" + page_name + "' after " + timeout_secs + " second(s).");
                }
            }
            window.addEventListener("load", function() {
                attempt_nav_page("%s", new Date(), %d);
            });
        </script>
    """ % (page_name, timeout_secs)
    html(nav_script)

x = 0 
st.title('Car Tinder')
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

global yes_list
yes_list={}
def yes_car():
    global response
    response = 1
    #creates a dictionary of 'yes' cars
    yes_list[car_obj[0]]=car_obj
    print(response)
    st.write(response)
    







col1, col2, col3 , col4, col5,col6, col7, col8 = st.columns(8)
with col1:
    pass
with col4:
   yes_button= st.button('Yes', key='yes',on_click = yes_car)
   if yes_button:
          nav_page('main')

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







