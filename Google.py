import requests
import sounds
from bs4 import BeautifulSoup

questionQueue = ["who","what","where","when"] # testing this as alternative on ALICE.run

def query(user_query):

    URL = "https://www.google.com/search?q=" + user_query

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36'
    }

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find(class_='LGOjhe').get_text()
    print(result)
    return result


def calculate(equation):
    sounds.soundListening()
    URL = "https://www.google.com/search?q=" + equation.replace('calculate', ' ')

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36'
    }

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    answer = soup.find(class_='qv3Wpe').get_text()

    print(answer)
    return answer

# year of first fifa world cup
# age of ronaldo
# height of burj khalifa
# when was leonardo di vinci born
# prime minister of uk
# what is the weight of earth