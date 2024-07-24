#!/usr/bin/python3
from models.base_model import BaseModel
import unittest
import datetime


class TestBaseModel(unittest.TestCase):

    def test_id(self):
        my_model = BaseModel()
        self.assertTrue(my_model.id)

    def test_created_at(self):
        my_model = BaseModel()
        self.assertTrue(my_model.created_at)

    def test_save_updated_at(self):
        my_model = BaseModel()
        my_model.save()
        self.assertNotEqual(my_model.updated_at, my_model.created_at)

    def test_str(self):
        my_model = BaseModel()
        self.assertEqual(str(my_model), "[{}] ({}) {}".format(my_model.__class__.__name__, my_model.id, my_model.__dict__))

    def test_to_dict(self):
        my_model = BaseModel()
        output = my_model.to_dict()
        self.assertIn('id', output)
        self.assertIn('created_at', output)
        self.assertIn('__class__', output)
        self.assertIn('updated_at', output)


if __name__ == '__main__':
    unittest.main()
