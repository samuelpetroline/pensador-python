class PensadorException(Exception):
    def __init__(self, message):
        self.message = message

class PensadorQueryException(PensadorException):
    def __init__(self, message, http_code):
        super().__init__(message)

        self.http_code = http_code