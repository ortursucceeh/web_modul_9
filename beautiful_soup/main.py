import json
from typing import List, Set
from datetime import datetime

import requests
from bs4 import BeautifulSoup


base_url = "http://quotes.toscrape.com"



def get_quotes() -> List[dict]:
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quote_author = soup.select('div[class=quote] small[class=author]')
    quote_text = soup.select('div[class=quote] span[class=text]')
    quote_tags = soup.select('div[class=quote] div[class=tags] meta')
    quotes = []

    for author, text, tags in zip(quote_author, quote_text, quote_tags):
        quote = {}

        quote['tags'] = tags['content'].split(',')
        quote['author'] = author.text
        print(author.text)
        quote['quote'] = text.text

        quotes.append(quote)
    
    return quotes

def get_url_authors() -> Set[str]:
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    author_links = soup.select('div[class=quote] span a')
    urls = []
    
    for link in author_links:
        urls.append(base_url + link['href'])

    return set(urls)


def get_authors(urls: Set[str]):
    authors = []
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        

        fullname = soup.select('h3[class=author-title]')
        born_date = soup.select('span[class=author-born-date]')[0].text
        born_location = soup.select('span[class=author-born-location]')[0].text
        description = soup.select('div[class=author-description]')[0].text
        author = {}
        author['fullname'] = fullname
        author['born_date'] = datetime.strptime(born_date, "%B %d, %Y").isoformat()
        author['born_location'] = born_location
        author['description'] = description.strip()

        authors.append(author)

    return authors

def load_in_json(filename: str, data: List[dict]):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)



    

if __name__ == '__main__':
    quotes = get_quotes()
    urls = get_url_authors()
    authors = get_authors(urls)
    load_in_json('authors.json', authors)
    load_in_json('quotes.json', quotes)
    # print(quotes)