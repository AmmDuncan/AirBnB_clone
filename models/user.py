#!/usr/bin/python3
"""Define User Model"""
import email
from models.base_model import BaseModel


class User(BaseModel):
    """User model
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize User object"""
        super().__init__(*args, **kwargs)
