# Scraping code in here, duh
# importing a few Selenium modules or classes that we need to use
# writing a function that takes website url and simply returns all the content from it. If using bright data we can bypass recaptcha and websites that block bots


from bs4 import BeautifulSoup
from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By
AUTH = 'brd-customer-hl_dce554b1-zone-ai_scraper:lx3z6ye36o58'
SBR_WEBDRIVER = f'https://{AUTH}@brd.superproxy.io:9515'

#function to grab content from a website using selenium. Selenium helps us control our browser to do things humans can do like click buttons and stuff like that

def scrape_website(website):
    print("launching browser...")

    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        driver.get(website)
        print('Taking page screenshot to file page.png')
        driver.get_screenshot_as_file('./page.png')
        print('Navigated! Scraping page content...')
        html = driver.page_source
        return html

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""


def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()                       #looks inside our parsed content for any script or style and remove them.

    cleaned_content = soup.get_text(separator="\n")  #get all text and separate it with new line
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip()) #code to remove any backslash n character that are unnecessary

    return cleaned_content


# need to split text into a bunch of seperate batches of what the max size is so we dont exceed the LLM character limit(token limit)

def split_dom_content(dom_content, max_length = 6000):
    return [
        dom_content[i: i + max_length] for i in range(0, len(dom_content), max_length)
    ]

#if __name__ == '__main__':
    #scrape_website()