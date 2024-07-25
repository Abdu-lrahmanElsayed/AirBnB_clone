#!/usr/bin/python3
"""A module for state class"""
import uuid
import datetime
import models
from models.base_model import BaseModel


class State(BaseModel):
    """State class inherits from BaseModel"""

    name = ""
