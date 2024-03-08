#!/usr/bin/python3
"""Console and methods for
Console
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """HBNB Command class"""
    prompt = '(hbnb) '
    classesList = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review",
    ]

    def do_quit(self, arg):
        """ Exit the console"""
        return True

    def do_EOF(self, arg):
        """ Exit the console"""
        return True

    def emptyline(self):
        """Prevent empty lines"""
        pass

    def do_create(self, arg):
        """Create a BaseModel"""
        splitedARG = arg.split()
        if len(arg) < 1:
            print("** class name missing **")
        elif splitedARG[0] in self.classesList:
            newModel = eval(splitedARG[0])()
            print(newModel.id)
            newModel.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Show instance string representation"""
        splitedARG = arg.split()
        if len(splitedARG) < 1:
            print("** class name missing **")
        elif splitedARG[0] not in self.classesList:
            print("** class doesn't exist **")
        elif len(splitedARG) < 2:
            print("** instance id missing **")
        else:
            class_and_id = splitedARG[0] + '.' + splitedARG[1]
            objects = storage.all()
            if class_and_id in objects:
                print(objects[class_and_id])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete instance and save (from id)."""
        splitedARG = arg.split()
        if len(splitedARG) < 1:
            print("** class name missing **")
        elif splitedARG[0] not in self.classesList:
            print("** class doesn't exist **")
        elif len(splitedARG) < 2:
            print("** instance id missing **")
        else:
            class_and_id = splitedARG[0] + '.' + splitedARG[1]
            objects = storage.all()
            if class_and_id in objects:
                del objects[class_and_id]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Print all string repr of all instances"""
        splitedARG = arg.split()
        my_list = []
        objects = storage.all()
        if not arg:
            for obj in objects:
                my_list.append(str(objects[obj]))
            print(my_list)
        else:
            if splitedARG[0] in self.classesList:
                for obj in objects:
                    if obj.split('.')[0] == splitedARG[0]:
                        my_list.append(str(objects[obj]))
                print(my_list)
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance based on ID"""
        if not arg or len(arg) <= 0:
            print("** class name missing **")
            return
        splitedARG = arg.split()
        if splitedARG[0] not in self.classesList:
            print("** class doesn't exist **")
            return
        elif len(splitedARG) < 2:
            print("** instance id missing **")
            return
        dictionary = storage.all()
        class_and_id = splitedARG[0] + '.' + splitedARG[1]
        if class_and_id not in dictionary:
            print("** no instance found **")
            return
        if len(splitedARG) < 3:
            print("** atribute name missing **")
            return
        elif len(splitedARG) < 4:
            print("** value missing **")
            return
        for key, value in dictionary.items():
            if key == class_and_id:
                setattr(value, splitedARG[2], eval(splitedARG[3]))
                value.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
