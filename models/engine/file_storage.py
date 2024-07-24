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

    def __init__(self):
        """initialize attrs"""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """public method returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """public method sets in __objects 
            the obj with key <obj class name>.id"""
        self.__objects['{}.{}'.format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        with open(self.__file_path, 'w', encoding="UTF8") as f:
            d = {k:v.to_dict() for k, v in self.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r', encoding="UTF8") as f:
                self.__objects = json.load(f)
