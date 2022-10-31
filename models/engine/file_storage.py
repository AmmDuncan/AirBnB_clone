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
            [_, _, classes_dict] = getClasses()
            with open(self.__file_path, 'r') as file:
                dicts = json.loads(file.read())
                self.__objects = {}
                for key in dicts.keys():
                    value = dicts[key]
                    Class = classes_dict[value['__class__']]
                    self.__objects[key] = Class(**value)
        except FileNotFoundError:
            pass


def getClasses():
    """Get available classes"""
    from models.base_model import BaseModel
    from models.user import User
    classes = [BaseModel, User]
    available_classes = [*map(lambda c: c.__name__, classes)]
    class_dict = {name: classes[index]
                  for (index, name) in enumerate(available_classes)}
    return [classes, available_classes, class_dict]
