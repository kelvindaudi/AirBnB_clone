#!/usr/bin/python3
"""The module creates a User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """This defines a class for managing user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
