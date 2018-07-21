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
        location(str/MapMarker): either a string giving the simple name of the location where the quest is located
            or a link to a MapMarker which will give more detailed information about the location.
        phase_description(str): a short one line description of the quest phase which should be used as a marker of the
            progress one has made so far in the given quest.
        full_description(str): a long form description of the aspects of the quest. The details of the full description
            can invoke some of the other class attributes to further describe the quest details.
        quest_type(str): a string descriptor of the class type used by journal entry to identify which functionality to
            use when loading and saving files.
    """

    def __init__(self, quest_name, quest_giver, location, phase_description, full_description, quest_type):
        """
        Initialize a class instance and set up any default instance variables
        """
        super().__init__(quest_name, quest_type)
        self.quest_giver = quest_giver
        self.location = location
        self.phase_description = phase_description
        self.full_description = self.phase_description + "\r\n\n\t" + full_description
        self.quest_type = quest_type

    def update_entry(self, phase_description=None, full_update=None, location=None, quest_giver=None):
        """
        Used to update all the mailable qualities of the Quest Class
        :param phase_description: string being used to create a new phase or step of a quest which is very similar to
            the quest short description.
        :param full_update: string which will be used to store the major details of the new phase of the quest by
            updating the full description of the quest.
        :param location: string/MapMarker which details the location of the current objective for this quest if known
        :param quest_giver: string/CharacterBio which explains who the original giver of the quest is, and who
            (if applicable) to return to for quest completion.
        :return: error code, 0 if update successful, -1 if an error occurred.
        """
        super().update_entry()
        if phase_description is not None:
            self.phase_description = phase_description + "\n\r\n" + self.phase_description
            if full_update is None:
                return -1  # if the full_update is not given with a phase, return an error.
            self.full_description = phase_description + "\n\r\n\t" + full_update + "\n\r\n" + self.full_description

        self.location = location
        self.quest_giver = quest_giver

    def save_entry(self, log):
        """
        Create a log containing all the different attribute data which is found in a quest implementation, and call the
            base JournalEntry class to store that data to the log file.

        :return: dict - dictionary mapping named entry characteristics with details about the set
            characteristic
        """
        for attribute_name, attribute_value in self.__dict__.items():
            if not attribute_name.startswith('__'):
                log[attribute_name] = attribute_value
        super().save_entry(log)

