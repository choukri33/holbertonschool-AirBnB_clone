#!/usr/bin/python3
""" Import module class """
import json
from datetime import datetime
from models.base_model import BaseModel


class FileStorage:
    """ Create a Class FileStorage that serializes
    instances to a JSON file and deserializes JSON file to instances"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ return instances storaged """
        return self.__objects

    def new(self, obj):
        """ Add a new object to objects dictionary """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ Serialize __objects to the JSON file (path: __file_path) """
        save_obj = {}
        for key, value in self.__objects.items():
            save_obj[key] = value.to_dict()
        with open(self.__file_path, "w") as jsonfile:
            json.dump(save_obj, jsonfile)

    def reload(self):
        """ Deserialize the object from JSON file """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as jsonfile:
                json_dict = json.load(jsonfile)
                for key, value in json_dict.items():
                    value['created_at'] = datetime.strptime(value['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
                    value['updated_at'] = datetime.strptime(value['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
                    obj_class = eval(key.split(".")[0])
                    obj_instance = obj_class(**value)
                    self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
   
