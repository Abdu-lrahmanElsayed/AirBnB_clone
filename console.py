#!/usr/bin/python3
"""a module for HBNBCommand class"""
import cmd
from models.base_model import BaseModel
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    """class HBNBCommand inherited from cmd"""

    prompt = '(hbnb)'
    valid_classes = ["BaseModel"]

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Do no thing for empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
            saves it (to the JSON file) and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        elif arg not in self.valid_classes:
            print("** class doesn't exist **")
            return
        else:
            bm = BaseModel()
            bm.save()
            print(bm.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
            based on the class name and id"""
        a = arg.split()
        if not arg:
            print("** class name missing **")
            return
        elif a[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        elif len(a) < 2:
            print("** instance id missing **")
            return
        else:
            key = "{}.{}".format(a[0], a[1])
            if key not in storage.all():
                print("** no instance found **")
                return
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        a = arg.split()
        if not arg:
            print("** class name missing **")
            return
        elif a[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        elif len(a) < 2:
            print("** instance id missing **")
            return
        else:
            key = "{}.{}".format(a[0], a[1])
            if key not in storage.all():
                print("** no instance found **")
                return
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not
            on the class name."""
        a = arg.split()
        if len(a) == 0:
            output = [str(obj) for k, obj in storage.all().items()]
            print(output)
        else:
            if a[0] not in self.valid_classes:
                print("** class doesn't exist **")
                return
            else:
                output = [str(obj) for k, obj in storage.all().items()]
                print(output)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
            by adding or updating attribute"""
        a = arg.split()
        if not arg:
            print("** class name missing **")
            return
        elif a[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        elif len(a) < 2:
            print("** instance id missing **")
            return
        else:
            key = "{}.{}".format(a[0], a[1])
            if key not in storage.all():
                print("** no instance found **")
                return
            else:
                if len(a) < 3:
                    print("** attribute name missing **")
                    return
                elif len(a) < 4:
                    print("** value missing **")
                    return
                else:
                    k = "{}.{}".format(a[0], a[2])
                    if k in ("id", "created_at", "updated_at"):
                        return
                    else:
                        value = a[3].replace('"', '')
                        setattr(storage.all()[key], k, value)
                        storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
