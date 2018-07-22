#!/usr/bin/env python
from Journal.Journal import Journal
from Journal.FileSystem.JournalFileLogger import JournalFileLogger
from Journal.Quest.MainQuest import MainQuest
import tkinter as tk
from Journal.UserControls.Application import Application

if __name__ == '__main__':

    journal = Journal()
    file_system = JournalFileLogger()
    # todo: move all this shit to a simple gui framework.
    log_file = input("Please Enter the Full Path of the Journal File you Would Like to Load")
    file_system.set_log_file(file_name=log_file)
    app = Application()
    app.mainloop()
    exit(0)

