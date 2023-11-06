import tkinter as tk
from tkinter import ttk

root = tk.Tk()
main = ttk.Frame(root)
main.pack(side="left", fill="both", expand=True)
tk.Label(main, text="label", bg="purple").pack(
    side="left", fill="both", expand=True)
tk.Label(main, text="label", bg="red").pack(
    side="top", fill="both", expand=True)


tk.Label(main, text="label", bg="blue").pack(
    side="top", fill="both", expand=True)


root.mainloop()
