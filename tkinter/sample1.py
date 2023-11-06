import tkinter as tk
from tkinter import ttk
root = tk.Tk()
# root.resizable(False, False)
root.title("blalalla")
# root.iconbitmap()
root.geometry("400x300")

def click():
    print("clicked")


# name = tk.Label(root, text="سلام", foreground="red",
#                 font=("Arial", 22), background="cyan", padx=100, pady=100)
# name.pack()
# family = ttk.Label(root, text="نام خانوادگی",
#                    padding=(20, 40), background="yellow")
# family.pack()

# my_button = tk.Button(root, text="click me!", font=(
#     "Arial", 22), background="cyan", padx=100, pady=100, command=click)
# my_button.pack()

# my_button = ttk.Button(root, text="click me!", padding=(40, 30))
# my_button.pack(side="left", fill="both", expand=True)
# quit_button = ttk.Button(
#     root, text="خروج", padding=(40, 30), command=root.destroy)
# quit_button.pack(side="left", fill="both", expand=True)

def my_function():
    print(f'hello {user_name.get()}')

user_name = tk.StringVar()

name_label = ttk.Label(root, text="Name:")
name_label.pack(side="left", padx=(0, 10))

name_entry = ttk.Entry(root, width=10, textvariable=user_name)
name_entry.pack(side="left")
name_entry.focus()



my_button = ttk.Button(root, text="click", command=my_function)
my_button.pack(side="left")
root.mainloop()
