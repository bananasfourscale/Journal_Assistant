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
        phase_description(str): a short one line description of the quest phase which should be used as a marker of the
            progress one has made so far in the given quest.
        full_description(str): a long form description of the aspects of the quest. The details of the full description
            can invoke some of the other class attributes to further describe the quest details.
    """

    def __init__(self, quest_name, quest_giver, location, phase_description, full_description):
        """
        Initialize a class instance and set up any default instance variables
        """
        super().__init__(quest_name)
        self.quest_giver = quest_giver
        self.location = location
        self.phase_description = phase_description
        self.full_description = self.phase_description + "/r/n/t" + full_description

    def update_entry(self, phase_description=None, full_update=None):
        """
        Used to update the phase and/or full description of given quest instance.
        :param phase_description: string being used to create a new phase or step of a quest which is very similar to
            the quest short description.
        :param full_update: string which will be used to store the major details of the new phase of the quest by
            updating the full description of the quest.
        :return: None
        """
        super().update_entry()
        self.phase_description = phase_description + "\n\r" + self.phase_description
        self.full_description = phase_description + "\n\r\t" + full_update + "\n\r" + self.full_description

    def save_entry(self):
        """
        Create a log containing all the different attribute data which is found in a quest implementation, and call the
            base JournalEntry class to store that data to the log file.

        :return: dict - dictionary mapping named entry characteristics with details about the set
            characteristic
        """
        self.updated = False
        # TODO compile dictionary of the class attributes to be saved.

    def read_entry(self):
        """
        Reads the journal entry for the calling implementation of the Quest class by calling the base JournalEntry class
            and passing itself as an argument. At the time of calling the class implementation should only be a shell
            of the Quest class which contains the name of the reference. This information is then used by the
            base class to obtain all the other Quest information and fill out the remaining attribute data.

        :return: None
        """
        super().read_entry(entry=self)
