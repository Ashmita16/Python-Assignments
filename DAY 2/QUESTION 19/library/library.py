import books
import users
from exceptions import NotFoundError, BookNotAvailableError, BookNotIssuedError

def issue_book(book_id: int, user_id: int):
    user = users.find_user_by_id(user_id)
    if not user:
        raise NotFoundError(f"User with ID {user_id} does not exist")
    
    book = books.find_book_by_id(book_id)
    if not book:
        raise NotFoundError(f"Book with ID {book_id} does not exist")
    
    if not book["available"]:
        raise BookNotAvailableError(f"Book '{book['title']}' is currently issued")
    
    book["available"] = False
    book["issued_to"] = user_id

def return_book(book_id: int):
    book = books.find_book_by_id(book_id)
    if not book:
        raise NotFoundError(f"Book with ID {book_id} does not exist")
    
    if book["available"]:
        raise BookNotIssuedError(f"Book '{book['title']}' is not currently issued")
    
    book["available"] = True
    book["issued_to"] = None

def get_available_books():
    return [b for b in books.books if b["available"]]

def get_issued_books():
    return [b for b in books.books if not b["available"]]
