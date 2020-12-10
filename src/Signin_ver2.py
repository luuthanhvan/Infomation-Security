from tkinter import *
from tkinter import messagebox
import os.path
import csv
import numpy as np
import random
from Crypto.Hash import MD5, SHA1, SHA256, SHA512

def kiemtra(tendangnhap, matkhau):
    file = open("CSDL.csv", mode="r")
    check = False;
    data = csv.reader(file, delimiter="\t")

    for row in data:
        ten = row[0] # lấy tên đăng nhập
        mk = row[1] # lấy mật khẩu

        if ten == tendangnhap:
            if len(mk) == 32:
                if mk == MD5.new(matkhau).hexdigest().upper():
                    check = True # successful user authentication
            elif len(mk) == 40:
                if mk == SHA1.new(matkhau).hexdigest().upper():
                    check = True
            elif len(mk) == 64:
                if mk == SHA256.new(matkhau).hexdigest().upper():
                    check = True
            elif len(mk) == 128:
                if mk == SHA512.new(matkhau).hexdigest().upper():
                    check = True
    
    file.close()
    return check

def dangnhap():
    tendangnhap = txtTendangnhap.get()
    matkhau = txtMatkhau.get().encode()

    if kiemtra(tendangnhap, matkhau) == True:
        messagebox.showinfo("Thông báo", "Đăng nhập thành công!")
    else:
        messagebox.showinfo("Thông báo", "Tên đăng nhập/Mật khẩu không đúng. Vui lòng nhập lại!")
    

window = Tk()
window.title("Welcome to Demo An toàn bảo mật thông tin")

lbHeader = Label(window, text=" ", font=("Arial Bold", 10))
lbHeader.grid(column=0, row=0)

lbTitle = Label(window, text="Đăng nhập", font=("Arial Bold", 20))
lbTitle.grid(column=1, row=1)

lbTendangnhap = Label(window, text="Tên đăng nhập", font=("Arial", 14))
lbTendangnhap.grid(column=0, row=3)
txtTendangnhap = Entry(window, width=30)
txtTendangnhap.grid(column=1, row=3)

lbMatkhau = Label(window, text="Mật khẩu", font=("Arial", 14))
lbMatkhau.grid(column=0, row=4)
txtMatkhau = Entry(window, width=30)
txtMatkhau.grid(column=1, row=4)

btnTaotaikhoan = Button(window, text="Đăng nhập", command=dangnhap)
btnTaotaikhoan.grid(column=1, row=5)

# hien thi cua so
window.geometry('500x200')
window.mainloop()
