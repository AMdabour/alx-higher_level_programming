import unittest
from models.rectangle import Rectangle
from models.base import Base

class test_rectangle_class(unittest.TestCase):

    def test_is_instance(self):
        r = Rectangle(10, 2)
        self.assertIsInstance(r, Rectangle)

    def test_is_subclass(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def test_getter_setter(self):
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        r.width = 5
        self.assertEqual(r.width, 5)
        with self.assertRaises(AttributeError):
            x = r.__width
