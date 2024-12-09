from .handlers import *
from .decorators import catch_exceptions

ALLOWED_COMMAND_LIST = ['add', 'list', 'change_status', 'delete', 'switch_model']

def catch():
    while True:
        res = manage_command()
        if res:
            if res == -1:
                break
        print(res)
@catch_exceptions
def manage_command():
    while True:
        command = input(f"Введите одну из следующих комманд: "
                        f"{['' + command for command in ALLOWED_COMMAND_LIST]} ")
        if command not in ALLOWED_COMMAND_LIST:
            raise InvalidInput("введенная вами команда не предусмотрена")
        if command == 'add':
            return add_book_handler()
        elif command == 'list':
            return list_books_handler()
        elif command == 'change_status':
            return change_book_status_handler()
        elif command == 'delete':
            return delete_book_handler()
        elif command == "switch_logic":
            return -1