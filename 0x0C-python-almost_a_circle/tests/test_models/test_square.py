#!/usr/bin/python3
"""Defines unittests for Square class."""


import os
import unittest
from models.square import Square


class SquareTestCase(unittest.TestCase):
    """ Unit tests for the square class """

    def setUp(self):
        """ Set up square instances for testing """
        self.square = Square(5, 2, 3, 1)

    def test_size(self):
        """ Test the size property """
        self.assertEqual(self.square.size, 5)

    def test_area(self):
        """ Test the area calculation """
        self.assertEqual(self.square.area(), 25)

    def test_width_property(self):
        """ Test the width property """
        self.assertEqual(self.square.width, 5)

    def test_height_property(self):
        """ Test the height property """
        self.assertEqual(self.square.height, 5)

    def test_set_size(self):
        """ Test setting the size property """
        self.square.size = 4
        self.assertEqual(self.square.size, 4)
        self.assertEqual(self.square.width, 4)
        self.assertEqual(self.square.height, 4)

    def test_constructor(self):
        """ Test the consructor of the Square class """
        self.assertEqual(self.square.size, 5)
        self.assertEqual(self.square.x, 2)
        self.assertEqual(self.square.y, 3)
        self.assertEqual(self.square.id, 1)

    def test_valid_square(self):
        """ test creating a valid square instance """
        sq = Square(1, 2, 3, 4)
        self.assertEqual(sq.size, 1)
        self.assertEqual(sq.x, 2)
        self.assertEqual(sq.y, 3)
        self.assertEqual(sq.id, 4)

    def test_square_create(self):
        """ Test to create a square with 1, 2 inputs """
        sq = Square(1, 2)
        self.assertEqual(sq.size, 1)
        self.assertEqual(sq.x, 2)
        self.assertEqual(sq.y, 0)

    def test_valid_square_without_y(self):
        """ test creating a square without y """
        sq = Square(1, 2, 3)
        self.assertEqual(sq.size, 1)
        self.assertEqual(sq.x, 2)
        self.assertEqual(sq.y, 3)

    def test_valid_square_only_size(self):
        """ test creating a square with the size parameter only """
        sq = Square(1)
        self.assertEqual(sq.size, 1)
        self.assertEqual(sq.y, 0)
        self.assertEqual(sq.y, 0)

    def test_str(self):
        """ Test the __str__ method of te Square class """
        self.assertEqual(str(self.square), "[Square] (1) 2/3 - 5")

    def test_size_property(self):
        """ Test the size property of the Square class """
        self.assertEqual(self.square.size, 5)
        self.square.size = 10
        self.assertEqual(self.square.size, 10)
        self.assertEqual(self.square.width, 10)
        self.assertEqual(self.square.height, 10)

    def test_invalid_size(self):
        """ test create a square with an invalid y """
        with self.assertRaises(TypeError):
            Square("1", 2, 3, 1)

    def test_update_invalid_size(self):
        """ Test update method with invalid size """
        with self.assertRaises(ValueError):
            self.square.update(2, -2, 4, 6)

    def test_negative_size(self):
        """ test creating a square with a -ve size """
        with self.assertRaises(ValueError):
            Square(-1, 2, 3, 1)

    def test_negative_size_and_x(self):
        """ test creating a square with a -ve size & x """
        with self.assertRaises(ValueError):
            Square(1, -2, 3, 1)

    def test_negative_size_x_y(self):
        """ test creating a square with a -ve size, x & y """
        with self.assertRaises(ValueError):
            Square(1, 2, -3, 1)

    def test_zero_size(self):
        """ test create a square with size 0 """
        with self.assertRaises(ValueError):
            Square(0, 2, 3, 1)

    def test_update_invalid_x(self):
        """ Test update method with invalid x """
        with self.assertRaises(ValueError):
            self.square.update(2, 2, -4, 6)

    def test_invalid_x(self):
        """ test create a square with an invalid x """
        with self.assertRaises(TypeError):
            Square(1, "2", 3, 1)

    def test_update_invalid_y(self):
        """ Test the update method with invalid y """
        with self.assertRaises(ValueError):
            self.square.update(2, 7, 4, -6)

    def test_invalid_y(self):
        """ test create a square with an invalid y """
        with self.assertRaises(TypeError):
            Square(1, 2, "3", 1)

    def test_update_with_args(self):
        """ Test the update method of the Square class with args"""
        self.square.update(2, 7, 4, 6)
        self.assertEqual(self.square.id, 2)
        self.assertEqual(self.square.size, 7)
        self.assertEqual(self.square.x, 4)
        self.assertEqual(self.square.y, 6)

    def test_update_with_kwargs(self):
        """ Test the update method of the Square class with kwargs """
        self.square.update(size=8, x=5)
        self.assertEqual(self.square.size, 8)
        self.assertEqual(self.square.x, 5)

    def test_update_invalid_id(self):
        """ Test the update method with invalid type"""
        with self.assertRaises(TypeError):
            self.square.update("invalidid", 10, 4, 6)

    def test_to_dictionary(self):
        """ Test the to_dictionary method of the Square class """
        expected_dict = {
            "id": 1,
            "size": 5,
            "x": 2,
            "y": 3,
        }
        self.assertEqual(self.square.to_dictionary(), expected_dict)

    def test_to_dictionary_output(self):
        """
        Test case to verify the output of the to_dictionary method
        """
        s = Square(10, 2, 1, 1)
        correct = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(correct, s.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        """
        Test case to ensure that the to_dictionary method does
        not modify the state of the Square object
        """
        s1 = Square(10, 2, 1, 2)
        s2 = Square(1, 2, 10)
        s2.update(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)

    def test_to_dictionary_arg(self):
        """
        Test case to check if calling to_dictionary with an
        arg other than self raises a TypeError.
        """
        sq = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            sq.to_dictionary(1)

    def test_area(self):
        """ test the area method of the Square class """
        self.assertEqual(self.square.area(), 25)
        self.square.size = 8
        self.assertEqual(self.square.area(), 64)

    def test_save_to_file_none(self):
        """ Test saving none squares to a file """
        Square.save_to_file(None)
        file_exists = os.path.isfile("Square.json")
        self.assertTrue(file_exists)
        with open("Square.json", "r") as a_file:
            file_contents = a_file.read()
            self.assertEqual(file_contents, "[]")

    def test_save_to_file(self):
        """ Test saving the squares of a file"""
        sq_list = [Square(3, 1, 2, 4), Square(4, 5, 6, 5)]
        Square.save_to_file(sq_list)
        with open("Square.json", "r") as a_file:
            file_contents = a_file.read()
            expect = '[{"id": 4, "size": 3, "x": 1, "y": 2}, ' \
                '{"id": 5, "size": 4, "x": 5, "y": 6}]'
            self.assertEqual(file_contents, expect)

    def test_save_to_file_empty_list(self):
        """ Test saving an empty list of squares to a file """
        sq = []
        Square.save_to_file(sq)
        with open("Square.json", "r") as a_file:
            file_contents = a_file.read()
            self.assertEqual(file_contents, "[]")

    def test_save_to_file_single_square(self):
        """ Test saving a single square to a file """
        sq = [Square(1, id=1)]
        Square.save_to_file(sq)
        with open("Square.json", "r") as a_file:
            file_contents = a_file.read()
        expected = '[{"id": 1, "size": 1, "x": 0, "y": 0}]'
        self.assertEqual(file_contents, expected)

    def test_save_to_file_not_exist(self):
        """ test loading squares from a file that does not exist """
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        sq = Square.load_from_file()
        self.assertEqual(sq, [])

    def test_save_to_file_exist(self):
        """Test loading squares from an existing file"""
        sq = [Square(3, 1, 2, 4), Square(4, 5, 6, 5)]
        Square.save_to_file(sq)
        loaded_sq = Square.load_from_file()

        for orig_sq, loaded_square in zip(sq, loaded_sq):
            self.assertEqual(orig_sq.size, loaded_square.size)
            self.assertEqual(orig_sq.x, loaded_square.x)
            self.assertEqual(orig_sq.y, loaded_square.y)
            self.assertEqual(orig_sq.id, loaded_square.id)


if __name__ == '__main__':
    unittest.main()
