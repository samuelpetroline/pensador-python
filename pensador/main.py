
from .query import Query
from .models import Quote, QuoteList
from .utils import clear_tags, get_string_nested
from .exceptions import PensadorException, PensadorQueryException

from bs4 import BeautifulSoup
import unidecode

class Pensador(object):

    def __init__(self):
        self.query = Query()

    def quote(self, query, page=1, limit=8):
        try:
            self.__validate_query(query)

            content = self.query.get_quote(query, page)

            quote_list = content.find(class_='phrases-list')
            if quote_list is None:
                return QuoteList(None, 0, 0)

            current_page, max_page = self.__extract_pagination(quote_list)
            quotes = self.__extract_quotes(quote_list, limit)

            return QuoteList(quotes, current_page, max_page)
        except Exception as ex:
            raise ex

        return content

    def author(self, author, page=1, limit=8):
        try:
            self.__validate_query(author)

            formatted_author = author.replace(' ', '_')
            formatted_author = formatted_author.lower()
            formatted_author = unidecode.unidecode(formatted_author)

            content = self.query.get_author(formatted_author, page)

            quote_list = content.find(class_='phrases-list')
            if quote_list is None:
                return QuoteList(None, 0, 0)

            current_page, max_page = self.__extract_pagination(quote_list)
            quotes = self.__extract_quotes(quote_list, limit)

            return QuoteList(quotes, current_page, max_page)
        except Exception as ex:
            raise ex

        return content

    def __validate_query(self, query):
        if query is None or len(query) == 0:
            raise PensadorException('Invalid query format')

    def __extract_quotes(self, content, limit):
        quote_list = content.find_all(class_='thought-card')

        quote_list = quote_list[:limit]

        quotes = list()
        for item in quote_list:
            quote = get_string_nested(clear_tags(item.find(class_='frase'), 'br'), 'p')
            author = get_string_nested(item.find(class_='autor'), 'a')
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
            max_page = int(max_page_tag[-1].getText())

            current_page_tag = pagination_content.find(class_='atual')
            current_page = int(current_page_tag.getText())

        return current_page, max_page


