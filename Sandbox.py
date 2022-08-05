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


# Final Code
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
                    print("Check a new source for result")




while True:

    query()
   # except Exception:
 #       print('Sorry no result, please be clear')
