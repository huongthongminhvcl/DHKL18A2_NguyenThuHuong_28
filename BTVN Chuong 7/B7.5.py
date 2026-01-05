## Đọc & hiển thị ảnh

import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Chuong trinh xem anh")

img = Image.open("Otto.png")
img = img.resize((500, 300))
photo = ImageTk.PhotoImage(img)

label = tk.Label(window, image=photo)
label.pack()

window.mainloop()
