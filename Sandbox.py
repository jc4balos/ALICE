import requests
from bs4 import BeautifulSoup


def query():
    user_query = input('Enter your query: ')

    URL = "https://www.google.com/search?q=" + user_query

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36'
    }

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find(class_='qv3Wpe').get_text()
    print(result)


while True:
    try:
        query()
    except Exception:
        print('Sorry no result, please be clear')
