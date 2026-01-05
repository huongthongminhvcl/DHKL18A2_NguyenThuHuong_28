## Tạo nhãn và thay đổi kiểu phông chữ (tên phông, đậm, kích thước).

import tkinter as tk
from tkinter import font

window = tk.Tk()
window.title("Bài 7.3 - Font chữ")

my_font = font.Font(
    family="Arial",
    size=16,
    weight="bold"
)

label = tk.Label(window, text="Tkinter Font Demo", font=my_font)
label.pack(padx=20, pady=20)

window.mainloop()
