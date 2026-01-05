import tkinter as tk

window = tk.Tk()
window.title("tk")
window.geometry("500x250")

lbl_name = tk.Label(window, text="Student Name:")
lbl_name.grid(row=0, column=0, padx=20, pady=15, sticky="e")

entry_name = tk.Entry(window, width=30)
entry_name.grid(row=0, column=1, padx=10, pady=15)

lbl_id = tk.Label(window, text="Student ID:")
lbl_id.grid(row=1, column=0, padx=20, pady=15, sticky="e")

entry_id = tk.Entry(window, width=30)
entry_id.grid(row=1, column=1, padx=10, pady=15)

lbl_pass = tk.Label(window, text="Password:")
lbl_pass.grid(row=2, column=0, padx=20, pady=15, sticky="e")

entry_pass = tk.Entry(window, width=30, show="*")
entry_pass.grid(row=2, column=1, padx=10, pady=15)

btn_submit = tk.Button(window, text="Submit", width=10)
btn_submit.grid(row=3, column=1, pady=20)

window.mainloop()
