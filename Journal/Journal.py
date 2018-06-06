#!/usr/bin/env python

"""Class Representing a Journal which holds different types of JournalEntries"""


class Journal:
    """
    Class Representing the Journal of a player. Can contain any number of different entries specific to the
        journey of the player, and handles storage and retrieval of entries by saving pertinent data to a file
        upon request, and on successful exit of program.

    Attributes:
        saved(bool): Flag indicating if the journal has been saved since the most recent update of any of its entries
        quest_entries(dict): Dictionary of all journal entries which fall into the Quest classification,
            mapped with entry names as keys and entry references as values.
        map_markers(dict): Dictionary of all journal entries which fall into the MapMarker classification,
            mapped with entry names as keys and entry references as values.
        character_bios(dict): Dictionary of all journal entries which fall into the the CharacterBio classification,
            mapped with entry names as keys and entry references as values.
        bestiary(dict): Dictionary of all journal entries which fall into the Bestiary classification,
            mapped with entry names as keys and entry references as values.
    """

    def __init__(self):
        """
        Initialize a journal instance to be used by either a DM or Player Character
        """
        self.saved = False
        self.quest_entries = {}
        self.map_markers = {}
        self.character_bios = {}
        self.bestiary = {}

    def add_quest_entry(self, entry):
        """
        Add a new quest entry to the journal. Entries can be of a few different types including,
            MainQuest, MajorQuest, FactionQuest, SideQuest, MinorQuest, Task

        :param entry: any class which inherits from the base JournalEntry class and falls into the Quest
            classification.
        :return: None
        """

        self.quest_entries[entry.name] = entry
        self.saved = False

    def add_map_marker(self, marker):
        """
        Add a new map marker to the journal. Map markers can be one a few different types including,
            Capital, City, Village, WildernessSite

        :param marker: any class which inherits from the base JournalEntry class and falls in the MapMarker
            classification
        :return: None
        """

        self.map_markers[marker.name] = marker
        self.saved = False

    def add_character_bio(self, bio):
        """
        Add a new bio to the journal. Bios are commonly character biographies of characters
                that are met in the players travels.

        :param bio: any class which inherits from the base JournalEntry class and falls into the CharacterBio
            classification.
        :return: None
        """

        self.character_bios[bio.name] = bio
        self.saved = False

    def add_bestiary_entry(self, entry):
        """
        Add a new bestiary entry to the journal. Bestiary entries are used to chronicle the stats and abilities of
            creatures that are encountered by the player on their journey.

        :param entry: any class which inherits from the base JournalEntry class and falls in the Bestiary
            classification.
        :return: None
        """

        self.bestiary[entry.name] = entry
        self.saved = False
