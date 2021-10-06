from utils_files import database
import pprint
import os
os.system('cls')
USER_OPTIONS = '''
- Introduce "a" to add a new book.
- Introduce "l" to show all stored books.
- Introduce "r" to change the status of a book to read.
- Introduce "d" to remove a book from storage.
- Introduce "q" para stop the program.

Your option: --> '''


def menu():
    while (user_input := input(USER_OPTIONS)) != "q":
        os.system('cls')
        if user_input == 'a':
            database.create_database()
            name = input("Write the name of the book: ").title()
            author = input("Write the name of the author: ").title()
            status = database.add_book(name, author)
            if not status:
                print('The book you wish to add is already on storage!')

        elif user_input == 'l':
            pprint.pprint(database.all_books())

        elif user_input == 'r':
            pprint.pprint(database.all_books())
            book_id = input('Write the ID of the book you have read: ').title()
            status = database.book_status(book_id)
            if not status:
                print('The book you indicated is not on the list.')
            else:
                print('The book status has been changed to "read" :)')

        elif user_input == 'd':
            pprint.pprint(database.all_books())
            while True:
                try:
                    book_id = int(input('Enter the ID of the book you want to remove: '))
                    database.delete_book(book_id)
                    break
                except ValueError:
                    print('Error. Write the book ID.')
                    continue
            print('Book removed successfully :)')
        else:
            print("Please enter a valid option!")

    print('Goodbye :)')


if __name__ == '__main__':
    menu()
