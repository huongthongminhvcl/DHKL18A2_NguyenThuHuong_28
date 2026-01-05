## GCD và LCM

import tkinter as tk
import math

def calculate():
    m = int(entry_m.get())
    n = int(entry_n.get())
    if option.get() == "GCD":
        result = math.gcd(m, n)
        lbl_result.config(text=f"GCD(m, n) = {result}")
    else:
        result = abs(m*n) // math.gcd(m, n)
        lbl_result.config(text=f"LCM(m, n) = {result}")

window = tk.Tk()
window.title("tk")

tk.Label(window, text="Enter value of m:").grid(row=0, column=0)
entry_m = tk.Entry(window)
entry_m.grid(row=0, column=1)

tk.Label(window, text="Enter value of n:").grid(row=1, column=0)
entry_n = tk.Entry(window)
entry_n.grid(row=1, column=1)

option = tk.StringVar(value="GCD")
tk.OptionMenu(window, option, "GCD", "LCM").grid(row=2, column=1)

lbl_result = tk.Label(window, text="")
lbl_result.grid(row=3, column=1)

tk.Button(window, text="Validate", command=calculate).grid(row=4, column=1)

window.mainloop()
