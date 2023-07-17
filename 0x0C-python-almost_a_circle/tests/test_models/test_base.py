#!/usr/bin/python3
""" Define unittests for base.py """


import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_init_with_id(self):
        """ Test the initialization method with an id parameter """
        base = Base(id=5)
        self.assertEqual(base.id, 5)

    def test_init_without_id(self):
        """ Test the initialization method without an id parameter """
        base1 = Base()
        base2 = Base()

        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_to_json_string_empty_list(self):
        """ Test to_json_string with an empty list """
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_none(self):
        """ Test to_json_string with None """
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_to_json_string_single_dict(self):
        """ Test to_json_string with a single dictionary """
        my_dict = {"name": "Kate", "age": 10}
        result = Base.to_json_string([my_dict])
        self.assertEqual(result, '[{"name": "Kate", "age": 10}]')

    def test_to_json_string_multiple_dicts(self):
        """ Test to_json_string with multiple dictionaries """
        dict_1 = {"name": "Kate", "age": 10}
        dict_2 = {"name": "Rael", "age": 16}
        result = Base.to_json_string([dict_1, dict_2])
        self.assertEqual(
            result,
            '[{"name": "Kate", "age": 10}, {"name": "Rael", "age": 16}]'
            )

    def test_save_to_file_with_empty_list(self):
        """ Test empty file"""
        Base.save_to_file([])
        with open("Base.json") as a_file:
            file_content = a_file.read()
            self.assertEqual(file_content, "[]")

    def test_save_to_file_with_none(self):
        Base.save_to_file(None)
        with open("Base.json") as a_file:
            file_content = a_file.read()
            self.assertEqual(file_content, "[]")

    def test_create_rectangle_original(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r1))

    def test_create_rectangle_new(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))

    def test_create_rectangle_is(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_create_rectangle_equals(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_create_square_original(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s1))

    def test_create_square_new(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (7) 5/1 - 3", str(s2))

    def test_create_square_is(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

    def test_create_square_equals(self):
        s1 = Square(3, 5, 1, 7)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)


def test_load_from_file(self):
    """Test load_from_file method with different files"""
    result = Rectangle.load_from_file()
    self.assertEqual(result, [])

    rectangle1 = Rectangle(1, 2)
    rectangle2 = Rectangle(3, 4)
    obj_list = [rectangle1, rectangle2]
    Rectangle.save_to_file(obj_list)

    result = Rectangle.load_from_file()
    self.assertIsInstance(result, list)
    self.assertEqual(len(result), 2)
    self.assertIsInstance(result[0], Rectangle)
    self.assertIsInstance(result[1], Rectangle)

    # Delete created file
    os.remove("Rectangle.json")


if __name__ == "__main__":
    unittest.main()
