## Tính tổng 1 + 2 + … + N

import tkinter as tk

def calc_sum():
    n = int(entry.get())
    total = 0
    for i in range(1, n+1):
        total += i
    lbl_result.config(text=f"The sum is 1 + 2 + ... + {n} = {total}")

window = tk.Tk()
window.title("tk")

tk.Label(window, text="Enter value of integer N:").grid(row=0, column=0, padx=10)
entry = tk.Entry(window)
entry.grid(row=0, column=1)

lbl_result = tk.Label(window, text="")
lbl_result.grid(row=1, column=1)

tk.Button(window, text="Validate", command=calc_sum).grid(row=2, column=1, pady=10)

window.mainloop()
