import requests
from bs4 import BeautifulSoup
from typing import List

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
        quote['author'] = author.string
        quote['quote'] = text.string
        quote['tags'] = tags['content'].split(',')
        quotes.append(quote)
    
    return quotes

def get_url_authors():
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    author_links = soup.select('div[class=quote] span a')
    urls = []
    
    for link in author_links:
        urls.append(base_url + link['href'])

    return urls


def get_authors():
    pass

if __name__ == '__main__':
    quotes = get_quotes()
    urls = get_url_authors()
    print(urls)
    