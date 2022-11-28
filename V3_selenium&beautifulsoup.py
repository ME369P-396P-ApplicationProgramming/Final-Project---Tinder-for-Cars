# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 16:50:06 2022

@author: rohit
"""

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options


opts = Options()
opts.add_argument("user-agent= [Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36]")
chrome_driver = 'C:/Program Files (x86)/chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver,chrome_options=opts)


url1 = 'https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=664361397&allListingType=all-cars&zip=78705&state=TX&city=Austin&dma=&searchRadius=50&isNewSearch=false&referrer=%2Fcars-for-sale%2Fall-cars%3Fzip%3D78705&clickType=listing'
url2 = 'https://www.autotrader.com/cars-for-sale/vehicledetails.xhtml?listingId=664621022&allListingType=all-cars&zip=78705&state=TX&city=Austin&searchRadius=50&isNewSearch=false&referrer=%2Fcars-for-sale%2Fall-cars%3Fzip%3D78705&clickType=listing' 

target = url1 
driver.get(target)

soup = BeautifulSoup(driver.page_source, "html.parser")

#print(soup.prettify())

def get_names(html_soup):
    basic_info = html_soup.find_all('div',attrs={'class':'container'})
    body = basic_info[1]
    
    nameCar = body.find('h1', attrs={'data-cmp':'heading'})
    title_nameCar= nameCar.get_text()

    return title_nameCar

def get_importantInfo(html_soup):
    import_info = []
    basic_info = html_soup.find_all('div',attrs={'class':'container'})
    body = basic_info[1]
    
    importInfo_lst = body.find_all('li')
    for item in importInfo_lst:
        import_info.append(item.text.strip())
    
    return import_info

def get_listingPrice(html_soup):
    #basic_info = html_soup.find_all('div',attrs={'data-cmp':'stickyContainer'})
    price = html_soup.find('span',attrs={'class':'first-price first-price-lg text-size-700'})
    list_price = price.get_text()
    
    return list_price

def get_sellerComments(html_soup):
    comment = html_soup.find_all('div',attrs={'data-cmp':'section'})
    print(comment)
    
    return comment 



print(get_names(soup))
print(get_importantInfo(soup))
print(get_listingPrice(soup))
#print(get_sellerComments(soup))

