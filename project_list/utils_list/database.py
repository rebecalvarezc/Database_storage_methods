books = []


def book_structure(name: str, author: str, status: bool) -> dict:
    """
    Template to create a book that you want to store in a database.
    :param name: str
    :param author: str
    :param status: bool
    :return: dict
    """
    return {'name': name, 'author': author, 'status': status}


def add_book(name: str, author: str) -> bool:
    """
    function used to add a book to the database.
    :param name: str
    :param author: str
    :return: bool
    """
    book = book_structure(name, author, False)
    if book not in books:
        books.append(book)
        return True
    return False


def delete_book(name: str) -> None:
    """
    function used to remove a book from the database
    :param name: str
    :return: None
    """
    global books
    books = [book for book in books if book.get('name') != name]


def book_status(name: str, author: str) -> None:
    """
    function used to change the status of a book. True if it's read and False for unread.
    :param name: str
    :param author: str
    :return: None
    """
    global books
    books = [
        book_structure(name, author, True) if book.get('name') == name and book.get('author') == author else book
        for book in books]
