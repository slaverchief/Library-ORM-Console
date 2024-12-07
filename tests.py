import unittest
from books.executors import add_book, list_books, change_book_status, delete_book

from main.exceptions import *


class TestBooks(unittest.TestCase):

    def test_year_not_digit(self):
        self.assertRaises(InvalidInput, add_book, 'test', 'test', 'invalid_year')

    def test_no_such_objects(self):
        self.assertRaises(ObjectsDontExist, list_books, title="not_existing_title")
        self.assertRaises(ObjectsDontExist, list_books, author="not_existing_author")
        self.assertRaises(ObjectsDontExist, list_books, year=10001)

    def test_id_input(self):
        self.assertRaises(InvalidInput, delete_book, -123)
        self.assertRaises(ObjectsDontExist, delete_book, 10 ** 100)



if __name__ == "__main__":
    unittest.main()
