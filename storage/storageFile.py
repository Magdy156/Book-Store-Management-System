#!/usr/bin/python3
"""File storage module"""
import json


class FileStorage:
    """Represents our storage"""
    __file_path = "books.json"

    def reload(self):
        """Deserializes a JSON file to dictionaries"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                booksData = json.load(f)
            return (booksData)
        except FileNotFoundError:
            return
