# ++
# 'Abletones'
# copyright (c) 2023 hexbenjamin
# full license available at /COPYING
# --

# > IMPORTS <
import ttkbootstrap as ttk

# from ttkbootstrap.colorutils import contrast_color, color_to_rgb

from tkinter import font as TkFont

import widgets as hbw


# > CLASSES <
class AbletonesApp(ttk.Window):
    def __init__(self, dark: bool = False):
        theme = "cyborg" if dark else "flatly"
        super().__init__(self, themename=theme)

        self.default_font = TkFont.nametofont("TkDefaultFont")
        self.default_font.configure(size=16, family="Helvetica")

        self.geometry("500x500")

        self.grid_columnconfigure(0, weight=1)

        self.selector = hbw.SelectorPanel(self)
        self.selector.grid(row=0, column=0, sticky="nsew")


# >> ENTRY
if __name__ == "__main__":
    app = AbletonesApp(dark=True)
    app.mainloop()
