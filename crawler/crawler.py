# -*- coding: utf-8 -*-

import os
import csv
import requests
from bs4 import BeautifulSoup

def request(url):
    req = requests.get(url)

    if req.status_code != 200:
        return None

    try:
        html_doc = req.text
    except:
        raise("There's some problem in retrieving html document")

    return html_doc

def crawl(url):
    html_doc = request(url)

    soup = BeautifulSoup(html_doc, "html.parser")
    table = soup.find('table')
    urls = table.find_all('a')
    hrefs = [url.get('href') for url in urls if url.get('href') is not None]
    hrefs = set(hrefs)
    fighters = [get_fighter(href) for href in hrefs]
    return fighters

def get_fighter(link):
    fighter = {}

    html_doc = request(link)
    soup = BeautifulSoup(html_doc, "html.parser")
    name = soup.find('span', {'class':'b-content__title-highlight'}).text
    name = name.strip()

    fighter['name'] = name

    ## continuar...

def main(letter):
    url = "http://www.fightmetric.com/statistics/fighters?char={}&page=all".format(letter)
    crawl(url)

if __name__ == '__main__':
    letter = u'a'
    main(letter)
