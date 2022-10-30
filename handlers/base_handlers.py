#!/usr/bin/python3
"""Contains Handlers for Console Actions"""
from models import storage
from models.base_model import BaseModel


def getClasses():
    classes = [BaseModel]
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
    params = str_params.split(" ")
    params = str_params.split(" ")
    classFound = checkClass(params)
    if classFound:
        instance = checkInstance(params)
        if instance:
            print(classFound(**instance))


def handleDestroy(str_params):
    """Show instance of a Model if exists"""
    params = str_params.split(" ")
    classFound = checkClass(params)
    if classFound:
        instance = checkInstance(params)
        if instance:
            storage.remove(f"{instance['__class__']}.{instance['id']}")
            storage.save()


def handleAll(str_params):
    """Prints all string representation of all instances \
        based or not on the class name"""
    dicts = storage.all().values()
    if str_params:
        classFound = getClass(str_params.split(" ")[0])
        if not classFound:
            return
        dicts = [*filter(lambda d: d['__class__'] == str_params, dicts)]
    instances = [*map(dictionaryToInstance, dicts)]
    instance_strings = [*map(lambda i: str(i), instances)]
    print(instance_strings)


def dictionaryToInstance(d):
    """Transform dict repr to instance"""
    [_, _, class_dict] = getClasses()
    Class = class_dict[d['__class__']]
    return Class(**d)
