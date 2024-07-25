#!/usr/bin/python3
from models.state import State
import unittest


class TestState(unittest.TestCase):

    def test_name(self):
        s = State()
        s.name = "Alexandria"
        s.save()
        self.assertEqual(s.name, "Alexandria")


if __name__ == '__main__':
    unittest.main()
