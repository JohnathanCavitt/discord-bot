from bs4 import BeautifulSoup
from html.parser import HTMLParser
import requests

#returns the newest league of legends patch notes summary
def lol_patch():
    list_to_print = []
    list_of_links = []
    # set headers
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
    my_url = "https://na.leagueoflegends.com/en-us/news/game-updates/"
    # get web page
    # make BeautifulSoup object that contains html from web page
    req = requests.get(my_url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    for match in soup.find_all('li', class_='style__Item-sc-3mnuh-3 ekxbJn'):
        word = "https://"
        word2 = "en-us"
        newlink = match.a.get('href')
        if word2 in match.a.get('href'):
            newlink = "na.leagueoflegends.com" + newlink
        if word in match.a.get('href'):
            newlink = newlink.replace(word, "")
        newlink = word + newlink
        if "patch" in newlink and "teamfight" not in newlink:
            list_of_links.append(newlink)
    
    new_url = list_of_links[0]
    new_req = requests.get(new_url, headers)
    new_soup = BeautifulSoup(new_req.content, 'html.parser')
    print("\n")
    for champ in new_soup.find_all('div', class_='content-border'):
        try:
            champ_name = champ.find('h3', class_='change-title').text
            champ_summary = champ.find('p', class_='summary').text
        except Exception as e:
            champ_name = None
            champ_summary = None
        if champ_name is not None:
            list_to_print.append(champ_name + ": " + champ_summary)
            

    return list_to_print



#returns the link that goes with the patch notes.
def lol_patch_link():
    list_to_print = []
    list_of_links = []
    link_to_print = []
    # set headers
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'})
    my_url = "https://na.leagueoflegends.com/en-us/news/game-updates/"
    # get web page
    # make BeautifulSoup object that contains html from web page
    req = requests.get(my_url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    for match in soup.find_all('li', class_='style__Item-sc-3mnuh-3 ekxbJn'):
        word = "https://"
        word2 = "en-us"
        newlink = match.a.get('href')
        if word2 in match.a.get('href'):
            newlink = "na.leagueoflegends.com" + newlink
        if word in match.a.get('href'):
            newlink = newlink.replace(word, "")
        newlink = word + newlink
        if "patch" in newlink and "teamfight" not in newlink:
            list_of_links.append(newlink)

    link_to_print.append(list_of_links[0])
    return link_to_print
