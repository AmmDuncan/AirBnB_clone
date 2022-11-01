#!/usr/bin/python3
"""Define Review Class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Representation of reviews"""

    place_id = ""
    user_id = ""
    text = ""
