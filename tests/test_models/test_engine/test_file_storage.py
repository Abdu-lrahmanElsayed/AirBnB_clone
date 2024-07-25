#!/usr/bin/python3
from models.base_model import BaseModel
import unittest
import models
import os
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):

    def test___objects(self):
        model = BaseModel()
        model.save()
        self.assertTrue(models.storage.__objects)

    def test_all(self):
        self.assertEqual(type(models.storage.all()), dict)

    def test_new(self):
        model = BaseModel()
        models.storage.new(model)
        self.assertIn("BaseModel.{}".format(model.id), models.storage.all())

    def test_save(self):
        model = BaseModel()
        models.storage.new(model)
        models.storage.save()
        self.assertTrue(os.path.isfile("json.file"))

    def test_reload(self):
        model = BaseModel()
        models.storage.reload()
        self.assertIn("BaseModel.{}".format(model.id), models.storage.all())


if __name__ == '__main__':
    unittest.main()
