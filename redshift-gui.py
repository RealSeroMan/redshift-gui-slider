#!/usr/bin/env python3

import tkinter as tk
import subprocess

def apply_temperature(event):
    temp = int(float(scale.get()))
    subprocess.run(["redshift", "-x"])
    subprocess.run(["redshift", "-O", str(temp)])

root = tk.Tk()
root.title("Redshift Temperature Controller")

# Create the scale (without setting command immediately)
scale = tk.Scale(root, from_=3000, to=6500, orient="horizontal", length=400,
                 label="Color Temperature (Kelvin)")
scale.set(4500)  # Default starting temperature
scale.pack(padx=20, pady=20)

# Now bind mouse release event to the apply function
scale.bind("<ButtonRelease-1>", apply_temperature)

root.mainloop()
