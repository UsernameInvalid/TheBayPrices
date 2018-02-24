from db import connect
from bs import soupify


def itemCrawl():

    # Initilizes the db connection
    conn = connect()

    # Open SQL Cursor
    cur = conn.cursor()

    cur.execute('select brand_link from brands limit 1')
    rows = cur.fetchall()

    for url in rows:
        soup = soupify(url[0])
        print(soup.prettify())
