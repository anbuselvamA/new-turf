import tkinter as tk
from tkinter import filedialog
import shutil
import os

try:
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Select the breathtaking Turf Image you want to use!",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.webp")]
    )

    if file_path:
        dest = r"c:\Users\anbua\Downloads\turfvadi\hero-bg.jpg"
        shutil.copy(file_path, dest)
        print("Image saved successfully as hero-bg.jpg!")
    else:
        print("User cancelled.")
except Exception as e:
    print(f"Error: {e}")
