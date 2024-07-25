#!/usr/bin/python3
"""A module for user class"""
import uuid
import datetime
import models
from models.base_model import BaseModel


class User(BaseModel):
    """User class inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
