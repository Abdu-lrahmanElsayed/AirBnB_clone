#!/usr/bin/python3
from models.base_model import BaseModel
import unittest
from models import storage


class TestBaseModel(unittest.TestCase):

    def test___objects(self):
        model = BaseModel()
        model.save()
        self.assertTrue(storage.__objects)

    def test_all(self):
        stor = storage.all()
        self.assertTrue(stor.__objects)

    def test_new(self):
        model = BaseModel()

    def test_save(self):
        model = BaseModel()
        self.assertTrue(model.save())

    def test_reload(self):
        model = BaseModel()


if __name__ == '__main__':
    unittest.main()
