#!/usr/bin/python3
"""Define User Model"""
import json
from models.base_model import BaseModel


class User(BaseModel):
    """User model
    """

    def __init__(self, *args, **kwargs):
        """Initialize User object"""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

    def decode(self, s):
        """Decode json to instance"""
        dicts = json.loads(s)
        instances = {}
        for key in dicts.keys():
            instances[key] = self.__class__(**dicts[key])
        return instances
