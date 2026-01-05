## Liệt kê các ước của N

import tkinter as tk

def find_divisors():
    n = int(entry.get())
    divisors = ""
    for i in range(1, n+1):
        if n % i == 0:
            divisors += str(i) + " "
    lbl_result.config(text=f"The divisors of N: {divisors}")

window = tk.Tk()
window.title("tk")

tk.Label(window, text="Enter the value of N:").grid(row=0, column=0, padx=10)
entry = tk.Entry(window)
entry.grid(row=0, column=1)

lbl_result = tk.Label(window, text="")
lbl_result.grid(row=1, column=1)

tk.Button(window, text="Validate", command=find_divisors).grid(row=2, column=1, pady=10)

window.mainloop()
