import json
import tkinter as tk
from tkinter import messagebox

# Define color scheme
color_scheme = {
    "bg_color": "#505693",
    "fg_color": "#39406e",
    "button_fg_color": "#e4ecf3",
    "button_bg_color": "#354888",
    "button_hover_color": "#3b4e8e",
    "label_text_color": "#e4ecf3",
    "entry_bg_color": "#7083b4",
}

parts_list = []
transaction_records = []

def add_part():
    part_number = entry_part_number.get()
    part_description = entry_part_description.get()
    part_price = entry_price.get()
    
    parts_list.append((part_number, part_description, part_price))
    transaction_records.append(f"Operation: A, Part number: {part_number}")

    # Load existing data from the JSON file
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {"parts_list": [], "transaction_records": []}

    # Append new data to the existing data
    data["parts_list"].append((part_number, part_description, part_price))
    data["transaction_records"].append(f"Operation: A, Part number: {part_number}")

    # Write the updated data back to the JSON file
    with open('data.json', 'w') as f:
        json.dump(data, f)

    entry_part_number.delete(0, tk.END)
    entry_part_description.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    
    entry_part_number.focus()

def confirm():
    # Load existing data from the JSON file
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {"parts_list": [], "transaction_records": []}

    parts_list = data["parts_list"]
    transaction_records = data["transaction_records"]

    # Open the new window with menu options
    menu_window = tk.Toplevel(root)
    menu_window.title("Menu")
    menu_window.configure(bg=color_scheme["bg_color"])

    # Add and Change Part Section
    label_add_part = tk.Label(menu_window, text="Add Part", fg=color_scheme["label_text_color"], bg=color_scheme["bg_color"])
    label_add_part.grid(row=0, column=0, padx=10, pady=5)

    button_add_part = tk.Button(menu_window, text="[A] Add", command=lambda: add_another_part(menu_window),
                                fg=color_scheme["button_fg_color"], bg=color_scheme["button_bg_color"],
                                activebackground=color_scheme["button_hover_color"])
    button_add_part.grid(row=1, column=0, padx=10, pady=5)

    label_change_part = tk.Label(menu_window, text="Change Part", fg=color_scheme["label_text_color"], bg=color_scheme["bg_color"])
    label_change_part.grid(row=0, column=1, padx=10, pady=5)

    button_change_part = tk.Button(menu_window, text="[C] Change", command=lambda: open_change_part_window(menu_window),
                                   fg=color_scheme["button_fg_color"], bg=color_scheme["button_bg_color"],
                                   activebackground=color_scheme["button_hover_color"])
    button_change_part.grid(row=1, column=1, padx=10, pady=5)

    # Delete and Exit Part Section
    label_delete_part = tk.Label(menu_window, text="Delete Part", fg=color_scheme["label_text_color"], bg=color_scheme["bg_color"])
    label_delete_part.grid(row=2, column=0, padx=10, pady=5)

    button_delete_part = tk.Button(menu_window, text="[D] Delete", command=lambda: open_delete_window(menu_window),
                                   fg=color_scheme["button_fg_color"], bg=color_scheme["button_bg_color"],
                                   activebackground=color_scheme["button_hover_color"])
    button_delete_part.grid(row=3, column=0, padx=10, pady=5)

    label_exit_program = tk.Label(menu_window, text="Exit the program", fg=color_scheme["label_text_color"], bg=color_scheme["bg_color"])
    label_exit_program.grid(row=2, column=1, padx=10, pady=5)

    button_exit_program = tk.Button(menu_window, text="[X] Exit", command=root.quit,
                                    fg=color_scheme["button_fg_color"], bg=color_scheme["button_bg_color"],
                                    activebackground=color_scheme["button_hover_color"])
    button_exit_program.grid(row=3, column=1, padx=10, pady=5)

