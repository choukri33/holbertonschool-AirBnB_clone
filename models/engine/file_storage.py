#!/usr/bin/python3
from models.base_model import BaseModel
import json

"""FileStorage allows to manage serialization & deserialization"""


class FileStorage:
    """FileStorage Class"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns __objects dict"""
        return self.__objects

    def new(self, obj):
        """Add a new object in the object dict"""

        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Save the __objects dict to a json file"""
        serialized_obj = {}
        for key, value in self.__objects.items():
            serialized_obj[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(serialized_obj, file)

    def reload(self):
        """Reload dict from json file"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                for key, value in json.load(file).items():
                    value = eval(key.split(".")[0])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass
