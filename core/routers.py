from .exceptions import InvalidPrompt
import importlib
from constants import BUSINESS_LOGIC_ROUTES




def manage_command():
    command = input(f"Введите одну из следующих комманд: "
                    f"{['' + command for command in BUSINESS_LOGIC_ROUTES.keys()]} ")
    catcher = BUSINESS_LOGIC_ROUTES.get(command)
    if not catcher:
        raise InvalidPrompt("введенная вами команда не предусмотрена")
    return catcher()