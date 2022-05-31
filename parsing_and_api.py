import random
import requests
from bs4 import BeautifulSoup
from keyboa import Keyboa

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}

def keyboard(button_list):
    keyboard = Keyboa(items=button_list, copy_text_to_callback=True, items_in_row=2)
    return keyboard()


def get_api():
    data = requests.get("https://imdb-api.com/en/API/Top250Movies/k_zz6dmkqw").json()
    return data

def parsing():
    data = requests.get("https://citaty.info/random").text
    soup = BeautifulSoup(data, "html5lib")
    qout = soup.find("p")
    return qout.text

