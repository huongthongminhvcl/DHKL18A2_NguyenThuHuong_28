## Năm dương đến năm âm lịch

import tkinter as tk

can = ["Giáp","Ất","Bính","Đinh","Mậu","Kỷ","Canh","Tân","Nhâm","Quý"]
chi = ["Tý","Sửu","Dần","Mão","Thìn","Tỵ","Ngọ","Mùi","Thân","Dậu","Tuất","Hợi"]

def convert():
    year = int(entry.get())
    lbl_result.config(text=can[year % 10] + " " + chi[year % 12])

window = tk.Tk()
window.title("tk")

tk.Label(window, text="Enter solar year:").grid(row=0, column=0)
entry = tk.Entry(window)
entry.grid(row=0, column=1)

lbl_result = tk.Label(window, text="")
lbl_result.grid(row=1, column=1)

tk.Button(window, text="Validate", command=convert).grid(row=2, column=1)

window.mainloop()


