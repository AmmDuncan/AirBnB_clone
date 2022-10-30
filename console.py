#!/usr/bin/python3
"""Entry point for AirBnB clone backend"""
import cmd
from handlers.base_handlers import (
    handleAll,
    handleCreate,
    handleDestroy,
    handleShow
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
