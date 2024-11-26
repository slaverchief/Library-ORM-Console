
from routers import *
from exceptions import *

ALLOWED_COMMAND_LIST = ['add', 'delete', 'list', 'change_status']

def main():
    while True:
        try:
            command = input(f"Введите одну из следующих комманд: "
                            f"{[''+command for command in ALLOWED_COMMAND_LIST]} ")
            if command not in ALLOWED_COMMAND_LIST:
                raise LibraryException("введенная вами команда не предусмотрена")
            print(manage_command(command))
        except InvalidInput as exc:
            print(f"Произошла ошибка в введенных вами данных: {str(exc)}")
        except ObjectsDontExist as exc:
            print(f'Произошла ошибка при попытке получить данные из базы данных: {str(exc)}')
        except InvalidPrompt as exc:
            print(f'Произошла ошибка при введении команды: {str(exc)}')

if __name__ == '__main__':
    Book.initialize()
    main()