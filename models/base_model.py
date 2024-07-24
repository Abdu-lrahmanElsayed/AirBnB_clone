#!/usr/bin/python3
"""A module for BaseModel class"""
import uuid
import datetime
from models import storage


class BaseModel:
    """BaseModel class
        defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialize instance attributes of the class,
            all attributes are public

            id: string - assign with an uuid when an instance
            created_at: datetime - assign with the current datetime
                when an instance is created
            updated_at: datetime - assign with the current datetime
                when an instance is created
                and it will be updated every time you change your object
            *args won’t be used
            if kwargs is not empty: will use its items
            """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.datetime.strptime(
                            value,
                            "%Y-%m-%dT%H:%M:%S.%f"
                            ))
            storage.new(self)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        """This method should print:
            [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                self.__dict__
                )

    def save(self):
        """A public method updates the public instance attribute updated_at"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__"""
        dict_str = self.__dict__.copy()
        dict_str['__class__'] = self.__class__.__name__
        dict_str['created_at'] = self.created_at.isoformat()
        dict_str['updated_at'] = self.updated_at.isoformat()
        return dict_str
