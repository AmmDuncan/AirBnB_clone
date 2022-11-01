#!/usr/bin/python3
"""Entry point for AirBnB clone backend"""
import cmd
from handlers.base_handlers import (
    getClasses,
    handleAll,
    handleCreate,
    handleDestroy,
    handleShow,
    handleUpdate
)


class HBNBCommand(cmd.Cmd):
    """Interpreter class to process commands from the command line"""

    prompt = "(hbnb) "

    def emptyline(self, *args):
        """Do nothing"""
        pass

    def do_quit(self, *args):
        """Quit command to exit the program
        """
        exit(0)

    def do_EOF(self, *args):
        """Quit command to exit the program
        """
        exit(0)

    def do_create(self, classname):
        """create <class name> {create an instance of the <class name>}
        """
        handleCreate(classname)

    def do_show(self, str_params):
        """show <class name> <id> {Show details of and instance of a class}
        """
        handleShow(str_params)

    def do_destroy(self, str_params):
        """destroy <class name> <id> {Delete instance from storage}
        """
        handleDestroy(str_params)

    def do_all(self, str_params):
        """all [<class name>] {Show all instances [of a class]}
        """
        handleAll(str_params)

    def do_update(self, str_params):
        """update <class name> <id> <field> "<value>" {Update an instance}
        """
        handleUpdate(str_params)

    def precmd(self, line: str) -> str:
        [_, class_names, _] = getClasses()
        for classname in class_names:
            if f"{classname}.all()" == line:
                return super().precmd(f'all {classname}')
        return super().precmd(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
