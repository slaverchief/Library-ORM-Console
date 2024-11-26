from exceptions import ObjectsDontExist, InvalidInput
from models import Book

def add(title: str, author: str, year: int) -> str:
    Book(title, author, year).save()
    return "Успешно"

def list_objects(**kwargs) -> list:
    return Book.list_objects(**kwargs)

def change_status(id: int) -> str:
    try:
        if not isinstance(id, int) or id < 0:
            raise InvalidInput("невалидный ID")
        b = Book.list_objects(id=id)[0]
        b.status = not b.status
        b.save()
        return "Успешно"
    except IndexError:
        raise ObjectsDontExist("несуществующий ID")

def delete(id: int) -> str:
    Book.get_by_id(id).delete()
    return "Успешно"