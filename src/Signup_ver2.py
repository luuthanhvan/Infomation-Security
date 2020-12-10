from tkinter import *
from tkinter import messagebox
import os.path
import csv
import numpy as np
import random
from Crypto.Hash import MD5, SHA1, SHA256, SHA512

def ghifile(data):
    file = open("CSDL.csv", mode="a")
    try:
        database_writer = csv.writer(file, delimiter='\t')
        database_writer.writerow(data)
    finally:
        file.close()

def kiemtra(tendangnhap):
    file = open("CSDL.csv", mode="r")

    data = csv.reader(file, delimiter="\t")
    for row in data:
        ten = row[0] # lấy tên đăng nhập
        
        if ten == tendangnhap:
            return True # tên đăng nhập đã tồn tại
    
    file.close()

    return False

def dangky():
    tendangnhap = txtTendangnhap.get()
    matkhau = txtMatkhau.get().encode()

    func = np.random.randint(4)

    if func == 0:
        mkDuocMaHoa = MD5.new(matkhau).hexdigest().upper()
    elif func == 1:
        mkDuocMaHoa = SHA1.new(matkhau).hexdigest().upper()
    elif func == 2:
        mkDuocMaHoa = SHA256.new(matkhau).hexdigest().upper()
    elif func == 3:
        mkDuocMaHoa = SHA512.new(matkhau).hexdigest().upper()
    
    if os.path.isfile("CSDL.csv"):
        if kiemtra(tendangnhap) == True:
            messagebox.showinfo("Thông báo", "Tên đăng nhập đã tồn tại!")
            return
        
        data = [tendangnhap, mkDuocMaHoa]
        ghifile(data)
        messagebox.showinfo("Thông báo", "Bạn đã tạo tài khoản thành công!")

    else:
        with open("CSDL.csv", mode="w") as csdl:
            database_writer = csv.writer(csdl, delimiter='\t')
            database_writer.writerow([tendangnhap, mkDuocMaHoa])
        
        messagebox.showinfo("Thông báo", "Bạn đã tạo tài khoản thành công!")
    

window = Tk()
window.title("Welcome to Demo An toàn bảo mật thông tin")

lbHeader = Label(window, text=" ", font=("Arial Bold", 10))
lbHeader.grid(column=0, row=0)

lbTitle = Label(window, text="Tạo tài khoản", font=("Arial Bold", 20))
lbTitle.grid(column=1, row=1)

lbTendangnhap = Label(window, text="Tên đăng nhập", font=("Arial", 14))
lbTendangnhap.grid(column=0, row=3)
txtTendangnhap = Entry(window, width=30)
txtTendangnhap.grid(column=1, row=3)

lbMatkhau = Label(window, text="Mật khẩu", font=("Arial", 14))
lbMatkhau.grid(column=0, row=4)
txtMatkhau = Entry(window, width=30)
txtMatkhau.grid(column=1, row=4)

btnTaotaikhoan = Button(window, text="Tạo tài khoản", command=dangky)
btnTaotaikhoan.grid(column=1, row=5)

# hien thi cua so
window.geometry('500x200')
window.mainloop()
