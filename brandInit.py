import psycopg2
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from db import connect
from bs import soupify

def all_brand_insert():
    # Request the html from the brands page
    soup = soupify('http://www.thebay.com/webapp/wcs/stores/servlet/en/HBCBrandsListView?storeId=10701&catalogId=10652&langId=-24')

    # Initializes a array for the all urls
    itemUrls = []
    itemNames = []
    # All brand columns are in divs with class byword
    brandColumns = soup.find_all(class_='byword')
    # For each of the 6 brand columns...
    for column in brandColumns:

        # ...find the a tag within...
        for item in column.find_all('a'):
            # ... and add the link to the brandColumns array
            itemUrls.append(item['href'])
            itemNames.append(item.text)

    # Creates connection
    conn = connect()

    # Opens SQL Cursor
    cur = conn.cursor()

    # Clears Table
    cur.execute("delete from brands")

    # Sets up insert statement
    insert = "insert into brands (brand_name, brand_link) values (%s, %s)"

    # For every item...
    for i, brand in enumerate(itemUrls):
        # ...Set values equal to name and url and...
        values = [itemNames[i], itemUrls[i]]
        # ...insert into table
        cur.execute(insert, tuple(values))

        print("Inserting {} into table".format(itemNames[i]))

    # Commits all actions
    conn.commit()

    # Closes database connection
    conn.close()
