## Tạo cửa sổ Tkinter, đặt tiêu đề và thêm một nhãn (Label).

import tkinter as tk

window = tk.Tk()
window.title("Bài 7.2 - Label")

label = tk.Label(window, text="Xin chào Tkinter!")
label.pack(padx=20, pady=20)

window.mainloop()
