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

    def test_update_invalid_size(self):
        """ Test update method with invalid size """
        with self.assertRaises(ValueError):
            self.square.update(2, -2, 4, 6)

    def test_update_invalid_x(self):
        """ Test update method with invalid x """
        with self.assertRaises(ValueError):
            self.square.update(2, 2, -4, 6)

    def test_update_invalid_y(self):
        """ Test the update method with invalid y """
        with self.assertRaises(ValueError):
            self.square.update(2, 7, 4, -6)

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
    
    def test_area(self):
        """ test the area method of the Square class """
        self.assertEqual(self.square.area(), 25)
        self.square.size = 8
        self.assertEqual(self.square.area(), 64)

if __name__ == '__main__':
    unittest.main()
