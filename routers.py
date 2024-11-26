from handlers import *

def manage_command(command: str):
    if command == 'add':
        return add_book()
    elif command == 'list':
        return list_book_objects()
    elif command == 'change_status':
        return change_book_status()
    elif command == 'delete':
        return delete_book()