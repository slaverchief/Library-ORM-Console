from core.exceptions import *

def catch_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except InvalidInput as exc:
            print(f"Произошла ошибка в введенных вами данных: {str(exc)}")
        except ObjectsDontExist as exc:
            print(f'Произошла ошибка при попытке получить данные из базы данных: {str(exc)}')
    return wrapper