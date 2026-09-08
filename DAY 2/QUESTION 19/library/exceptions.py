class LibraryException(Exception):
    pass

class DuplicateIDError(LibraryException):
    pass

class NotFoundError(LibraryException):
    pass

class BookNotAvailableError(LibraryException):
    pass

class BookNotIssuedError(LibraryException):
    pass

class InvalidInputError(LibraryException):
    pass
