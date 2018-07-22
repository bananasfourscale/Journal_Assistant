#!/usr/bin/env python
from Journal.Journal import Journal
from Journal.FileSystem.JournalFileLogger import JournalFileLogger
from Journal.Quest.MainQuest import MainQuest
import tkinter as tk
from Journal.UserControls.Application import Application

if __name__ == '__main__':

    journal = Journal()
    file_system = JournalFileLogger()
    app = Application()
    app.mainloop()
    exit(0)

