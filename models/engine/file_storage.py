#!/usr/bin/python3
"""
Containsthe FileStorage class
"""

import json
from models.base_model import Amenity
from models.base_model import BaseModel
from models.base_model import City
from models.base_model import Place
from models.base_model import Review
from models import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BasModel, "City": City, "Place": Place, "Reveiw": Review, "State": State, "User": User}

class FileStorage:
"""Serializes instances to a JSON file & deserializes back to instances"""

# string - path to the JSON file
__file_path = "file.json"
# dictionary - empty but will store all objects
__objects = {}

def all(self, cls=None):
    """returns the dictionary __objects"""
    if cls is not None:
        new_dict = {}
        for key, value in self.__objects.items():
            if cls == value.__class__ or cls == value.__class__.__name__:
                new_dict[key] = value
        new_dict
    return self.__objects

def new(self, obj):
    """sets in __objects the obj with key"""
    if obj is not None:
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

def save(self):
    """Serializes __objects to JSON file"""
    json_objects = {}
    for key in self.__objects:
        json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

def reload(self):
    """deserializes the JSON file to __objects"""
    try:
        with open(self.__file_path, 'r') as f:
            jo = json.load(f)
        for key in jo:
            self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
    except:
        pass

def delete(self, obj=None):
    """delete obj from __objects if it's inside"""
    if obj is not None:
        key = obj.__class__.__name__ + '.' + obj.id
        if key in self.__objects:
            del self.__objects[key]

def close(self):
    """call reload() method for deserializing the JSON file to objects"""
    self.reload()
