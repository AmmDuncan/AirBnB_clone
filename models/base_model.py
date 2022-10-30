#!/usr/bin/python3
"""
Base Class Module: defines BaseModel class on which all other
classes will be built
"""
import uuid
from datetime import datetime

from models import storage


class BaseModel:
    """
    Class to define fundamental properties and
    methods of all other models
    """

    def __init__(self, *args, **kwargs):
        """Initiate instance of BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if not args and not kwargs:
            storage.new(self.to_dict())
        for key, value in kwargs.items():
            match(key):
                case 'id':
                    self.id = value
                case 'created_at':
                    self.created_at = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                case 'updated_at':
                    self.updated_at = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")

    def __str__(self):
        """Informal string representation of BaseModel instances"""
        id = self.id
        classname = self.__class__.__name__
        obj_dict = self.__dict__
        return f"[{classname}] ({id}) {obj_dict}"

    def save(self):
        """Update updated at instance attribute"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Get attributes of BaseModel instance"""
        inst_obj = {**self.__dict__}
        inst_obj["__class__"] = self.__class__.__name__
        inst_obj["created_at"] = datetime.strftime(
            inst_obj["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
        inst_obj["updated_at"] = datetime.strftime(
            inst_obj["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        return inst_obj