from .exceptions import PensadorQueryException
import requests
from bs4 import BeautifulSoup

class Query(object):

    def __init__(self):
        self.url = 'https://www.pensador.com/busca.php'

    def get(self, query):

        try:
            page = requests.get(self.url, params={'q': query})

            page.raise_for_status()
        except:
            if page.text and len(page.text) > 0 and page.text != 'null':
                raise PensadorQueryException('{0}: {1}'.format(page.url, page.json()['error']['message']), page.status_code)

            raise PensadorQueryException('{0}: {1}'.format(page.url, 'error'), page.status_code)

        return BeautifulSoup(page.text, 'html.parser')

