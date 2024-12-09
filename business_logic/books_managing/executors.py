
from storages.non_relational.file.databases import JSONDB
from .models import Book

Book_unit = JSONDB.get_unit(Book)

def add_book(title: str, author: str, year: int) -> str:
    Book_unit.add_or_update_object(Book(title, author, year))
    return "Успешно"

def list_books(**kwargs) -> list:
    return Book_unit.list_objects(**kwargs)

def change_book_status(id: int) -> str:
    b = Book_unit.get_object(id)
    b.status = not b.status
    Book_unit.add_or_update_object(b)
    return "Успешно"

def delete_book(id: int) -> str:
    obj = Book_unit.get_object(id)
    Book_unit.delete_object(obj)
    return "Успешно"