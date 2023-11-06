import tkinter as tk
from tkinter import ttk
from utils import show_info


root = tk.Tk()
name = tk.StringVar()
family = tk.StringVar()
output = tk.StringVar()


name_frame = ttk.LabelFrame(root, text="name", padding=(20, 10, 20, 0))
name_frame.pack()

name_label = ttk.Label(name_frame, text="Name: ")
name_entry = ttk.Entry(name_frame, textvariable=name)

name_label.pack(side="left")
name_entry.pack(side="left", ipady = 5)


family_frame = ttk.LabelFrame(root, padding=(20, 10, 20, 0))
family_frame.pack()


family_label = ttk.Label(family_frame, text="family: ")
family_entry = ttk.Entry(family_frame, textvariable=family)

family_label.pack(side="left")
family_entry.pack(side="left", ipady = 5)


output_label = ttk.Label(root, textvariable=output)
output_label.pack()

buttons_frame = ttk.Frame(root)
buttons_frame.pack()

submit_button = ttk.Button(buttons_frame, text="Show Name", padding=(
    10, 10), command=lambda: show_info(output, name))
exit_button = ttk.Button(buttons_frame, text="exit",
                         padding=(10, 10), command=root.destroy)

submit_button.pack(side="left", padx=10, pady=10)
exit_button.pack(side="left", padx=10, pady=10)


root.mainloop()
