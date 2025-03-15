
# NOTE: can use bright data subscription to bypass the captchas and IP blocking certain websites use against bots so we can scrape anything otherwise only certain websites will work

# Use streamlit to create an easy to use UI especially when working with LLM's
# Use Selenium(allows us to automate a web browser so we can nav to a webpage) to fetch data from the website that we want to scrape
# Grab all content on page then we can filter through it using an LLM
# So we can use that LLM to parse through the data to give us what we want

import streamlit as st
from scrape import scrape_website, split_dom_content, clean_body_content, extract_body_content
from parse import parse_with_ollama

st.title("AI Web Scraper")
url = st.text_input("Enter Website URL: ") #creates very basic text input box

if st.button("Scrape Site"):
    st.write("Scraping the website")
    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content

    #allows us to epand and view more content
    with st.expander("View DOM Content"): #kinda like a button that toggles what we are showing inside
        st.text_area("DOM Content", cleaned_content, height = 300) #expand the size 0f the content we want to display 


#need to ask the user for a prompt about what they want to view

if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse?")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content")

            dom_chunks = split_dom_content(st.session_state.dom_content) #take these as chunks and then we're gonna parse them in a LLM
            result = parse_with_ollama(dom_chunks, parse_description)
            st.write(result)