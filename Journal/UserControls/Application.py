#!/usr/bin/env python
# taken from user Steven Vascellaro on https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter

import tkinter as tk
from tkinter import font as tkfont
import ctypes

from Journal.FileSystem.JournalFileLogger import JournalFileLogger

file_sys = JournalFileLogger()
frame_width = ctypes.windll.user32.GetSystemMetrics(0)
frame_height = ctypes.windll.user32.GetSystemMetrics(1)


class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Western', size=22, weight="bold")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        window_size = "{}x{}".format(500, 500)
        self.geometry(window_size)
        container = tk.Frame(self, bg="black", height=frame_height, width=frame_width)
        container.pack_propagate(False)
        container.pack(side="top", fill=None, expand=False)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (TitlePage, LoadPage, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("TitlePage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class TitlePage(tk.Frame):

    def __init__(self, parent, controller):
        background_color = "#A1759B"
        tk.Frame.__init__(self, parent, height=frame_height, width=frame_width, bg=background_color)
        self.controller = controller
        self.pack_propagate(False)

        # Title
        title_label = tk.Label(self, text="Welcome To Journal Manager", font=controller.title_font,
                               bg=background_color)
        title_label.pack(side="top", fill="x", pady=10)

        # Spacing frame used to position the load button
        spacing_frame = tk.Frame(self, height=frame_height/5, bg=background_color)
        spacing_frame.pack()

        # Button used to transition to the journal load form
        load_button = tk.Button(self, text= "Load Journal",
                                command=lambda: controller.show_frame("LoadPage"),
                                height=4, width=16)
        load_button.pack()

        # Button used to exit the application
        quit_button_color = "#D91B1B"
        quit_button = tk.Button(self, text="QUIT",
                                command=controller.destroy,
                                bg=quit_button_color)
        quit_button.pack(side="bottom")


class LoadPage(tk.Frame):

    def __init__(self, parent, controller):
        background_color = "#A1759B"
        tk.Frame.__init__(self, parent, height=frame_height, width=frame_width, bg=background_color)
        self.controller = controller
        self.pack_propagate(False)

        # Spacer used to keep the search button from being against the top of the frame
        spacer_frame = tk.Frame(self, height=250, bg=background_color)
        spacer_frame.pack(side="top")

        # Button which can be used to open windows explorer to load a Journal file
        button = tk.Button(self, text="Search for File",
                           command=file_sys.read_journal_base_contents)
        button.pack(side="top")


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("MainMenu"))
        button.pack()
