#!/usr/bin/python3
"""Defines unittests for Rectangle class."""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class"""

    def setUp(self):
        """Set up Rectangle instance for testing"""
        self.rect = Rectangle(5, 10, 1, 2, 100)

    def test_width(self):
        """Test the width property and setter"""
        self.assertEqual(self.rect.width, 5)  # Check initial width
        self.rect.width = 3  # Change width
        self.assertEqual(self.rect.width, 3)
        with self.assertRaises(TypeError):
            self.rect.width = "invalid"
        with self.assertRaises(ValueError):
            self.rect.width = -5

    def test_height(self):
        """Test the height property and setter"""
        self.assertEqual(self.rect.height, 10)  # Check initial height
        self.rect.height = 4
        self.assertEqual(self.rect.height, 4)
        with self.assertRaises(TypeError):
            self.rect.height = "invalid"
        with self.assertRaises(ValueError):
            self.rect.height = -10

    def test_x(self):
        """Test the x property and setter"""
        self.assertEqual(self.rect.x, 1)  # Check initial x
        self.rect.x = 2  # Change x
        self.assertEqual(self.rect.x, 2)
        with self.assertRaises(TypeError):
            self.rect.x = "invalid"
        with self.assertRaises(ValueError):
            self.rect.x = -2

    def test_y(self):
        """Test the y property and setter"""
        self.assertEqual(self.rect.y, 2)  # Check initial y
        self.rect.y = 7
        self.assertEqual(self.rect.y, 7)
        with self.assertRaises(TypeError):
            self.rect.y = "invalid"
        with self.assertRaises(ValueError):
            self.rect.y = -1

    def test_area(self):
        """Test the area method"""
        self.assertEqual(self.rect.area(), 50)

    def test_display(self):
        """Test the display method"""
        self.rect.display()

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


if __name__ == '__main__':
    unittest.main()
