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
    

    # return content[0].find_all('span', attrs={'class': 'text'})[0].string
    return quote_tags
def get_url_authors():
    pass

def get_authors():
    pass

if __name__ == '__main__':
    quotes = get_quotes()
    print(quotes)
    