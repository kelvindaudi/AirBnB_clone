#!/usr/bin/python3
"""The module creates a User class"""

from models.base_model import BaseModel


class City(BaseModel):
    """The defines class for managing city objects"""

    state_id = ""
    name = ""
