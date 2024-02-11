#!/usr/bin/python3
"""The module creates a Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """It defines a class for managing review objects"""

    place_id = ""
    user_id = ""
    text = ""
