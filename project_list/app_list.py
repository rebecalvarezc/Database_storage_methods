from utils_list import database
import pprint

USER_OPTIONS = '''
- Introduce "a" to add a new book.
- Introduce "l" to show all stored books.
- Introduce "r" to change the status of a book to read.
- Introduce "d" to remove a book from storage.
- Introduce "q" para stop the program.

Your option: --> '''


def menu():
    while (user_input := input(USER_OPTIONS)) != "q":
        if user_input == 'a':
            name = input("Write the name of the book: ")
            author = input("Write the name of the author: ")
            status = database.add_book(name, author)
            if status:
                print('The book has been stored :)')
            else:
                print('This book is already in storage.')

        elif user_input == 'l':
            pprint.pprint(database.books)

        elif user_input == 'r':
            name = input('Write the name of the book you have read: ')
            author = input('Write the name of the author of the read book: ')
            database.book_status(name, author)
            print(f'\nThe status of {name} has been changed :)!')

        elif user_input == 'd':
            name = input('Enter the name of the book you want to remove: ')
            database.delete_book(name)
            print('The book has been removed successfully :)!')

        else:
            print("Please, enter a valid option!")

    print('Goodbye :)')


if __name__ == '__main__':
    menu()
