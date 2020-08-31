from bs4 import BeautifulSoup
from html.parser import HTMLParser
import requests

#returns a link to the closest result of the game searched on the steam store.
def steam_search(item):
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
    item = item.replace(' ', '+')
    my_url = "https://store.steampowered.com/search/?term=" + item
    req = requests.get(my_url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    for match in soup.find_all('div', id='search_resultsRows'):
        price = match.a.find('div', class_='col search_price_discount_combined responsive_secondrow')
        price = (price.text.strip())
        price = "Price: " + price[-5:]
        new = match.a.get('href')
        return new

#returns the price that goes with the game.
def steam_search_price(item):
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
    item = item.replace(' ', '+')
    my_url = "https://store.steampowered.com/search/?term=" + item
    req = requests.get(my_url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    for match in soup.find_all('div', id='search_resultsRows'):
        price = match.a.find('div', class_='col search_price_discount_combined responsive_secondrow')
        price = (price.text.strip())
        price = "Price: " + price[-5:]
        new = match.a.get('href')
        return price
