#!/usr/bin/env python
"""Class Representing a Quest entry which will be placed into a Journal"""
from Journal.JournalEntry import *


class Quest(JournalEntry):
    """
    Inheriting from the Journal Entry Class, A Quest is a type entry which is used to describe the various important
        aspects of a quest, and to define the

    Attributes:
        quest_name(str): the reference name of the quest.
        quest_giver(str/CharacterBio): either a string giving the name of the character, or a direct link to a
            CharacterBio which will house greater detail about the giver in question.
        location(str/CharacterBio): either a string giving the simple name of the location where the quest is located
            or a link to a MapMarker which will give more detailed information about the location.
        short_description(str): a short one line description of the quest which can be used to easily remind oneself
            of the goals of the quest.
        full_description(str): a long form description of the aspects of the quest. The details of the full description
            can invoke some of the other class attributes to further describe the quest details.
    """

    def __init__(self, quest_name, quest_giver, location, short_description, full_description):
        """
        Initialize a class instance and set up any default instance variables
        """
        super().__init__(quest_name)
        self.quest_giver = quest_giver
        self.location = location
        self.short_description = short_description
        self.full_description = self.short_description + "/r/n/t" + full_description

    def update_entry(self, phase_description, full_update):
        """
        Function meant to be overwritten by the inheriting classes, which will take in characteristic
            info and use that to update the specific entry data.
        :param phase_description: string being used to create a new phase or step of a quest which is very similar to
            the quest short description.
        :param full_update: string which will be used to store the major details of the new phase of the quest by
            updating the full description of the quest.
        :return: None
        """
        super().update_entry()
        self.short_description = phase_description + "\n\r" + self.short_description
        self.full_description = phase_description + "\n\r\t" + full_update + "\n\r" + self.full_description

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