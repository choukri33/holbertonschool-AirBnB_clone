#!/usr/bin/python3
"""The init file were the instance of an object is saved"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
