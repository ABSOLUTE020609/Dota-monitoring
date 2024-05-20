import requests
from bs4 import BeautifulSoup as b

URL = 'https://steamcommunity.com/market/search?l=russian&appid=570'

def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    items = soup.find_all('span', class_ = 'market_listing_item_name')
    return[c.text for c in items]

