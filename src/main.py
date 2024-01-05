# This file implements a temperature converter application.
# Designed by Tuur Mellaerts
# Version: v0.2
# Date: 05/01/2024

# General imports
import tkinter as tk

# Function to convert Celsius to Fahrenheit
def convertCtoF(celsius):
    fahrenheit = celsius * (9/5) + 32
    return fahrenheit

# Function to convert Fahrenheit to Celsius
def convertFtoC(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    return celsius

# Main function
def main():
    root = tk.Tk()

    root.title("Temperature Converter")

    label = tk.Label(text="Enter temperature")
    entry = tk.Entry()

    label.pack()
    entry.pack()

    root.mainloop()

# Start-up function
if __name__ == "__main__":
    main()
