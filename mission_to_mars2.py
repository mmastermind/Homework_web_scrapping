from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

# Dictionary to upload scrapped info and export it later to Mongo
mars_data={}

# Functions to be called by the app to get data from different URL's

def scrape_header():
    browser = init_browser()

    # Visit mars.nasa.gov/news
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"

    browser.visit(url)
    time.sleep(0)
    # Scrape page into Soup
    html = browser.html   
    try:
        soup = bs(html, "html.parser")
        header = soup.find("li", class_="slide").find("div", class_="content_title").text
        news = soup.find("li", class_="slide").find("div", class_="article_teaser_body").text
        mars_data['Header'] = header
        mars_data['Paragraph'] = news

    except NameError:
        pass
    
    browser.quit()
    return mars_data
    

def scrape_weather():
    browser = init_browser()

    # Visit tweeter for Mars Weather report
    url = "https://twitter.com/MarsWxReport?lang=en"

    browser.visit(url)
    time.sleep(0)
    # Scrape page into Soup
    html = browser.html   
    try:
        soup = bs(html, "html.parser")
        tweet = soup.find("ol", class_="stream_items")
        weather = soup.find("p", class_="tweet-text").text
        mars_data['tweeter'] = tweet
        mars_data['weather'] = weather

    except NameError:
        pass

    browser.quit()
    return mars_data
    

def scrape_jpl():
    browser = init_browser()

    # Visit jpl.nasa.gov for Mars featured image
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"

    browser.visit(url)
    time.sleep(0)
    # Scrape page into Soup
    html = browser.html   
    try:
        soup = bs(html, "html.parser")
        jpl = soup.find('article')['style'].replace('background-image: url(','').replace(');','')[1:-1]
        home_url = "https://www.jpl.nasa.gov"
        full_url = home_url + jpl
        mars_data['jpl_image'] = full_url

    except NameError:
        pass

    browser.quit()
    return mars_data
    

def scrape_quadrants():
    browser = init_browser()

    # Visit astrogeology.usgs.gov for Mars featured image
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    time.sleep(0)   
    
    pages_urls = []
    # sub_pages = browser.find_by_css("a.product-item h3")
    for page in range(4):
        quadrants = {}
        browser.find_by_css("a.product-item h3")[page].click()
        img_smp = browser.find_link_by_text("Sample").first
        quadrants["quad_url"] = img_smp["href"]
        quadrants["title"] = browser.find_by_css("h2.title").text
        pages_urls.append(quadrants)
        browser.back()
        
    mars_data["Hemispheres"] = pages_urls
    browser.quit()
    return mars_data
    

    