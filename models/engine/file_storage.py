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
        key_name = f"{obj['__class__']}.{obj['id']}"
        self.__objects[key_name] = obj

    def save(self):
        """Serialize objects to the JSON file"""
        serialized = json.dumps(self.__objects)
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
            with open(self.__file_path, 'r') as file:
                self.__objects = json.loads(file.read())
        except FileNotFoundError:
            pass
