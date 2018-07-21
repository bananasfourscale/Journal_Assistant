from Journal.Journal import Journal
from Journal.FileSystem.JournalFileLogger import JournalFileLogger
from Journal.Quest.MainQuest import MainQuest

if __name__ == '__main__':
    PlayerJournal = Journal()
    # todo: move all this shit to a simple gui framework.
    log_file = input("Please Enter the Full Path of the Journal File you Would Like to Load")
    JournalFileLogger.set_log_file(log_file=log_file)
