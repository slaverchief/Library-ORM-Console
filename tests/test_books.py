import unittest
from business_logic.books_managing.executors import add_book, list_books, delete_book

from core.exceptions import *


class TestExceptionHandlers(unittest.TestCase):

    def test_year_not_digit(self):
        self.assertRaises(InvalidInput, add_book, 'test', 'test', 'invalid_year')

    def test_no_such_objects(self):
        self.assertRaises(ObjectsDontExist, list_books, title="not_existing_title")
        self.assertRaises(ObjectsDontExist, list_books, author="not_existing_author")
        self.assertRaises(ObjectsDontExist, list_books, year=10001)

    def test_id_input(self):
        self.assertRaises(InvalidInput, delete_book, -123)
        self.assertRaises(ObjectsDontExist, delete_book, 10 ** 100)




