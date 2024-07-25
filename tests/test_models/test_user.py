#!/usr/bin/python3
from models.user import User
import unittest


class TestUser(unittest.TestCase):

    def test_email(self):
        self.assertEqual(str, type(User.email))
        u = User()
        u.email = "airbnb@mail.com"
        u.save()
        self.assertEqual(u.email, "airbnb@mail.com")

    def test_password(self):
        self.assertEqual(str, type(User.password))
        u = User()
        u.password = "root"
        u.save()
        self.assertEqual(u.password, "root")

    def test_first_name(self):
        self.assertEqual(str, type(User.first_name))
        u = User()
        u.first_name = "Betty"
        u.save()
        self.assertEqual(u.first_name, "Betty")

    def test_last_name(self):
        self.assertEqual(str, type(User.last_name))
        u = User()
        u.last_name = "Bee"
        u.save()
        self.assertEqual(u.last_name, "Bee")


if __name__ == '__main__':
    unittest.main()
