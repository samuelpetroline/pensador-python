import requests
from .exceptions import PensadorQueryException
from requests import RequestException
from bs4 import BeautifulSoup

class Query(object):

    def __init__(self):
        self.url = 'https://www.pensador.com'

    def get_author(self, author, page):

        try:
            query = 'autor/{0}/{1}'.format(author, page)

            return self.get(query)
        except Exception as ex:
            raise ex

    def get_quote(self, quote, page):

        try:
            query = '/{0}/{1}'.format(quote, page)

            return self.get(query)
        except Exception as ex:
            raise ex

    def get(self, query):

        try:
            url = '{0}/{1}'.format(self.url, query)
            page = requests.get(url)
        except RequestException as ex:
            raise PensadorQueryException('Error requesting data', page.status_code)
        except Exception as ex:
            raise ex

        return BeautifulSoup(page.text, 'html.parser')

