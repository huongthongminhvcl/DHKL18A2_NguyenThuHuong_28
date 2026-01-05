## Đảo ngược chuỗi

import tkinter as tk

def reverse_text():
    s = entry.get()
    result = ""
    for i in range(len(s)-1, -1, -1):
        result += s[i]
    lbl_result.config(text=result)

window = tk.Tk()
window.title("tk")

tk.Label(window, text="Enter a word:").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(window, width=30)
entry.grid(row=0, column=1)

lbl_result = tk.Label(window, text="")
lbl_result.grid(row=1, column=1)

btn = tk.Button(window, text="Validate", command=reverse_text)
btn.grid(row=2, column=1, pady=10)

window.mainloop()
