import requests
import sounds
from bs4 import BeautifulSoup

questionQueue = ["who","what","where","when"] # testing this as alternative on ALICE.run

def query(user_query):

    URL = "https://www.google.com/search?q=" + user_query.replace('search' , "")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36'
    }

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    try:
        # Highlighted Result
        result = soup.find(class_="Z0LcW CfV8xf").get_text()
        print(result)
        return result
    except AttributeError:
        try:
            # First Result
            result = soup.find(class_='qv3Wpe').get_text()
            print(result)
            return result
        except AttributeError:
            try:
                # Side Panel
                result = soup.find(class_="LGOjhe").get_text()  #
                print(result)
                return result
            except AttributeError:
                try:
                    # Side Panel 2
                    result = soup.find(class_="kno-rdesc").get_text()

                    print(result)
                    return result
                except:
                    return ("I'm Sorry. Please check a new source for result")





def calculate(equation):
    sounds.soundListening()
    URL = "https://www.google.com/search?q=" + equation.replace('alice', ' ')
    URL = "https://www.google.com/search?q=" + equation.replace('+', 'plus') # replacing "+" into plus to avoid conflicton url

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36'
    }

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    answer = soup.find(class_="qv3Wpe").get_text()
    question = soup.find(class_= "vUGUtc").get_text()
    feedback = question + answer

    print(feedback)
    return feedback

