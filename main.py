
from main.routers import *
from main.decorators import catch_exceptions



@catch_exceptions
def main():
    manage_command()


if __name__ == '__main__':
    while True:
        main()