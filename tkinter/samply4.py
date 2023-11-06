import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)


name_text = tk.StringVar()

name_label = ttk.Label(root, text="Name:", anchor="center")
name_label.grid(row=0, column=0, padx=(10, 10), sticky="ew")

name_entry = ttk.Entry(root, textvariable=name_text)
name_entry.grid(row=0, column=1, padx=(10, 10), sticky="ew")

exit_button = ttk.Button(root, text="exit", command=root.destroy)
exit_button.grid(row = 1, column=0, sticky="ew",padx=(10, 10))

run_button = ttk.Button(root, text="run", command=root.destroy)
run_button.grid(row = 1, column=1, sticky="ew",padx=(10, 10))

root.mainloop()
