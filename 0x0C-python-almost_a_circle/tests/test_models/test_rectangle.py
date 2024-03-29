#!/usr/bin/python3
"""Defines unittests for Rectangle class."""


import os
import io
from io import StringIO
import sys
from contextlib import redirect_stdout
from unittest.mock import patch
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class"""

    def setUp(self):
        """Set up Rectangle instance for testing"""
        self.rect = Rectangle(5, 10, 1, 2, 100)

    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("invalid", 2)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.5, 1)

    def test_complex_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(5), 2)

    def test_dict_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"a": 1, "b": 2}, 2)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 2)

    def test_set_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 2)

    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 2)

    def test_frozenset_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({1, 2, 3, 1}), 2)

    def test_range_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(5), 2)

    def test_bytes_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'Python', 2)

    def test_bytearray_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b'abcdefg'), 2)

    def test_nan_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 2)

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_memoryview_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b'abcedfg'), 2)

    def test_inf_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 2)

    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 5.5)

    def test_None_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, None)

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "invalid")

    def test_complex_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, complex(5))

    def test_dict_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {"a": 1, "b": 2})

    def test_list_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, [1, 2, 3])

    def test_set_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {1, 2, 3})

    def test_tuple_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, (1, 2, 3))

    def test_frozenset_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, frozenset({1, 2, 3, 1}))

    def test_range_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, range(5))

    def test_bytes_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, b'Python')

    def test_nan_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('nan'))

    def test_negative_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -1)

    def test_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)

    def test_bytearray_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, bytearray(b'abcdefg'))

    def test_memoryview_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, memoryview(b'abcedfg'))

    def test_inf_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, float('inf'))

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "invalid", 2)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, 5.5, 9)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, complex(5))

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {"a": 1, "b": 2}, 2)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, [1, 2, 3], 2)

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, {1, 2, 3}, 2)

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, (1, 2, 3), 2)

    def test_frozenset_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, frozenset({1, 2, 3, 1}))

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, range(5))

    def test_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float('nan'), 2)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(5, 3, -1, 0)

    def test_bytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, b'hey')

    def test_bytearray_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, bytearray(b'abcdefg'))

    def test_memoryview_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, memoryview(b'abcedfg'))

    def test_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, float('inf'), 2)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, "invalid")

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, None)

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, 5.5)

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, complex(5))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {"a": 1, "b": 2})

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, [1, 2, 3])

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, {1, 2, 3})

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, (1, 2, 3))

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, range(5))

    def test_bytes_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, b'hey')

    def test_frozenset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, frozenset({1, 2, 3, 1}))

    def test_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float('nan'))

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 5, 0, -1)

    def test_bytearray_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, bytearray(b'abcdefg'))

    def test_memoryview_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, memoryview(b'abcedfg'))

    def test_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 1, float('inf'))

    def test_area(self):
        """Test the area method"""
        self.assertEqual(self.rect.area(), 50)

    def test_display(self):
        """Test the display method"""
        self.rect.display()

    def test_display_exist(self):
        """Test the display method if it exists """
        rect = Rectangle(5, 3)  # width=5 and height=3
        expected = "#####\n#####\n#####\n"
        with io.StringIO() as buffer, redirect_stdout(buffer):
            rect.display()
            output = buffer.getvalue()
        self.assertEqual(output, expected)

    def test_display_no_y(self):
        """Test the display method without y"""
        rect = Rectangle(
            5, 5, 2)  # width=5, height=5, and x=2
        expected_width = 5
        expected_height = 5

        with io.StringIO() as buffer, redirect_stdout(buffer):
            rect.display()
            output = buffer.getvalue()
        expected = ' ' * 2 + '#' * expected_width + '\n'
        expected = expected * expected_height
        self.assertEqual(output, expected)
        lines = output.strip().split('\n')
        for line in lines:
            self.assertEqual(len(line.strip()), expected_width)
        self.assertEqual(len(lines), expected_height)

    def test_display_no_x_y(self):
        """ Test the display method without x and y """
        rect = Rectangle(5, 5)
        expected = "#####\n" \
                   "#####\n" \
                   "#####\n" \
                   "#####\n" \
                   "#####\n"
        with io.StringIO() as buffer, redirect_stdout(buffer):
            rect.display()
            output = buffer.getvalue()
        self.assertEqual(output, expected)

    def test_update(self):
        """
        Test update method
        Update using positional arguments
        """
        self.rect.update(200)
        self.assertEqual(self.rect.id, 200)

        self.rect.update(300, 8)
        self.assertEqual(self.rect.id, 300)
        self.assertEqual(self.rect.width, 8)

        self.rect.update(400, 8, 6)
        self.assertEqual(self.rect.id, 400)
        self.assertEqual(self.rect.width, 8)
        self.assertEqual(self.rect.height, 6)

        self.rect.update(500, 8, 6, 4)
        self.assertEqual(self.rect.id, 500)
        self.assertEqual(self.rect.width, 8)
        self.assertEqual(self.rect.height, 6)
        self.assertEqual(self.rect.x, 4)

        self.rect.update(600, 8, 6, 4, 3)
        self.assertEqual(self.rect.id, 600)
        self.assertEqual(self.rect.width, 8)
        self.assertEqual(self.rect.height, 6)
        self.assertEqual(self.rect.x, 4)
        self.assertEqual(self.rect.y, 3)

        # Update using keyword arguments
        self.rect.update(id=700)
        self.assertEqual(self.rect.id, 700)

        self.rect.update(id=800, width=9)
        self.assertEqual(self.rect.id, 800)
        self.assertEqual(self.rect.width, 9)

        self.rect.update(id=900, width=9, height=7)
        self.assertEqual(self.rect.id, 900)
        self.assertEqual(self.rect.width, 9)
        self.assertEqual(self.rect.height, 7)

        self.rect.update(id=1000, width=9, height=7, x=5)
        self.assertEqual(self.rect.id, 1000)
        self.assertEqual(self.rect.width, 9)
        self.assertEqual(self.rect.height, 7)
        self.assertEqual(self.rect.x, 5)

        self.rect.update(id=1100, width=9, height=7, x=5, y=6)
        self.assertEqual(self.rect.id, 1100)
        self.assertEqual(self.rect.width, 9)
        self.assertEqual(self.rect.height, 7)
        self.assertEqual(self.rect.x, 5)
        self.assertEqual(self.rect.y, 6)

        # Test invalid arguments
        with self.assertRaises(TypeError):
            self.rect.update("invalidarg")

    def test_to_dictionary(self):
        """Test the to_dictionary method"""
        dict = {
            "id": 100,
            "width": 5,
            "height": 10,
            "x": 1,
            "y": 2
        }
        # Check generated dictionary
        self.assertDictEqual(self.rect.to_dictionary(), dict)

    def test_save_to_file_none(self):
        """ Test saving none rectangles to a file """
        Rectangle.save_to_file(None)
        file_exists = os.path.isfile("Rectangle.json")
        self.assertTrue(file_exists)
        with open("Rectangle.json", "r") as a_file:
            file_contents = a_file.read()
            self.assertEqual(file_contents, "[]")

    def test_save_to_file_empty_list(self):
        """ Test saving an empty list of rectangles to a file """
        sq = []
        Rectangle.save_to_file(sq)
        with open("Rectangle.json", "r") as a_file:
            file_contents = a_file.read()
            self.assertEqual(file_contents, "[]")

    def test_save_to_file_single_rectangle(self):
        """ Test saving a single square to a file """
        rect = [Rectangle(1, 2, id=1)]
        Rectangle.save_to_file(rect)
        file_exists = os.path.isfile("Rectangle.json")
        self.assertTrue(file_exists)
        with open("Rectangle.json", "r") as a_file:
            file_contents = a_file.read()
        expected = '[{"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}]'
        self.assertEqual(file_contents, expected)

    def test_save_to_file_not_exist(self):
        """ test loading rectangles from a file that does not exist """
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        rect = Rectangle.load_from_file()
        self.assertEqual(rect, [])

    def test_load_from_file_exist(self):
        """Test loading rectangles from an existing file"""
        rects = [
            Rectangle(1, 2, id=1),
            Rectangle(3, 4, id=2),
            Rectangle(5, 6, id=3)
        ]
        Rectangle.save_to_file(rects)
        loaded_rects = Rectangle.load_from_file()
        self.assertEqual(len(loaded_rects), len(rects))
        for idx in range(len(rects)):
            self.assertEqual(loaded_rects[idx].id, rects[idx].id)
            self.assertEqual(loaded_rects[idx].width, rects[idx].width)
            self.assertEqual(loaded_rects[idx].height, rects[idx].height)
            self.assertEqual(loaded_rects[idx].x, rects[idx].x)
            self.assertEqual(loaded_rects[idx].y, rects[idx].y)


if __name__ == '__main__':
    unittest.main()
