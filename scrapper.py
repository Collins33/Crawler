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
        # parse the contents of the response into html
        html = BeautifulSoup(response.content, 'html.parser')
        if html :
            # get all div tags with the class col-xs-6 col-md-6 zero
            div = html.find('div', class_='col-xs-6 col-md-6 zero')
            ul = div.find_all('ul', class_='sub-stories-2')
            data = []
            for item in ul:
                image_url = item.find('img').get('src')
                text = item.find('img').get('alt')
                link = item.find('li').find('a').get('href')
            data.append({
                'image':image_url,
                'text': text,
                'link': link
            })
            return json.dumps(data, indent=2)    
            





scraper = Scrapper()
print(scraper.scrape_website())
            
