#!/usr/bin/python3
from models.user import User
import unittest


class TestUser(unittest.TestCase):

    def tets_email(self):
        u = User()
        u.email = "airbnb@mail.com"
        u.save()
        self.assertTrue(u.email)

    def test_password(self):
        u = User()
        u.password = "root"
        u.save()
        self.assertTrue(u.password)

    def test_first_name(self):
        u = User()
        u.first_name = "Betty"
        u.save()
        self.assertTrue(u.first_name)

    def test_last_name(self):
        u = User()
        u.last_name = "Bee"
        u.save()
        self.assertTrue(u.last_name)


if __name__ == '__main__':
    unittest.main()
