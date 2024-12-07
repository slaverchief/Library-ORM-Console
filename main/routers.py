from books.handlers import *
from books.routers import catch as book_router
from .exceptions import InvalidPrompt

MODELS_LIST = ['book']

def manage_command():
    command = input(f"Введите одну из следующих комманд: "
                    f"{['' + command for command in MODELS_LIST]} ")
    if command not in MODELS_LIST:
        raise InvalidPrompt("введенная вами команда не предусмотрена")
    if command == 'book':
        return book_router()
