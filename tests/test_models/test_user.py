#!/usr/bin/python3
from models.user import User
import unittest


class TestUser(unittest.TestCase):

    def test_email(self):
        u = User()
        u.email = "airbnb@mail.com"
        u.save()
        self.assertEqual(u.email, "airbnb@mail.com")

    def test_password(self):
        u = User()
        u.password = "root"
        u.save()
        self.assertEqual(u.password, "root")

    def test_first_name(self):
        u = User()
        u.first_name = "Betty"
        u.save()
        self.assertEqual(u.first_name, "Betty")

    def test_last_name(self):
        u = User()
        u.last_name = "Bee"
        u.save()
        self.assertEqual(u.last_name, "Bee")


if __name__ == '__main__':
    unittest.main()
