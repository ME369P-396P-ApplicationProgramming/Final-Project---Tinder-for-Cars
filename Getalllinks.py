# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 20:18:54 2022

@author: emils
"""

import requests
from bs4 import BeautifulSoup
import selenium
import numpy as np
import statistics as st

def search_cars(zip_code, r, min_price, max_price):
    
    URL = f"https://www.autotrader.com/cars-for-sale/cars-between-{min_price}-and-{max_price}/austin-tx-{zip_code}?dma=&searchRadius={r}&priceRange=&location=&marketExtension=include&isNewSearch=false&showAccelerateBanner=false&sortBy=relevance&numRecords=100"

    print(URL)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    a_tags = soup.select('a[aria-label]')
    print(a_tags)
    all_tags = []
    for tag in a_tags:
        all_tags.append(tag.text.strip())
        
    print(all_tags)
    page_navigator = [x for x in all_tags if x != '']
    
    print(page_navigator)
    pages = list(page_navigator[-2])[-1]
    print(pages)
    
    all_URLs = [f"https://www.autotrader.com/cars-for-sale/cars-between-{min_price}-and-{max_price}/austin-tx-{zip_code}?dma=&searchRadius={r}&priceRange=&location=&marketExtension=include&isNewSearch=false&showAccelerateBanner=false&sortBy=relevance&numRecords=100"]
    for i in range(int(pages)-1):
        all_URLs.append(URL+"&firstRecord={}".format((i+1)*100))
    
    print(len(all_URLs))
    return all_URLs
    
    

def get_all_links(URL):
    
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    all_links = []
    for link in soup.find_all('a'):
        all_links.append(link.get('href'))
    
    no_none_links = [x for x in all_links if not isinstance(x, type(None))]
    
    substring = "vehicledetails" 
    
    all_car_links = [item for item in no_none_links if substring in item]
    unique_car_links = list(set(all_car_links))
    
    unique_car_links = ["https://www.autotrader.com" + s for s in unique_car_links]
    print(len(unique_car_links))
    
    return unique_car_links
    

def analyse_cars(year, milage, car_style): #list of car attributes
    mean_year = st.mean(year)
    sd_year = st.stdev(year)
    
    year_range = [mean_year-sd_year,mean_year+sd_year]
    
    mean_milage = st.mean(milage)
    sd_milage = st.stdev(milage)
    
    milage_range = [mean_milage-sd_milage,mean_milage+sd_milage]
    
    style = ["Hatchback","Coupe" , "Sedan", "Convertible", "Wagon", "Sport Utility", "Truck", "Van" ]
    
    style_size = [style.index(item) for item in car_style]
    
    mean_style = st.mean(style_size)
    sd_style = st.stdev(style_size)
    
    style_range = [mean_style-sd_style,mean_style+sd_style]

    return year_range, milage_range, style_range
    
def find_cars(n, car_dict, years, milages, styles):
    found_cars = []
    
    i_year = 0
    i_milage = 1
    i_style = 2
    
    for car, att in car_dict.items():
        if (years[0] < att[i_year] < years[1]) and (milages[0] < att[i_milage] < milages[1]) and (styles[0] < att[i_year] < styles[1]): 
            found_cars.append(car)
    
    return found_cars
    
page_links = search_cars(70001, 50, 3000, 100000)

car_URL = np.array([])

for link in page_links:
    car_URL = np.append(car_URL,get_all_links(link))
    
car_URL = car_URL.tolist()
