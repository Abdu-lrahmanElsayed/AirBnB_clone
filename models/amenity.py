#!/usr/bin/python3
"""A module for Amenity class"""
import uuid
import datetime
import models
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class inherits from BaseModel"""

    name = ""
