import os
from io import StringIO
import numpy as np
from tkinter import *
import time
import json
from screenshot_to_ascii import convert_screenshot_to_ascii

FONT_NAME = "Consolas"

# WINDOW_WIDTH, WINDOW_HEIGHT = 960, 540
# WINDOW_WIDTH, WINDOW_HEIGHT, CONVERT_SIZE = 920, 620, 7
WINDOW_WIDTH, WINDOW_HEIGHT, CONVERT_SIZE = 1075, 728, 6
# WINDOW_WIDTH, WINDOW_HEIGHT, CONVERT_SIZE = 1800, 900, 5

class Screen(Tk):

    def __init__(self):
        # setting up tkinter
        super(Screen, self).__init__()
        self.title("Screen to ASCII")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{10}+{10}")
        # self.resizable(False, False)

        # frame used to set content size with pixels
        self.content_frame = Frame(self, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="black")
        self.content_frame.pack()

        self.content = Label(self.content_frame, bg="black", fg="white",
                             text="SCREEN TO ASCII", font=("Consolas", 2))
        self.content.place(x=0, y=0, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

        self.fps_label = Label(self.content_frame, bg="black", fg="white",
                             text="FPS: ___", font=("Consolas", 12))
        self.fps_label.place(x=62, y=0)

        self.invert_choice = BooleanVar(value=False)
        def wait(*_):
            time.sleep(0.1)
        self.invert_choice.trace("w", wait)
        self.check_button = Checkbutton(self.content_frame, text="Invert", variable=self.invert_choice, font=("Consolas", 12),
                                      bg="black", relief="ridge", fg="white")
        self.check_button.place(x=-22, y=0)

        self.after(1, self._draw)

    def _draw(self) -> None:
        """Draws a single frame at a time."""

        start_time = time.time()

        invert = self.invert_choice.get()
        text = convert_screenshot_to_ascii(CONVERT_SIZE, invert)
        self.content.config(text=text)
        took = time.time() - start_time
        self.fps_label.config(text=f"FPS: {round(1/took)}")

        self.after(1, self._draw)
