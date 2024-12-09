from .executors import *
from core.exceptions import *

def add_book_handler() -> str:
    try:
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        year = int(input("Введите год выпуска книги: "))
    except ValueError:
        raise InvalidInput("введен невалидный год")
    return add_book(title, author, year)

def list_books_handler() -> str:
    print('Далее вам надо ввести поля поиска, оставьте их пустыми, если они вам не важны.')
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")
    year = input("Введите год выпуска книги: ")
    kwargs = {}
    if title:
        kwargs['title'] = title
    if author:
        kwargs['author'] = author
    if year:
        try:
            kwargs['year'] = int(year)
            if kwargs['year'] <= 0:
                raise ValueError
        except ValueError:
            raise InvalidInput("вы указали невалидный год книги")
    return_str = ''
    for book in list_books(**kwargs):
        return_str += str(book) + '\n'
    return return_str

def change_book_status_handler() -> str:
    try:
        id = int(input("Введите id книги, для которой вы меняете статус: "))
        return change_book_status(id)
    except ValueError:
        raise InvalidInput("невалидный id книги")


def delete_book_handler() -> str:
    try:
        id = int(input("Введите id книги, которую вы удаляете: "))
        return delete_book(id)
    except ValueError:
        raise InvalidInput("невалидный id книги")