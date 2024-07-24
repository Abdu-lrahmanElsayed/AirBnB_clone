#!/usr/bin/python3
"""a module for HBNBCommand class"""
import cmd


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand inherited from cmd"""

    prompt = '(hbnb)'

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
