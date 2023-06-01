import tkinter as tk
from PIL import Image, ImageTk

class Theme:
    def __init__(self, root):
        self.root = root
        self.night_mode = False

        image = Image.open("images/sun.png")
        image = image.resize((32, 32), Image.ANTIALIAS)
        self.sun_image = ImageTk.PhotoImage(image)
        image = Image.open("images/moon.png")
        image = image.resize((32, 32), Image.ANTIALIAS)
        self.moon_image = ImageTk.PhotoImage(image)

        self.mode_button = tk.Button(self.root, image=self.moon_image, command=self.change_mode, bg="white", bd=0)
        self.mode_button.place(x=10, y=10)

        self.components = []

    def add(self, component, attr, day_value, night_value=None):
        if night_value is None:
            night_value = day_value
        self.components.append((component, attr, day_value, night_value))
        self.update()

    def change_mode(self):
        self.night_mode = not self.night_mode
        self.mode_button.config(image=self.sun_image if self.night_mode else self.moon_image)
        self.update()

    def update(self):
        bg_color = "#000000" if self.night_mode else "white"
        self.root.configure(bg=bg_color)
        self.mode_button.configure(bg=bg_color)
        for component, attr, day_value, night_value in self.components:
            value = night_value if self.night_mode else day_value
            component.configure(**{attr: value})
