# This file implements a temperature converter application.
# Designed by Tuur Mellaerts
# Version: v0.1

# General imports
import tkinter as tk

def main():
    root = tk.Tk()

    root.title("Temperature Converter")

    label = tk.Label(text="Enter temperature")
    entry = tk.Entry()

    label.pack()
    entry.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
