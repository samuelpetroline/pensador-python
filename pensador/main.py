
from .query import Query
from .models import Quote, QuoteList
from .exceptions import PensadorException, PensadorQueryException

from bs4 import BeautifulSoup

class Pensador(object):

    def __init__(self):
        self.query = Query()

    def quote(self, query, page=1, limit=8):
        self.__validate_query(query)

        try:
            content = self.query.get(query)

            quote_list = content.find(class_='phrases-list')
            if quote_list is None:
                return QuoteList(None, 0, 0)

            current_page, max_page = self.__extract_pagination(quote_list)
            quotes = self.__extract_quotes(quote_list)

            return QuoteList(quotes, current_page, max_page)
        except Exception as ex:
            raise ex

        return content

    def __validate_query(self, query):
        if query is None or len(query) == 0:
            raise PensadorException('Invalid query format')

    def __extract_quotes(self, content):
        quote_list = content.find_all(class_='thought-card')

        quotes = list()
        for item in quote_list:
            quote = item.find(class_='frase').string
            author = item.find(class_='autor').find('a').string
            image = item.attrs['data-src'] or None

            quotes.append(Quote(quote, author, image))

        return quotes

    def __extract_pagination(self, content):
        current_page = 1
        max_page = 1

        pagination_content = content.find(id='paginacao')
        if pagination_content != None:
            # print([(lambda tag: tag.name == 'a' and not tag.has_attr('class'))(tag) for tag in page_tags])

            max_page_tag = pagination_content.find_all(class_= None)
            max_page = int(max_page_tag[-1].string)

            current_page_tag = pagination_content.find(class_='atual')
            current_page = int(current_page_tag.string)

        return current_page, max_page


