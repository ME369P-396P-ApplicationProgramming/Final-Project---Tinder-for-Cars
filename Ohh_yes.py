# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 21:15:17 2022

@author: emils
"""

# -*- coding: utf-8 -*-


import requests
from bs4 import BeautifulSoup
import selenium
import numpy as np
import statistics as st
import random
import math as m
import tkinter as tk

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
    except:
        image_urls = ["errorImage.jpg"]
    
    try:
        return [make_model, year, miles, size, price, import_info, URL, image_urls[0]]
    except:
        print(image_urls)
        print("this is error")

def analysis_cars(year, milage, car_style): #list of car attributesr
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
        cars.append([ i, *get_car_info(urls[i])])
    
    return cars

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

def init_window(): 
    root=tk.Tk()
    
    root.geometry("600x400")
      
    zip_var=tk.IntVar()
    r_var=tk.IntVar()
    min_var=tk.IntVar()
    max_var=tk.IntVar()
     
    def submit():
     
        zip_code=zip_var.get()
        r=r_var.get()
        min_price=min_var.get()
        max_price=max_var.get()
    
        global info
        
        info = [zip_code, r, min_price, max_price]
        
        root.destroy()
        
        
    
    zip_label = tk.Label(root, text = 'Zip', font=('calibre',10, 'bold'))
    zip_entry = tk.Entry(root,textvariable = zip_var, font=('calibre',10,'normal'))
    
    r_label = tk.Label(root, text = 'r', font = ('calibre',10,'bold'))
    r_entry=tk.Entry(root, textvariable = r_var, font = ('calibre',10,'normal'))
    
    min_label = tk.Label(root, text = 'Min price', font = ('calibre',10,'bold'))
    min_entry=tk.Entry(root, textvariable = min_var, font = ('calibre',10,'normal'))
    
    max_label = tk.Label(root, text = 'Max price', font = ('calibre',10,'bold'))
    max_entry=tk.Entry(root, textvariable = max_var, font = ('calibre',10,'normal'))
      
    sub_btn=tk.Button(root,text = 'Submit', command = submit)
    
    zip_label.grid(row=0,column=0)
    zip_entry.grid(row=0,column=1)
    r_label.grid(row=1,column=0)
    r_entry.grid(row=1,column=1)
    min_label.grid(row=2,column=0)
    min_entry.grid(row=2,column=1)
    max_label.grid(row=3,column=0)
    max_entry.grid(row=3,column=1)
    sub_btn.grid(row=4,column=1)
      
    root.mainloop()
    
    return info


def show_car(car):
    print(car)
    print("\n")
    
    def send_yes():
        global answer
        answer = 1
        root.destroy()

    def send_no():
        global answer
        answer = 0
        root.destroy()

    root = tk.Tk()
    root.geometry("700x350")
    frame = tk.Frame(root)
    frame.pack()


    text_disp= tk.Button(frame, text="YES", fg="green", command=send_yes)

    text_disp.pack(side=tk.LEFT)

    exit_button = tk.Button(frame, text="NO",fg="red", command=send_no)

    exit_button.pack(side=tk.RIGHT)

    root.mainloop()
    
    return answer

zip_code, r, min_price, max_price = init_window()


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
        
        nice = show_car(all_cars[rand_int])
        
        if nice == 1:
            liked_cars.append(q_cars[rand_int])
        end = len(liked_cars)
        
    
    cont = int(input("Continue? (1/0): "))
    car_ranges = analysis_cars(np.array(liked_cars,dtype=object).T[2], np.array(liked_cars,dtype=object).T[3], np.array(liked_cars,dtype=object).T[4])
    q_cars = find_q_cars(all_cars, car_ranges)
    
    
    

print(find_perfect_car(all_cars,st.mean(car_ranges[0]),st.mean(car_ranges[1]),st.mean(car_ranges[2])))

