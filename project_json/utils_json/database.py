import json
import os
from typing import Union

STATUS = {True: 'Read', False: 'Unread'}

database_name = 'rebeca_library.json'


def data_structure(book_id: Union[str, int], name: str, author: str, status: bool) -> dict:
    """
    Template that creates the structure of the book.
    :param book_id: Union[str, int]
    :param name: str
    :param author: str
    :param status: bool
    :return: dict
    """
    return {
        book_id:
            {
                'name': name,
                'author': author,
                'status': STATUS[status]
            }
    }


def create_database() -> None:
    """
    This function creates the json file in case it does not exists.
    :return: None
    """
    if not os.path.exists(database_name):
        with open(database_name, 'w', encoding='utf-8') as file:
            json.dump([], file)  # arreglo vacío  # fp = file pointer


def save_all_books(books: list[dict]) -> None:
    """
    This function saves the iterable information in the json file.
    :param books: list[dict]
    :return: None
    """
    with open(database_name, 'w', encoding='utf-8') as file:
        json.dump(books, file)


def open_library() -> list[dict]:
    """
    This function saves all the objects in the json and introduces them in a list.
    :return: list[dict]
    """
    with open(database_name, 'r', encoding='utf-8') as all_books:
        books = json.load(all_books)
    return books


def add_book(name: str, author: str) -> bool:
    """
    This function allows the user to add a book to the json file.
    :param name: str
    :param author: str
    :return: bool
    """
    books = open_library()
    book_id = len(books) + 1
    book_exists = [data_structure(str(index), name, author, status) in books for status in (True, False)
                   for index, _ in enumerate(books, start=1)]
    if not any(book_exists):
        books.append({book_id: {'name': name, 'author': author, 'status': STATUS[False]}})
        save_all_books(books)
        return True
    return False


def book_status(book_id: str) -> bool:
    """
    This function allows the user to change the status of a book from 'Read' to 'Unread'.
    It stores the changed book in the json file.
    :param book_id: str
    :return: bool
    """
    books = open_library()
    for book in books:
        if book.get(book_id):
            book[book_id]['status'] = STATUS[True]
            save_all_books(books)
            return True
    return False


def delete_book(book_id: str) -> None:
    """
    This function allows the user to remove a book from the json file by rewriting it.
    :param book_id: str
    :return: None
    """
    books = open_library()
    books = [book for book in books if book_id not in book.keys()]
    save_all_books(books)
