#!/usr/env python3
"""Lite compiler create"""
import os


class Create:
    """
        Create model of the data definition language
        Args:
            identifier: to determine a table or a database
            condition: include conditional for identifier
            lang: how to create a table
        Return:
    """

    def __init__(self):
        """initialize / constructor"""
        pass

    def database(self, flags: bool = False, name: str = None) -> None:
        """
        A method that create a database
        Args:
            name: a string that take the name of the database
            flags: an optional value that doesn't raise Error
        """
        file_path = name + '.db'
        try:
            if os.path.isfile(file_path) and flags is False:
                raise FileExistsError
            else:
                with open(file_path, 'w') as file:
                    file.write('')
        except Exception as e:
            print(e)
        finally:
            file.close()

    def table(self, _name: str, struct: dict) -> None:
        """
        A method that creates a table in a database
        Args:
            _name: name of the table to be created
            struct: list of attribute/property to add to table
        return:
        """

