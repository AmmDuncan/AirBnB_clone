#!/usr/bin/python3
"""Contains Handlers for Console Actions"""
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


def getClasses():
    """Get available classes"""
    classes = [BaseModel, User, State, City, Amenity, Place, Review]
    available_classes = [*map(lambda c: c.__name__, classes)]
    class_dict = {name: classes[index]
                  for (index, name) in enumerate(available_classes)}
    return [classes, available_classes, class_dict]


def getInstance(classname=None, id=None):
    """get instance if exists from stored data"""
    instances = storage.all()
    instance_name = f"{classname}.{id}"
    instance = instances.setdefault(instance_name, None)
    if not instance:
        print("** no instance found **")
    return instance


def getClass(classname):
    """get class from available class list if exists"""
    [classes, available_classes, _] = getClasses()
    for (index, c_name) in enumerate(available_classes):
        if c_name == classname:
            return classes[index]
    print("** class doesn't exist **")
    return None


def checkClass(params):
    """Perform checks for class"""
    if len(params) < 1 or not params[0]:
        print("** class name missing **")
    else:
        return getClass(params[0])


def checkInstance(params):
    """Perform checks for instance"""
    if len(params) < 2:
        print("** instance id missing **")
    else:
        return getInstance(params[0], params[1])


def checkAttribute(params):
    """Perform checks for attribute"""
    if len(params) < 3:
        print("** attribute name missing **")
    else:
        return True


def checkValue(params):
    """Perform checks for value"""
    if len(params) < 4:
        print("** value missing **")
    else:
        return True


def handleCreate(classname=None):
    """Handle instance creation"""
    if not classname:
        print("** class name missing **")
    else:
        classFound = getClass(classname)
        if classFound:
            instance = classFound()
            instance.save()
            print(instance.id)


def handleShow(str_params):
    """Show instance of a Model if exists"""
    params = re.findall(r"\"[^\"]+\"|[^\s]+", str_params)
    classFound = checkClass(params)
    if classFound:
        instance = checkInstance(params)
        if instance:
            print(instance)


def handleDestroy(str_params):
    """Show instance of a Model if exists"""
    params = re.findall(r"\"[^\"]+\"|[^\s]+", str_params)
    classFound = checkClass(params)
    if classFound:
        instance = checkInstance(params)
        if instance:
            storage.remove(f"{instance.__class__.__name__}.{instance.id}")
            storage.save()


def handleAll(str_params):
    """Prints all string representation of all instances \
        based or not on the class name"""
    dicts_dict = storage.all()
    instances = dicts_dict.values()
    if str_params:
        classFound = getClass(str_params.split(" ")[0])
        if not classFound:
            return
        instances = [*filter(lambda d: d.__class__.__name__
                             == str_params, instances)]
    instance_strings = [*map(lambda i: str(i), instances)]
    print(instance_strings)


def handleCount(str_params):
    """Count all instances [of a class]"""
    dicts_dict = storage.all()
    instances = dicts_dict.values()
    if str_params:
        classFound = getClass(str_params.split(" ")[0])
        if not classFound:
            return
        instances = [*filter(lambda d: d.__class__.__name__
                             == str_params, instances)]
    print(len(instances))


def handleUpdate(str_params):
    """Update a field on an instance in storage"""
    params = re.findall(r"\"[^\"]+\"|[^\s]+", str_params)
    params = [*map(lambda w: w.strip('"'), params)]
    classFound = checkClass(params)
    if classFound:
        instance = checkInstance(params)
        if instance and checkAttribute(params) and checkValue(params):
            instance[params[2]] = params[3]
            instance.save()
