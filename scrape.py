# Scraping code in here, duh
# importing a few Selenium modules or classes that we need to use
# writing a function that takes website url and simply returns all the content from it

import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time


#function to grab content from a website using selenium. Selenium helps us control our browser to do things humans can do like click buttons and stuff like that

def scrape_website(website):
    print("launching browser...")

    chrome_driver_path = "./chromedriver.exe" #specify where driver is that allows us to control chrome
    options = webdriver.ChromeOptions() #specify how the chrome driver should operate
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options) #set up driver but could use something other than chrome


    try:
        driver.get(website) #use webdriver to go to website and grab the content
        print("Page loaded...")
        html = driver.page_source #grab the page source and then return
        time.sleep(10)

        return html
    finally:
        driver.quit()