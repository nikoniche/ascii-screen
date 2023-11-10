import os
from io import StringIO
import numpy as np
from tkinter import *
import time
import json

FONT_NAME = "Consolas"

WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900

# for moving the game screen to different side of the real pc screen
X_OFFSET, Y_OFFSET = 400, 50

class Screen(Tk):

    def __init__(self):
        # setting up tkinter
        super(Screen, self).__init__()
        self.title("Characterized")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{X_OFFSET}+{Y_OFFSET}")
        self.resizable(False, False)

        # frame used to set content size with pixels
        self.content_frame = Frame(self, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="black")
        self.content_frame.pack()

        self.grid = None
        self.content = None

        self.after(1, self._draw)

    def _draw(self) -> None:
        """Draws a single frame at a time."""
        self._render_grid()
        self.after(1, self._draw)
    def _render_grid(self) -> None:
        """Formats the screen grid into a string, which is then displayed in the main label."""

        # Array reshaping
        shape = self.grid.shape
        reshaped_grid = np.transpose(self.grid).reshape((shape[1], shape[0]))

        # Conversion to string using save-txt method
        temp_io = StringIO()
        np.savetxt(temp_io, reshaped_grid, delimiter='', fmt="%s")
        text = temp_io.getvalue()
        temp_io.close()

        # Putting the text into the main label
        self.content.config(text=text)
