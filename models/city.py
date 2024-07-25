#!/usr/bin/python3
"""A module for city class"""
import uuid
import datetime
import models
from models.base_model import BaseModel


class City(BaseModel):
    """City class inherits from BaseModel"""

    state_id = ""
    name = ""