def open_change_part_window(parent_window):
    parent_window.destroy()
    change_window = tk.Toplevel(root)
    change_window.title("Change Part")
    change_window.configure(bg=color_scheme["bg_color"])

    label = tk.Label(change_window, text="Enter the part number you want to change: ", fg=color_scheme["label_text_color"], bg=color_scheme["bg_color"])
    label.grid(row=0, column=0, padx=10, pady=5)

    entry_change_part_number = tk.Entry(change_window, bg=color_scheme["entry_bg_color"])
    entry_change_part_number.grid(row=0, column=1, padx=10, pady=5)

    button_change_description = tk.Button(change_window, text="Change Description", command=lambda: open_change_description_window(change_window),
                                          fg=color_scheme["button_fg_color"], bg=color_scheme["button_bg_color"],
                                          activebackground=color_scheme["button_hover_color"])
    button_change_description.grid(row=1, column=0, padx=10, pady=5)

    button_change_price = tk.Button(change_window, text="Change Price", command=lambda: open_change_price_window(change_window),
                                    fg=color_scheme["button_fg_color"], bg=color_scheme["button_bg_color"],
                                    activebackground=color_scheme["button_hover_color"])
    button_change_price.grid(row=1, column=1, padx=10, pady=5)

    button_change_both = tk.Button(change_window, text="Change Both", command=lambda: open_change_both_window(change_window),
                                   fg=color_scheme["button_fg_color"], bg=color_scheme["button_bg_color"],
                                   activebackground=color_scheme["button_hover_color"])
    button_change_both.grid(row=1, column=2, padx=10, pady=5)

def open_change_description_window(parent_window):
    parent_window.destroy()
    description_window = tk.Toplevel(root)
    description_window.title("Change Description")
    description_window.configure(bg=color_scheme["bg_color"])

    label = tk.Label(description_window, text="Change part description: ", fg=color_scheme["label_text_color"], bg=color_scheme["bg_color"])
    label.grid(row=0, column=0, padx=10, pady=5)

    entry_new_description = tk.Entry(description_window, bg=color_scheme["entry_bg_color"])
    entry_new_description.grid(row=0, column=1, padx=10, pady=5)

    button_confirm = tk.Button(description_window, text="Confirm", command=description_window.destroy,
                               fg=color_scheme["button_fg_color"], bg=color_scheme["button_bg_color"],
                               activebackground=color_scheme["button_hover_color"])
    button_confirm.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

def open_change_price_window(parent_window):
    parent_window.destroy()
    price_window = tk.Toplevel(root)
    price_window.title("Change Price")
    price_window.configure(bg=color_scheme["bg_color"])

    label = tk.Label(price_window, text="Change part price: ", fg=color_scheme["label_text_color"], bg=color_scheme["bg_color"])
    label.grid(row=0, column=0, padx=10, pady=5)

    entry_new_price = tk.Entry(price_window, bg=color_scheme["entry_bg_color"])
    entry_new_price.grid(row=0, column=1, padx=10, pady=5)

    button_confirm = tk.Button(price_window, text="Confirm", command=price_window.destroy,
                               fg=color_scheme["button_fg_color"], bg=color_scheme["button_bg_color"],
                               activebackground=color_scheme["button_hover_color"])
    button_confirm.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

def open_change_both_window(parent_window):
    parent_window.destroy()
    both_window = tk.Toplevel(root)
    both_window.title("Change Both")
    both_window.configure(bg=color_scheme["bg_color"])

    label_desc = tk.Label(both_window, text="Change part description: ", fg=color_scheme["label_text_color"], bg=color_scheme["bg_color"])
    label_desc.grid(row=0, column=0, padx=10, pady=5)

    entry_new_description = tk.Entry(both_window, bg=color_scheme["entry_bg_color"])
    entry_new_description.grid(row=0, column=1, padx=10, pady=5)

    label_price = tk.Label(both_window, text="Change part price: ", fg=color_scheme["label_text_color"], bg=color_scheme["bg_color"])
    label_price.grid(row=1, column=0, padx=10, pady=5)

    entry_new_price = tk.Entry(both_window, bg=color_scheme["entry_bg_color"])
    entry_new_price.grid(row=1, column=1, padx=10, pady=5)

    button_confirm = tk.Button(both_window, text="Confirm", command=both_window.destroy,
                               fg=color_scheme["button_fg_color"], bg=color_scheme["button_bg_color"],
                               activebackground=color_scheme["button_hover_color"])
    button_confirm.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

def open_delete_window(parent_window):
    parent_window.destroy()
    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Part")
    delete_window.configure(bg=color_scheme["bg_color"])

    label = tk.Label(delete_window, text="Enter the part number you want to delete: ", fg=color_scheme["label_text_color"], bg=color_scheme["bg_color"])
    label.grid(row=0, column=0, padx=10, pady=5)

    entry_delete_part_number = tk.Entry(delete_window, bg=color_scheme["entry_bg_color"])
    entry_delete_part_number.grid(row=0, column=1, padx=10, pady=5)

    button_confirm = tk.Button(delete_window, text="Confirm", command=lambda: delete_part(delete_window, entry_delete_part_number.get()),
                               fg=color_scheme["button_fg_color"], bg=color_scheme["button_bg_color"],
                               activebackground=color_scheme["button_hover_color"])
    button_confirm.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

