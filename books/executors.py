
from main.databases import JSONDB
from .models import Book

Book_DB = JSONDB(Book)

def add_book(title: str, author: str, year: int) -> str:
    Book_DB.add_or_update_object(Book(title, author, year))
    return "Успешно"

def list_books(**kwargs) -> list:
    return Book_DB.list_objects(**kwargs)

def change_book_status(id: int) -> str:
    b = Book_DB.get_object(id)
    b.status = not b.status
    Book_DB.add_or_update_object(b)
    return "Успешно"

def delete_book(id: int) -> str:
    obj = Book_DB.get_object(id)
    Book_DB.delete_object(obj)
    return "Успешно"