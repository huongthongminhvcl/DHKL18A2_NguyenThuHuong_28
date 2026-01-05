## WINDOW CÓ MENU

# Yêu cầu
# Tạo menu Chương 1 đến Chương 9
# Mỗi chương có các mục 1.1 đến 1.9
# Click Chương 1 đến 1.1 đến hiện thông báo:
# “Lập trình hướng đối tượng với nội dung là Giải phương trình bậc 2”

import tkinter as tk
from tkinter import messagebox

def thong_bao():
    messagebox.showinfo(
        "Lập trình hướng đối tượng",
        "Lập trình hướng đối tượng\nvới nội dung là Giải phương trình bậc 2"
    )

root = tk.Tk()
root.title("Chương trình Python nâng cao")
root.geometry("500x300")

menubar = tk.Menu(root)

for i in range(1, 10):
    menu_chuong = tk.Menu(menubar, tearoff=0)
    for j in range(1, 10):
        if i == 1 and j == 1:
            menu_chuong.add_command(label=f"{i}.{j}", command=thong_bao)
        else:
            menu_chuong.add_command(label=f"{i}.{j}")
    menubar.add_cascade(label=f"Chương {i}", menu=menu_chuong)

root.config(menu=menubar)
root.mainloop()
