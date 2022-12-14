# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 15:09:50 2022

@author: emil
"""

# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup
import selenium
import numpy as np
import statistics as stat
import random
import math as m

#Makes a list of all the pages
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

#Gets all links on one page     
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

#Gets link of all cars on all pages
def all_urls_of_search(zip_code, r, min_price, max_price):
    page_links = search_cars(zip_code, r, min_price, max_price)
    
    car_URL = np.array([])
    
    for link in page_links:
        car_URL = np.append(car_URL,get_all_links(link))
        
    car_URL = car_URL.tolist()
    
    return car_URL

#Gets all info about one car    
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
         
        
        images = soup.find_all('img')
         
        image_urls = []

        for img in images:
            if img.has_attr('src') and ('https://images.autotrader.com' in img['src']):
                image_urls.append(img['src'])

        if len(image_urls) == 0:
            image_urls.append("https://t4.ftcdn.net/jpg/02/51/95/53/360_F_251955356_FAQH0U1y1TZw3ZcdPGybwUkH90a3VAhb.jpg")
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
    except:
        image_urls = ["https://t4.ftcdn.net/jpg/02/51/95/53/360_F_251955356_FAQH0U1y1TZw3ZcdPGybwUkH90a3VAhb.jpg"]
    
    try:
        return [make_model, year, miles, size, price, import_info, URL, image_urls[0]]
    except:
        return ["N/A"*8]
        print(image_urls)
        print("this is error")

#Calulate ranges for next cars to qualify
def analysis_cars(year, milage, car_style): #list of car attributesr
    mean_year = stat.mean(year)
    sd_year = stat.stdev(year)
    
    year_range = [round(mean_year-sd_year),round(mean_year+sd_year)]
    
    mean_milage = stat.mean(milage)
    sd_milage = stat.stdev(milage)
    
    milage_range = [round(mean_milage-sd_milage),round(mean_milage+sd_milage)]
    
    style = ["Hatchback","Coupe" , "Sedan", "Convertible", "Wagon", "Sport Utility", "Truck", "Van" ]
    
    style_size = [style.index(item) for item in car_style]
    
    mean_style = stat.mean(style_size)
    sd_style = stat.stdev(style_size)
    
    style_range = [round(mean_style-sd_style),round(mean_style+sd_style)]

    return year_range, milage_range, style_range
#Gets link of all cars on all pages    
def all_urls_of_search(zip_code, r, min_price, max_price):
    page_links = search_cars(zip_code, r, min_price, max_price)
    
    car_URL = np.array([])
    
    for link in page_links:
        car_URL = np.append(car_URL,get_all_links(link))
        
    car_URL = car_URL.tolist()
    
    return car_URL

#Stores all car info, and link each car with an id
def get_all_cars(zip_code,r ,min_price, max_price):
    urls = all_urls_of_search(zip_code, r, min_price, max_price)
    
    cars = []
    
    for i in range(len(urls)):
        cars.append([ i, *get_car_info(urls[i])])
    
    return cars

def show_car(car):
    print(car)
    
    return car

#Finds the best car based on a list of car input (typically liked cars)
def find_perfect_car(cars, year, milage, car_style): 
    z_score = []
    
    style = ["Hatchback","Coupe" , "Sedan", "Convertible", "Wagon", "Sport Utility", "Truck", "Van" ]
    
    
    for car in cars:
        z = m.sqrt((car[2]*2-2*year)**2+(car[3]/10000-milage/10000)**2+(style.index(car[4])*2-car_style*2)**2)
        z_score.append(z)
    print(cars[z_score.index(min(z_score))])
    return cars[z_score.index(min(z_score))]

#Finds the qualified cars after 5 liked cars
def find_q_cars(all_cars, car_ranges, drawn_id): 
    #global drawn_id
    style = ["Hatchback","Coupe" , "Sedan", "Convertible", "Wagon", "Sport Utility", "Truck", "Van" ]
    q_cars = []
    
    for car in all_cars:
        if (car[0] not in drawn_id) and (car_ranges[0][0] <= car[2] <= car_ranges[0][1]) and (car_ranges[1][0] <= car[3] <= car_ranges[1][1]) and (car_ranges[2][0] <= style.index(car[4]) <= car_ranges[2][1]):
           q_cars.append(car) 
    
    return q_cars

#imports input from GUI
def import_inputs(info):
    MinPrice =  info[0]
    MaxPrice = info[1] 
    zipcode =  info[2] 
    radius =  info[3] 
    return [MinPrice,MaxPrice,zipcode,radius]

#First part of backend when interacting with user
def run_logic(info):
    '''
    zip_code = 
    r = input("Radius: ")
    min_price = input("Min. price: ")
    max_price = input("Max. price: ")
    '''
    ## Fake Inputs
   
    
    min_price,max_price,zip_code,r = info
    

    
    all_cars = get_all_cars(zip_code,r ,min_price, max_price)
    
    return all_cars
    # send all_cars to liked_cars(all_cars)

#Second part of backend when interacting with user
def run_logic2(all_cars):
   
    liked_cars = []
    q_cars = all_cars.copy()
    datapoints = 0
    drawn_id_total = []
    cont = 1
    end = 0

    while cont ==  1:
        datapoints += 5
        counter = 0
        drawn_id = []
        
        while end < datapoints:
            cars_left = len(q_cars) - counter
            
            if cars_left >= 1:
                rand_int = random.randint(0, len(q_cars)-1)
                while rand_int in drawn_id:
                    rand_int = random.randint(0, len(q_cars)-1)
                drawn_id.append(rand_int)
                drawn_id_total.append(q_cars[rand_int][0])
                show_car(q_cars[rand_int])
                
                
                
                nice = int(input("Like? (1/0): "))
                if nice == 1:
                    liked_cars.append(q_cars[rand_int])
                    counter += 1
                end = len(liked_cars)
                
            else:
                cont = 0
                break
        
        if cont == 1:
            cont = int(input("Continue? (1/0): "))
        
            
        car_ranges = analysis_cars(np.array(liked_cars,dtype=object).T[2], np.array(liked_cars,dtype=object).T[3], np.array(liked_cars,dtype=object).T[4])
        q_cars = find_q_cars(all_cars, car_ranges, drawn_id_total) 
        
        
    match = (find_perfect_car(all_cars,stat.mean(car_ranges[0]),stat.mean(car_ranges[1]),stat.mean(car_ranges[2])))
    perfect = find_perfect_car(all_cars,stat.mean(car_ranges[0]),stat.mean(car_ranges[1]),stat.mean(car_ranges[2]))
    
'''
print("program start")
info = [6000,7000,78705,50]
a = run_logic(info)
run_logic2(a)
'''
