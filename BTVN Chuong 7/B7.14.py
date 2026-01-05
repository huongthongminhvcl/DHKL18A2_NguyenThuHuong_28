## TÍNH CƯỚC TAXI (GUI)

import tkinter as tk
from tkinter import messagebox

def tinh_tien():
    try:
        km = float(entry_km.get())
        phut_cho = int(entry_phut.get())
        loai_xe = xe.get()

        if loai_xe == 4:
            mo_cua = 11000
            gia_30 = 15300
            gia_sau_30 = 12100
        else:
            mo_cua = 12000
            gia_30 = 16100
            gia_sau_30 = 13800

        tien = mo_cua

        if km > 0.8:
            km_con = km - 0.8
            if km_con <= 30:
                tien += km_con * gia_30
            else:
                tien += 30 * gia_30 + (km_con - 30) * gia_sau_30

        if phut_cho > 5:
            tien += (phut_cho - 5) * 7500

        lbl_kq.config(text=f"Tổng tiền: {int(tien):,} đồng")

    except:
        messagebox.showerror("Lỗi", "Dữ liệu không hợp lệ")

root = tk.Tk()
root.title("Tính cước taxi")

tk.Label(root, text="Số km:").grid(row=0, column=0)
entry_km = tk.Entry(root)
entry_km.grid(row=0, column=1)

tk.Label(root, text="Phút chờ:").grid(row=1, column=0)
entry_phut = tk.Entry(root)
entry_phut.grid(row=1, column=1)

xe = tk.IntVar(value=4)
tk.Radiobutton(root, text="Xe 4 chỗ", variable=xe, value=4).grid(row=2, column=0)
tk.Radiobutton(root, text="Xe 7 chỗ", variable=xe, value=7).grid(row=2, column=1)

tk.Button(root, text="Tính tiền", command=tinh_tien).grid(row=3, column=0, columnspan=2)

lbl_kq = tk.Label(root, text="")
lbl_kq.grid(row=4, column=0, columnspan=2)

root.mainloop()
