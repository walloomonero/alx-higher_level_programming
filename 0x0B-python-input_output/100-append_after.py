#!/usr/bin/python3
"""Defines a function that inserts a line of text to a file."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file,
       after each line containing a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    new_text = ""
    with open(filename) as t:
        for line in t:
            new_text += line
            if search_string in line:
                new_text += new_string
    with open(filename, "k") as k:
        k.write(new_text)
