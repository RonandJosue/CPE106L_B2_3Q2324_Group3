import tkinter as tk
from tkinter import filedialog

def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if filename:
        print("Selected file:", filename)

root = tk.Tk()
root.title("File Selection")

browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack(pady=10)

root.mainloop()
