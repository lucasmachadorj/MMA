# -*- coding: utf-8 -*-

import csv
import requests
from bs4 import BeautifulSoup

def crawl(url):
    req = requests.get(url)

    if req.status_code != 200:
        return None

    try:
        html_doc = req.text
    except:
        raise("There's some problem in retrieving html document")

    soup = BeautifulSoup(html_doc, 'html.parser')
    urls = soup.table.find_all('a')
    hrefs = [url.get('href') for url in urls if url.get('href') is not None]

    names = []
    for href in hrefs:
        split_href = href.split('/')
        name = split_href[-1]
        name = name.replace('-', ' ')
        names.append(name)

    with open('fighters.csv', 'w') as fighterfile:
        fieldnames = ['full_name']
        writer = csv.DictWriter(fighterfile, fieldnames=fieldnames)

        writer.writeheader()
        for name in names:
            print(name)
            writer.writerow({'full_name': name})

def main():
    url = "http://espn.go.com/mma/fighters"
    crawl(url)

if __name__ == '__main__':
    main()
