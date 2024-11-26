from executors import *
from exceptions import *

def add_book() -> str:
    try:
        return add(title = input("Введите название книги: "),
                   author = input("Введите автора книги: "),
                   year = int(input("Введите год выпуска книги: ")))
    except ValueError:
        raise InvalidInput("введен невалидный год")

def list_book_objects() -> str:
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
    for book in Book.list_objects(**kwargs):
        return_str += str(book) + '\n'
    return return_str

def change_book_status() -> str:
    try:
        id = int(input("Введите id книги, для которой вы меняете статус: "))
        return change_status(id)
    except ValueError:
        raise InvalidInput("невалидный id книги")


def delete_book() -> str:
    try:
        id = int(input("Введите id книги, которую вы удаляете: "))
        return delete(id)
    except ValueError:
        raise InvalidInput("невалидный id книги")