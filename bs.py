from bs4 import BeautifulSoup
import requests


def soupify(url):
    page = requests.get(url)

    # Encodes the html into utf-8 then decodes it back to ascii
    page_text = page.text.encode('utf-8').decode('ascii', 'ignore')

    # Saves the encoded html into a Beautiful Soup object
    soup = BeautifulSoup(page_text, 'html.parser')

    return soup
