#!/usr/bin/env python

from Journal.Quest.Quest import Quest


class MainQuest(Quest):
    """
    Inheriting from the base Quest Class, MainQuest is designed to be a simple way to track the progress of the greater
        overarching plot of the campaign detailed in the journal. The Main quest is designed to be update frequently
        and has very little expansion over the base Quest Class.
    """

    def __init__(self, quest_name, quest_giver, location, phase_description, full_description):
        super().__init__(quest_name, quest_giver, location, phase_description, full_description, "MainQuest")

    def update_entry(self,  phase_description=None, full_update=None, location=None, quest_giver=None):
        """
        Call the parent Quest call to update all of the main quest properties.
        :param phase_description: string being used to create a new phase or step of a quest which is very similar to
            the quest short description.
        :param full_update: string which will be used to store the major details of the new phase of the quest by
            updating the full description of the quest.
        :param location: string/MapMarker which details the location of the current objective for this quest if known
        :param quest_giver: string/CharacterBio which explains who the original giver of the quest is, and who
            (if applicable) to return to for quest completion.
        :return: error code, 0 if update successful, -1 if an error occurred.
        """
        return super().update_entry(phase_description, full_update, location, quest_giver)

    def save_entry(self):
        """
        Create a dictionary which maps all the Main Quest Attributes to string keys of the same name so that they
            can be saved by the Main Journal Entry Class. In this case because the Main quest shares all attributes with
            the Quest base Class, the dictionary pass up will always be empty.

        :return: None
        """
        log = {}
        super().save_entry(log)

