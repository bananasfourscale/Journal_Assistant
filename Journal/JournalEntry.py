#!/usr/bin/env python
"""Base Class representing all types of Journal Entires that can be added to the journal"""


class JournalEntry:
    """
    Represents a journal entry which is the base class used by many other types of entires that can
        be added to the Journal

    Attributes:
        name(str): string which gives a characteristic name to help the user identify the entry
        updated(bool): boolean indicator for determining if the entry has been updated recently
            and should be saved upon exit or call to save.
    """

    def __init__(self, name):
        """
        Initialize a class instance and set up any default instance variables
        """

        self.name = name
        self.updated = True

    def update_entry(self):
        """
        Function meant to be overwritten by the inheriting classes, which will take in characteristic
            info and use that to update the specific entry data.

        :return: None
        """
        self.updated = True

    def save_entry(self):
        """
        Function meant to be overwritten by inheriting classes, which will collect all important entry
            details and place them into a dictionary so that they can be saved. Will also set the updated
            flag to false to inform the journal that this entry has been saved.

        :return: dict - dictionary mapping named entry characteristics with details about the set
            characteristic
        """
        self.updated = False

    def read_entry_log(self, log):
        """
        Function meant to be overwritten by inheriting classes, which will read the given log entry and
            parse the data into an entry class instance.

        :param log: dictionary mapping entry details with the data structure used to hold that detail type.
            Logs are read for each entry upon opening a saved Journal.
        :return: None
        """