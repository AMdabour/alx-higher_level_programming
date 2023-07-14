import unittest
from models.base import Base

class test_base_class(unittest.TestCase):

    def test_is_instance(self):
        s = Base()
        self.assertIsInstance(s, Base)

    def test_id(self):
        s = Base()
        self.assertEqual(s.id, 1)
        s = Base(5)
        self.assertEqual(s.id, 5)
        s = Base()
        self.assertEqual(s.id, 2)
