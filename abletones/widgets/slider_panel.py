import ttkbootstrap as ttk


class SliderPanel(ttk.Frame):
    def __init__(self, container, name: str):
        super().__init__(container)
        self.parent = container

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=2)

        self.lbl_name = ttk.Label(
            self,
            text=name.upper(),
            justify="center",
            font=("Helvetica", 12),
            anchor="center",
        )
        self.lbl_name.grid(row=0, column=0, sticky="nsew")

        self.slider = ttk.Scale(
            self,
            from_=0,
            to=99,
            command=self.update,
        )
        self.slider.grid(row=1, column=0, sticky="nsew")

    def update(self, value):
        self.parent.update_text()

    def get(self):
        return self.slider.get()
