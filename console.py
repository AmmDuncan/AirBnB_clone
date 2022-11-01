#!/usr/bin/python3
"""Entry point for AirBnB clone backend"""
import cmd
import re
from handlers.base_handlers import (
    getClasses,
    handleAll,
    handleCount,
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

    def do_count(self, str_params):
        """count [<class name>] {Show count instances [of a class]}
        """
        handleCount(str_params)

    def precmd(self, line: str) -> str:
        [_, class_names, _] = getClasses()
        for classname in class_names:
            # patterns
            show_pattern = r"^{}\.show\(.+\)$".format(classname)
            destroy_pattern = r"^{}\.destroy\(.+\)$".format(classname)
            update_pattern = r"^{}\.update\(.+\)$".format(classname)
            args_pattern = r"\(([^,]+)\)"
            # args
            args = re.findall(args_pattern, line)
            has_args = len(args) > 0
            # checks
            if line == f"{classname}.all()":
                return super().precmd(f'all {classname}')
            if line == f"{classname}.count()":
                return super().precmd(f"count {classname}")
            if re.search(show_pattern, line) and has_args:
                arg = args[0]
                return super().precmd(f"show {classname} {arg}")
            if re.search(destroy_pattern, line) and has_args:
                arg = args[0]
                return super().precmd(f"destroy {classname} {arg}")
            if re.search(update_pattern, line) and has_args:
                id = args[0]
                attr_name = ""
                attr_value = ""
                if len(args) > 1:
                    attr_name = args[1]
                if len(args) > 2:
                    attr_value = args[2]
                return super().precmd(
                    f"destroy {classname} {id} {attr_name} {attr_value}")
        return super().precmd(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
