#!/usr/bin/pyhton3
import uuid
from datetime import datetime

import models


class BaseModel:
    """Create a Class BaseModel"""
    def __init__(self, *args, **kwargs):
        """Init attribute"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    now = datetime.now()
                    custom_time = now.strftime("%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
    
    def __str__(self):
        """Representation to a string"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Add a dict"""
        obj_dict = self.__dict__.copy()
        obj_dict.update({"__class__": self.__class__.__name__,
                         "created_at": self.created_at.isoformat(),
                         "updated_at": self.updated_at.isoformat()})

        return obj_dict
