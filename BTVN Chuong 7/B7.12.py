## TÍNH CHỈ SỐ BMI (GUI)

# Yêu cầu
# Nhập cân nặng (kg)
# Nhập chiều cao (m)
# Nhấn nút tính BMI
# Hiển thị BMI + kết luận

import tkinter as tk
from tkinter import messagebox

def tinh_bmi():
    try:
        can_nang = float(entry_can_nang.get())
        chieu_cao = float(entry_chieu_cao.get())

        bmi = can_nang / (chieu_cao ** 2)

        if bmi < 18.5:
            ket_luan = "Gầy"
        elif bmi < 25:
            ket_luan = "Bình thường"
        elif bmi < 30:
            ket_luan = "Thừa cân"
        else:
            ket_luan = "Béo phì"

        lbl_kq.config(text=f"BMI: {bmi:.2f}\nKết luận: {ket_luan}")
    except:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ")

root = tk.Tk()
root.title("BMI Calculator")

tk.Label(root, text="Cân nặng (kg):").pack()
entry_can_nang = tk.Entry(root)
entry_can_nang.pack()

tk.Label(root, text="Chiều cao (m):").pack()
entry_chieu_cao = tk.Entry(root)
entry_chieu_cao.pack()

tk.Button(root, text="Tính BMI", command=tinh_bmi).pack(pady=5)

lbl_kq = tk.Label(root, text="")
lbl_kq.pack()

root.mainloop()
