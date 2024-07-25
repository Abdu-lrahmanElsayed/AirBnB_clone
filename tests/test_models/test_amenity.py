#!/usr/bin/python3
from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):

    def test_name(self):
        self.assertEqual(str, type(Amenity.name()))
        a = Amenity()
        a.name = "plah"
        a.save()
        self.assertEqual(a.name, "plah")


if __name__ == '__main__':
    unittest.main()
