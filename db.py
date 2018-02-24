import psycopg2
from urllib.parse import urlparse


def connect():
    # Parses the ElephantSQL Url into connection peices
    url = urlparse("postgres://suhfoclo:8pCChYhwpfwzUaKdmbc11onFwK79-4hF@baasu.db.elephantsql.com:5432/suhfoclo")

    # Initializes Database Connection
    conn = psycopg2.connect(database=url.path[1:],
                            user=url.username,
                            password=url.password,
                            host=url.hostname,
                            port=url.port
                            )
    return conn

