#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 19:32:39 2022

@author: kevinnguyen
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 20:18:54 2022

@author: emils
"""

import requests
from bs4 import BeautifulSoup
import numpy as np
import statistics as st
import random
import math as m

def search_cars(zip_code, r, min_price, max_price):
    
    URL = f"https://www.autotrader.com/cars-for-sale/cars-between-{min_price}-and-{max_price}/austin-tx-{zip_code}?dma=&searchRadius={r}&priceRange=&location=&marketExtension=include&isNewSearch=false&showAccelerateBanner=false&sortBy=relevance&numRecords=100"

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    a_tags = soup.select('a[aria-label]')

    all_tags = []
    for tag in a_tags:
        all_tags.append(tag.text.strip())
        
    page_navigator = [x for x in all_tags if x != '']

    if len(page_navigator) > 1:
        pages = list(page_navigator[-2])[-1]
        all_URLs = [f"https://www.autotrader.com/cars-for-sale/cars-between-{min_price}-and-{max_price}/austin-tx-{zip_code}?dma=&searchRadius={r}&priceRange=&location=&marketExtension=include&isNewSearch=false&showAccelerateBanner=false&sortBy=relevance&numRecords=100"]
        for i in range(int(pages)-1):
            all_URLs.append(URL+"&firstRecord={}".format((i+1)*100))
    else:
        all_URLs = [URL]
    
    
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
    
    return unique_car_links

def all_urls_of_search(zip_code, r, min_price, max_price):
    page_links = search_cars(zip_code, r, min_price, max_price)
    
    car_URL = np.array([])
    
    for link in page_links:
        car_URL = np.append(car_URL,get_all_links(link))
        
    car_URL = car_URL.tolist()
    
    return car_URL
    
def get_car_info(URL):
    page = requests.get(URL)
    page.status_code
    
    soup = BeautifulSoup(page.content, 'html.parser')
    
    try:
        result = soup.find_all('head')[0]
        result2 = result.find('title').get_text()
        
        
        year = result2.split(" ")[1]
        make_model = result2.split("for")[0].split(year)[1].strip()
        size = result2.split(" ")[-6]
        if size == "Utility":
            size = "Sport Utility"
        
        year = int(year)
        
        import_info = []
        basic_info = soup.find_all('div',attrs={'class':'container'})
        body = basic_info[1]
            
        importInfo_lst = body.find_all('li')
        for item in importInfo_lst:
            import_info.append(item.text.strip())
        
        miles = int(import_info[0].split(" ")[0].replace(",", ""))
         
        price = soup.find('span',attrs={'class':'first-price first-price-lg text-size-700'})
        
        list_price = price.get_text()
        
        price = int(list_price.replace(",", ""))
        
        import_info.pop(0)
         
        image = get_images(URL)
             
    except:
        pass
    
    return [make_model, year, miles, size, price, import_info, URL]

def get_images(URL):
    page = requests.get(URL)
    page.status_code
    
    soup = BeautifulSoup(page.content, 'html.parser')
    
    images = soup.find_all('img')
     
    image_urls = []

    for img in images:
        if img.has_attr('src') and ('https://images.autotrader.com' in img['src']):
            image_urls.append(img['src'])

    if len(image_urls) == 0:
        image_urls.append("no photos")
    else:
        for i in range(len(image_urls)):
            image_urls[i] = image_urls[i].split("/")
            
            if image_urls[i][3] == "resize":
                l = 1500
                image_urls[i][4] = image_urls[i][4].split("x")
                w = round(l/(int(image_urls[i][4][0])/int(image_urls[i][4][1])))
                
                image_urls[i][4][0] = str(l)
                image_urls[i][4][1] = str(w)
                
                image_urls[i][4] = "x".join(image_urls[i][4]) 
                
            else:
                l = 1500
                w = round(l/(int(image_urls[i][4])/int(image_urls[i][5])))
                
                image_urls[i][4] = str(l)
                image_urls[i][5] = str(w)
            image_urls[i] = "/".join(image_urls[i] )
    
    im = image_urls[0]
    
    return im

def analysis_cars(year, milage, car_style): #list of car attributes
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
    
def all_urls_of_search(zip_code, r, min_price, max_price):
    page_links = search_cars(zip_code, r, min_price, max_price)
    
    car_URL = np.array([])
    
    for link in page_links:
        car_URL = np.append(car_URL,get_all_links(link))
        
    car_URL = car_URL.tolist()
    
    return car_URL

def get_all_cars(zip_code,r ,min_price, max_price):
    urls = all_urls_of_search(zip_code, r, min_price, max_price)
    
    cars = []
    
    for i in range(len(urls)):
        cars.append([ i, *get_car_info(urls[i]),get_images(urls[i])])
    
    return cars

def show_car(car):
    print(car)

def find_perfect_car(cars, year, milage, car_style): 
    z_score = []
    
    style = ["Hatchback","Coupe" , "Sedan", "Convertible", "Wagon", "Sport Utility", "Truck", "Van" ]
    
    
    for car in cars:
        z = m.sqrt((car[2]*2-2*year)**2+(car[3]/10000-milage/10000)**2+(style.index(car[4])*2-car_style*2)**2)
        z_score.append(z)
    
    return cars[z_score.index(min(z_score))]

def find_q_cars(all_cars, car_ranges):
    global drawn_id
    style = ["Hatchback","Coupe" , "Sedan", "Convertible", "Wagon", "Sport Utility", "Truck", "Van" ]
    q_cars = []
    
    for car in all_cars:
        if (car[0] not in drawn_id) and (car_ranges[0][0] <= car[2] <= car_ranges[0][1]) and (car_ranges[1][0] <= car[3] <= car_ranges[1][1]) and (car_ranges[2][0] <= style.index(car[4]) <= car_ranges[2][1]):
           q_cars.append(car) 
    
    return q_cars


zip_code = input("Zip: ")
r = input("Radius: ")
min_price = input("Min. price: ")
max_price = input("Max. price: ")

all_cars = get_all_cars(zip_code,r ,min_price, max_price)
liked_cars = []
q_cars = all_cars.copy()
print(len(all_cars))
datapoints = 0
drawn_id = []
cont = 1
end = 0

while cont ==  1:
    datapoints += 5
    
    while end < datapoints:
        
        rand_int = random.randint(0, len(q_cars)-1)
        while rand_int in drawn_id:
            rand_int = random.randint(0, len(q_cars)-1)
        drawn_id.append(rand_int)
        show_car(all_cars[rand_int])
        nice = int(input("Like? (1/0): "))
        if nice == 1:
            liked_cars.append(q_cars[rand_int])
        end = len(liked_cars)
    cont = int(input("Continue? (1/0): "))
    car_ranges = analysis_cars(np.array(liked_cars,dtype=object).T[2], np.array(liked_cars,dtype=object).T[3], np.array(liked_cars,dtype=object).T[4])
    q_cars = find_q_cars(all_cars, car_ranges)


    
print(find_perfect_car(all_cars,st.mean(car_ranges[0]),st.mean(car_ranges[1]),st.mean(car_ranges[2])))
    