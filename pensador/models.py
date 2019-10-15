class QuoteList(object):
    def __init__(self, quotes, page, max_page):
        self.quotes = quotes
        self.page = page
        self.max_page = max_page

class Quote(object):
    def __init__(self, quote, author, image=None):
        self.quote = quote.strip()
        self.author = author.strip()
        self.image = image