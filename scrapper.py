import json

import requests

from bs4 import BeautifulSoup

class Scrapper(object):

    def __init__(self):
        self.url = "https://www.standardmedia.co.ke"

    def scrape_website(self):
        # the method that scrapes the website

        # first ping the requested url and check the response
        response = requests.get(self.url)
        return response

scraper = Scrapper()
print(scraper.scrape_website())
            
