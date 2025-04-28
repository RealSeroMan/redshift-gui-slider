#!/usr/bin/env python3


import tkinter as tk
import subprocess

def set_temperature(value):
    temp = int(float(value))
    # Reset redshift first to avoid cumulative darkening
    subprocess.run(["redshift", "-x"])
    # Then apply new temperature
    subprocess.run(["redshift", "-O", str(temp)])

# Create main window
root = tk.Tk()
root.title("Redshift Temperature Controller")

# Create temperature slider
scale = tk.Scale(root, from_=3000, to=6500, orient="horizontal", length=400,
                 label="Color Temperature (Kelvin)", command=set_temperature)
scale.set(4500)  # Default starting temperature
scale.pack(padx=20, pady=20)

# Run the GUI
root.mainloop()

root.mainloop()
