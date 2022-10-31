#!/usr/bin/python3
"""Define class for file storage engine for AirBnB backend"""
import json


class FileStorage:
    """Class to manage data persistence to file storage"""
    __file_path = "json_db.json"
    __objects = {}

    def all(self):
        """Return stored objects"""
        return self.__objects

    def new(self, obj):
        """Add new object to internal objects list"""
        obj_dict = obj.to_dict()
        key_name = f"{obj_dict['__class__']}.{obj_dict['id']}"
        self.__objects[key_name] = obj

    def save(self):
        """Serialize objects to the JSON file"""
        dict_objects = {}
        for key in self.__objects.keys():
            dict_objects[key] = self.__objects[key].to_dict()
        serialized = json.dumps(dict_objects)
        with open(self.__file_path, 'w') as file:
            file.write(serialized)

    def remove(self, key):
        """Remove object from internal object list"""
        try:
            return self.__objects.pop(key)
        except NameError:
            pass

    def reload(self):
        """Deserialize json file to objects"""
        try:
            from models.base_model import BaseModel
            with open(self.__file_path, 'r') as file:
                self.__objects = json.loads(file.read(), cls=BaseModel)
        except FileNotFoundError:
            pass
