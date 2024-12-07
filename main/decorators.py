from .exceptions import *

def catch_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except InvalidPrompt as exc:
            print(f'Произошла ошибка при введении команды: {str(exc)}')
    return wrapper

