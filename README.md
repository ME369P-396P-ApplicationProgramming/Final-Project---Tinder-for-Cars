# Final-Project---Tinder-for-Cars

This will create a web application that will display cars in surrounding areas that can be 'liked' based on some preset parameters. Here is a link for our product presentation, that goes through the most important concepts of this project: https://docs.google.com/presentation/d/1kLDLlC_wndEY2eSFbvtL4KMPevXhRjZ9/edit#slide=id.p1

# About the GitHub

Building this application has been challenging, and the group went through a lot of different versions of code. Within the main branch older pieces of code can be found, to see the developement, this might not be relavant. But to see and use the right application the "Final" folder, should be used.

# Members

Hannah Long, Rohith Maturi, Kevin Nguyen, Emil Søeberg

# Overview

You are looking for a new car and you have no idea what you want! Based on your location and budget, our application will help you find the perfect car. Our application scrapes car data from AutoTrader, and presents it in a "Tinder" fashioned manner. The application will present you with cars until enough information is gathered to conduct an analysis on your preferences. The user has the option to continue swipping to make a more precise analysis or get their best match after only five liked cars. 

# Packages

BeatifulSoup4, Numpy, Statistics, Math, Streamlit, Request

# How to run Application

  1. Download zip file from this repository
  2. Make sure all files from the "Final" Folder are in the same folder
  3. Open up "Cartest.py"
  4. To run application, enter streamlit run Cartest.py in terminal

# Challenges and Future Steps
  
  1. Scrape and aggregate more website and data (including carfax) + include other vehicle options
  2. Use more robust code, speed up scraping, and more accurate data algorithms
  3. Refine GUI interface design and make it more user friendly

# Architecture
  
The code consist of "Cartest.py", which runs the code, the "Backend_logic.py", which stores the functions used for the backend, and the different GUI pages is found in the folder "Pages", one for liking, one for storing. A functional programming approach is used for running the logic behind the code.
