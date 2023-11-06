import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from PIL import Image, ImageTk

root = ttk.Window(themename="morph")

image = Image.open("logo.png").resize((32,32))
image = ImageTk.PhotoImage(image)

name_label = ttk.Label(root, text="name", image=image)
name_label.grid(row=0, column=0)

name_label.config(font=("FiraCode", 20))

name_entry = ttk.Entry(root)
name_entry.grid(row=0, column=1)

exit_button = ttk.Button(root, text="exit", bootstyle=(INFO, OUTLINE))
exit_button.grid(row=1, column=0)

root.mainloop()