def delete_part(window, part_number):
    global parts_list

    # Load existing data from the JSON file
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {"parts_list": [], "transaction_records": []}

    # Update the parts_list and transaction_records in memory
    parts_list = [part for part in parts_list if part[0] != part_number]
    transaction_records.append(f"Operation: D, Part number: {part_number}")

    # Update the parts_list and transaction_records in the JSON file
    data["parts_list"] = [part for part in data["parts_list"] if part[0] != part_number]
    data["transaction_records"].append(f"Operation: D, Part number: {part_number}")

    with open('data.json', 'w') as f:
        json.dump(data, f)

    window.destroy()

def open_transaction_records(parent_window=None):
    # Load existing data from the JSON file
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {"parts_list": [], "transaction_records": []}

    parts_list = data["parts_list"]
    transaction_records = data["transaction_records"]

    if parent_window:
        parent_window.destroy()
    transaction_window = tk.Toplevel(root)
    transaction_window.title("Transaction Records")
    transaction_window.configure(bg=color_scheme["bg_color"])

    row = 0
    for part in parts_list:
        label = tk.Label(transaction_window, text=f"Part number: {part[0]}, Description: {part[1]}, Price: {part[2]}", fg=color_scheme["label_text_color"], bg=color_scheme["bg_color"])
        label.grid(row=row, column=0, padx=10, pady=5)
        row += 1

    label_records = tk.Label(transaction_window, text="Transaction Records:", fg=color_scheme["label_text_color"], bg=color_scheme["bg_color"])
    label_records.grid(row=row, column=0, padx=10, pady=5)
    row += 1
    
    for record in transaction_records:
        label = tk.Label(transaction_window, text=record, fg=color_scheme["label_text_color"], bg=color_scheme["bg_color"])
        label.grid(row=row, column=0, padx=10, pady=5)
        row += 1

    button_exit = tk.Button(transaction_window, text="Exit", command=transaction_window.destroy,
                            fg=color_scheme["button_fg_color"], bg=color_scheme["button_bg_color"],
                            activebackground=color_scheme["button_hover_color"])
    button_exit.grid(row=row, column=0, padx=10, pady=10)
    
def add_another_part(menu_window):
    menu_window.destroy()
    
    entry_part_number.delete(0, tk.END)
    entry_part_description.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    
    entry_part_number.focus()

# Create the main window
root = tk.Tk()
root.title("Inventory")
root.configure(bg=color_scheme["bg_color"])

# Part Number
label_part_number = tk.Label(root, text="Please enter a part number: ", fg=color_scheme["label_text_color"], bg=color_scheme["bg_color"])
label_part_number.grid(row=0, column=0, padx=10, pady=5)

entry_part_number = tk.Entry(root, bg=color_scheme["entry_bg_color"])
entry_part_number.grid(row=0, column=1, padx=10, pady=5)

# Part Description
label_part_description = tk.Label(root, text="Enter part Description: ", fg=color_scheme["label_text_color"], bg=color_scheme["bg_color"])
label_part_description.grid(row=1, column=0, padx=10, pady=5)

entry_part_description = tk.Entry(root, bg=color_scheme["entry_bg_color"])
entry_part_description.grid(row=1, column=1, padx=10, pady=5)

# Price
label_price = tk.Label(root, text="Enter Price: ", fg=color_scheme["label_text_color"], bg=color_scheme["bg_color"])
label_price.grid(row=2, column=0, padx=10, pady=5)

entry_price = tk.Entry(root, bg=color_scheme["entry_bg_color"])
entry_price.grid(row=2, column=1, padx=10, pady=5)

# Buttons
button_add_part = tk.Button(root, text="Add Part", command=add_part, fg=color_scheme["button_fg_color"], bg=color_scheme["button_bg_color"],
                            activebackground=color_scheme["button_hover_color"])
button_add_part.grid(row=3, column=0, padx=10, pady=10)

button_confirm = tk.Button(root, text="Menu", command=confirm, fg=color_scheme["button_fg_color"], bg=color_scheme["button_bg_color"],
                           activebackground=color_scheme["button_hover_color"])
button_confirm.grid(row=3, column=1, padx=10, pady=10)

button_transactions = tk.Button(root, text="Transactions", command=open_transaction_records, fg=color_scheme["button_fg_color"], bg=color_scheme["button_bg_color"],
                                activebackground=color_scheme["button_hover_color"])
button_transactions.grid(row=3, column=2, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
