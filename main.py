from time import sleep

from selenium import webdriver

from data import *

import requests
from bs4 import BeautifulSoup as b

URL = 'https://steamcommunity.com/market/search?l=russian&appid=570'

def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    items = soup.find_all('span', class_ = 'market_listing_item_name')
    return[c.text for c in items]

class SteamBot:
    def __init__(self):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path = r'C:\Users\Admin\Desktop\geckodriver.exe')
    def close_browser(self):
        self.driver.close()
        self.driver.quit()

    def log_into_steam(self):
        driver = self.driver
        driver.get(steam_link)
        driver.implicitly_wait(10)
        
        driver.find_element_by_class_name('global_action_link').click()
        sleep(10)
        