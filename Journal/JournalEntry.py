#!/usr/bin/env python
"""Base Class representing all types of Journal Entires that can be added to the journal"""
from Journal.FileSystem.JournalFileLogger import JournalFileLogger


class JournalEntry:
    """
    Represents a journal entry which is the base class used by many other types of entires that can
        be added to the Journal

    Attributes:
        name(str): string which gives a characteristic name to help the user identify the entry
        entry_type(str): string which is used to identify the class type of the entry so that when reading
            the entry from a file or calling functions, the correct operations are performed.
        updated(bool): boolean indicator for determining if the entry has been updated recently
            and should be saved upon exit or call to save.
    """

    def __init__(self, name, entry_type):
        """
        Initialize a class instance and set up any default instance variables
        """
        self.name = name
        self.entry_type = entry_type
        self.__updated = True

    def update_entry(self):
        """
        Function meant to be overwritten by the inheriting classes, which will take in characteristic
            info and use that to update the specific entry data.

        :return: None
        """
        self.__updated = True

    def save_entry(self, log):
        """
        Function meant to be overwritten by inheriting classes, which will collect all important entry
            details and place them into a dictionary so that they can be saved. Will also set the updated
            flag to false to inform the journal that this entry has been saved.

        :param log: dictionary from inheriting sub class which this base class will store by calling the file logger.
            This keeps the need for multiple repetitive imports of the logger from being required in all sub classes.
        :return: None
        """
        self.__updated = False
        JournalFileLogger.save_log_entry(log)

