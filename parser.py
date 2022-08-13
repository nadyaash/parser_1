import requests, lxml
from bs4 import BeautifulSoup
from time import sleep
from userdata import HEADERS

headers = HEADERS

def get_url():
    for number_page in range(1, 8):

        url = f'https://scrapingclub.com/exercise/list_basic/?page={number_page}'
        try:
            response = requests.get(url, headers=headers, timeout=5)
            soup = BeautifulSoup(response.text, 'lxml')
            data = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

            for i in data:
                card_url = 'https://scrapingclub.com' + i.find('a').get('href')
                yield card_url
        except requests.RequestException as e:
            print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
            print(str(e))


def get_data():
    for card_url in get_url():
        try:
            response = requests.get(card_url, headers=headers, timeout=5)
            sleep(3)
            soup = BeautifulSoup(response.text, 'lxml')

            data = soup.find('div', class_='card mt-4 my-4')
            name = data.find('h3', class_='card-title').text.strip()
            price = data.find('h4').text.strip()
            text = data.find('p', class_='card-text').text.strip()
            img_url = 'https://scrapingclub.com' + data.find('img', class_='card-img-top img-fluid').get('src')
            yield name, price,text, img_url

        # Exceptions
        except requests.ConnectionError as e:
            print("OOPS!! Connection Error. Make sure you are connected to Internet. Technical Details given below.\n")
            print(str(e))
        except requests.Timeout as e:
            print("OOPS!! Timeout Error")
            print(str(e))
        except requests.RequestException as e:
            print("OOPS!! General Error")
            print(str(e))
        except KeyboardInterrupt:
            print("Someone closed the program")
