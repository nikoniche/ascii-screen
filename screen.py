import os
from io import StringIO
import numpy as np
from tkinter import *
import time
import json
from screenshot_to_ascii import convert_screenshot_to_ascii

FONT_NAME = "Consolas"

# WINDOW_WIDTH, WINDOW_HEIGHT = 960, 540
WINDOW_WIDTH, WINDOW_HEIGHT = 1024, 576

class Screen(Tk):

    def __init__(self):
        # setting up tkinter
        super(Screen, self).__init__()
        self.title("Screen to ASCII")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{10}+{10}")
        self.resizable(False, False)

        self.text = ""
        for y in range(42):
            for x in range(159):
                self.text += "X"
            self.text += "\n"

        # frame used to set content size with pixels
        self.content_frame = Frame(self, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="black")
        self.content_frame.pack()

        self.content = Label(self.content_frame, bg="black", fg="white",
                             text="Characterized", font=("Consolas", 2))
        self.content.place(x=0, y=2, width=WINDOW_WIDTH, height=WINDOW_HEIGHT+10)

        self.after(1, self._draw)

    def _draw(self) -> None:
        """Draws a single frame at a time."""

        start_time = time.time()

        text = convert_screenshot_to_ascii()
        self.content.config(text=text)
        took = time.time() - start_time
        print(took)
        print(1/took)

        self.after(1, self._draw)
