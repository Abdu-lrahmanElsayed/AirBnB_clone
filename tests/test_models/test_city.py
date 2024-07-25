#!/usr/bin/python3
from models.city import City
import unittest


class TestCity(unittest.TestCase):

    def test_state_id(self):
        c = City()
        c.state_id = "3"
        self.assertEqual(c.state_id , "3")

    def test_name(self):
        c = City()
        c.name = "alexandria"
        self.assertEqual(c.state_id , "alexandria")


if __name__ == '__main__':
    unittest.main()
