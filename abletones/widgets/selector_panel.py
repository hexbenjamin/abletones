import ttkbootstrap as ttk

from .slider_panel import SliderPanel


class SelectorPanel(ttk.Frame):
    def __init__(self, container):
        options = {"padx": 12, "pady": 0}

        super().__init__(container)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)

        # self.l_var = ttk.IntVar(value=0)
        self.l_slider = SliderPanel(
            self,
            name="letter",
        )
        self.l_slider.grid(row=1, column=0, sticky="nsew", **options)

        # self.n_var = ttk.IntVar(value=0)
        self.n_slider = SliderPanel(
            self,
            name="number",
        )
        self.n_slider.grid(row=1, column=1, sticky="nsew", **options)

        self.txt = ttk.StringVar(value="SELECT: A0")
        self.submit = ttk.Button(
            self,
            textvariable=self.txt,
            bootstyle="SUCCESS-OUTLINE",
        )
        ttk.Style().configure("TButton", font=("Helvetica", 16, "bold"))
        self.submit.grid(row=0, column=0, columnspan=2, padx=16, pady=16, sticky="nsew")

    def update_text(self) -> None:
        letter = "ABCDE"[self.slider_parse(self.l_slider.get(), steps=5)]

        number = self.slider_parse(self.n_slider.get(), steps=14)

        self.txt.set(f"SELECT: {letter}{number}")
        self.update()

    def slider_parse(self, value: float, steps: int):
        interval = 100 / steps

        div, mod = divmod(value, interval)
        # div += 1 if mod > interval / 2 else 0
        return int(div)
