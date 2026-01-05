## Nhập tên & tuổi, kiểm tra đủ 18

import tkinter as tk

def check_age():
    age = int(entry_age.get())
    if age >= 18:
        lbl_result.config(text="Bạn đã trưởng thành!")
    else:
        lbl_result.config(text="Bạn chưa đủ 18 tuổi")

window = tk.Tk()
window.title("tk")

tk.Label(window, text="Tên:").grid(row=0, column=0)
entry_name = tk.Entry(window)
entry_name.grid(row=0, column=1)

tk.Label(window, text="Tuổi:").grid(row=1, column=0)
entry_age = tk.Entry(window)
entry_age.grid(row=1, column=1)

lbl_result = tk.Label(window, text="")
lbl_result.grid(row=2, column=1)

tk.Button(window, text="Validate", command=check_age).grid(row=3, column=1)

window.mainloop()
