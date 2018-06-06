#!/usr/bin/env python
"""Used to read and write to Journal Files which are stored in a yaml format"""
# TODO import yaml and test functionality
import yaml


class JournalFileLogger:
    def __init__(self):
        self.file_name = None  # TODO make some default
        pass  # TODO: write file system.
        # TODO: figure out how to make relative file path for where the log is stored. May have to make log directory

    def set_log_file(self, file_name):
        """
        Set the given file name as the log file that will be referenced when all the read and write functionalities are
            called.

        :param file_name: the name of the file that
        :return: None
        """
        self.file_name = file_name  # TODO: should this include the path or should that be determined by a relative path

    def read_journal_base_contents(self):
        """
        Read the base content dictionary placed at the beginning of the set yaml logging file. This dictionary should
            contain a simple mapping of names of entries, with their corresponding object type. The greater detail of
            the specific entries should be gathered using the read_log_entry function found in this class.

        :return: dictionary which contains all the journal entries in the set log file so that their individual contents
            may be read separately.
        """
        # TODO read the starting dictionary (need to also figure out a name for it for formatting purposes.)

    def save_log_entry(self, log):
        """
        Save all the data from the given log in yaml format by creating upper level yaml section using named
            identifier. This is intended to be used on individual entries and can be called by the larger system to
            save all entries in one functional call.

        :param log: dictionary of all relevant data that should be saved. Save file will be in yaml format
        :return: None
        """
        pass  # TODO: take dictionary and store all elements as entries in yaml file.

    def read_log_entry(self, entry):
        """
        Read the yaml formatted entry for the given entries name and convert it to the class type of the entry instance.
            This implementation is meant to be utilized for reading in the details of a single log entry from the log
            file. TODO only time a read may be done is in the start of main. maybe not needed.


        :param entry: the entry instance whose contents are either blank or expected to be obsolescent and should be
            updated
        :return: dict containing all the relevant data found in the given entry. None type reference if the log
            entry could not be found from the given reference, or if the name of the entry given does not match in
            type/format to the given entry class.
        """