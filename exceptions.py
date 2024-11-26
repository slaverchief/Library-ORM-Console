class LibraryException(Exception):
    pass

class ObjectsDontExist(LibraryException):
    pass

class InvalidInput(LibraryException):
    pass

class InvalidPrompt(LibraryException):
    pass

class SystemError(LibraryException):
    pass