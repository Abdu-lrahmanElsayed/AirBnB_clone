#!/usr/bin/python3
"""
a module for class FileStorage
    that serializes instances to a JSON file
    and deserializes JSON file to instances
"""
import json
import os


class FileStorage:
    """
    class FileStorage
    attributes:
        __file_path: string - path to the JSON file
        __objects: dictionary - empty, will store objects by <class name>.id

    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """public method returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """public method sets in __objects 
            the obj with key <obj class name>.id"""
        k = '{}.{}'.format(type(obj).__name__, obj.id)
        FileStorage.__objects[k] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, 'w', encoding="UTF8") as f:
            d = {}
            for k, v in FileStorage.__objects.items():
                d[k] = v.to_dict()
            json.dump(d, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="UTF8") as f:
                FileStorage.__objects = json.load(f)
