
# NOTE: can use bright data subscription to bypass the captchas and IP blocking certain websites use against bots so we can scrape anything otherwise only certain websites will work

# Use streamlit to create an easy to use UI especially when working with LLM's
# Use Selenium(allows us to automate a web browser so we can nav to a webpage) to fetch data from the website that we want to scrape
# Grab all content on page then we can filter through it using an LLM
# So we can use that LLM to parse through the data to give us what we want

import streamlit as st
from scrape import scrape_website

st.title("AI Web Scraper")
url = st.text_input("Enter Website URL: ") #creates very basic text input box

if st.button("Scrape Site"):
    st.write("Scraping the website")
    result = scrape_website(url)
    print(result)
