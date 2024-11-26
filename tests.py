import unittest
from executors import add, list_objects, change_status, delete

from exceptions import *


class TestAddMethod(unittest.TestCase):

    def test_year_not_digit(self):
        self.assertRaises(InvalidInput, add, 'test', 'test', 'invalid_year')

class TestListObjectMethod(unittest.TestCase):

    def test_no_such_objects(self):
        self.assertRaises(ObjectsDontExist, list_objects, title="not_existing_title")
        self.assertRaises(ObjectsDontExist, list_objects, author="not_existing_author")
        self.assertRaises(ObjectsDontExist, list_objects, year=10001)

class TestChangeStatusMethod(unittest.TestCase):

    def test_id_input(self):
        self.assertRaises(InvalidInput, change_status, -123)
        self.assertRaises(InvalidInput, change_status, 'dsadas')
        self.assertRaises(ObjectsDontExist, change_status, 10**100)

class TestDeleteMethod(unittest.TestCase):

    def test_id_input(self):
        self.assertRaises(InvalidInput, delete, -123)
        self.assertRaises(InvalidInput, delete, 'dsadas')
        self.assertRaises(ObjectsDontExist, delete, 10 ** 100)
        self.assertRaises(InvalidInput, delete, '2')

if __name__ == "__main__":
    unittest.main()
