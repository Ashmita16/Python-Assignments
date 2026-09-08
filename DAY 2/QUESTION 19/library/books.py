from exceptions import DuplicateIDError, NotFoundError, BookNotIssuedError
books = [
    {
        "id": 1,
        "title": "Inglorious Empire",
        "author": "Sashi Tharoor",
        "available": True,
        "issued_to": None
    }
]

def add_book(book_id: int, title: str, author: str):
    if any(b['id'] == book_id for b in books):
        raise DuplicateIDError(f"Book with ID {book_id} already exists")
    
    books.append({
        "id": book_id,
        "title": title,
        "author": author,
        "available": True,
        "issued_to": None
    })

def remove_book(book_id: int):
    book = find_book_by_id(book_id)
    if not book:
        raise NotFoundError(f"Book with ID {book_id} not found")
    if not book["available"]:
        raise BookNotIssuedError("Cannot remove a book that is currently issued")
    
    books.remove(book)

def search_books(query: str):
    query = query.lower()
    return [
        b for b in books 
        if query in b["title"].lower() or query in b["author"].lower() or str(b["id"]) == query
    ]

def find_book_by_id(book_id: int):
    for b in books:
        if b["id"] == book_id:
            return b
    return None
