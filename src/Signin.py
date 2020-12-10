'''
Họ và tên: Lưu Thanh Vân
MSSV: B1709639
STT: 63
'''

from tkinter import *
from tkinter import messagebox
import os.path
import pandas as pd
import numpy as np
import random
from Crypto.Hash import MD5, SHA1, SHA256, SHA512

'''
Length:
- md5: 32
- sha1: 40
- sha256: 64
- sha512: 128
'''

def userAuthentication(username, password):
    data = pd.read_csv("../data/database.csv", delimiter="\t", header=None)
    
    checked = False;
    usernameValues = data.iloc[:,0] # username column
    passwordValues = data.iloc[:,1] # password column

    # print(usernameValues)
    # print(passwordValues)

    for rowIndex in range(len(usernameValues)):
        name = usernameValues[rowIndex]
        passwd = passwordValues[rowIndex]

        if name == username:
            if len(passwd) == 32:
                if passwd == MD5.new(password).hexdigest().upper():
                    checked = True # successful user authentication
            elif len(passwd) == 40:
                if passwd == SHA1.new(password).hexdigest().upper():
                    checked = True
            elif len(passwd) == 64:
                if passwd == SHA256.new(password).hexdigest().upper():
                    checked = True
            elif len(passwd) == 128:
                if passwd == SHA512.new(password).hexdigest().upper():
                    checked = True
            
        if checked == True: break
    
    return checked # User authentication failed if checked = false

def handlingSigninEvent():
    username = txtUsername.get()
    password = txtPassword.get().encode()

    if userAuthentication(username, password) == True:
        messagebox.showinfo("Thông báo", "Đăng nhập thành công!")
    else:
        messagebox.showinfo("Thông báo", "Tên đăng nhập/Mật khẩu không đúng. Vui lòng nhập lại!")

# khoi tao man hinh chinh
window = Tk()
window.title("Welcome to Demo An toàn bảo mật thông tin")

# them cac control
lbHeader = Label(window, text=" ", font=("Arial Bold", 10))
lbHeader.grid(column=0, row=0)

lbTitle = Label(window, text="Đăng nhập", font=("Arial Bold", 20))
lbTitle.grid(column=1, row=1)

lbUsername = Label(window, text="Tên đăng nhập", font=("Arial", 14))
lbUsername.grid(column=0, row=3)
txtUsername = Entry(window, width=30)
txtUsername.grid(column=1, row=3)

lbPassword = Label(window, text="Mật khẩu", font=("Arial", 14))
lbPassword.grid(column=0, row=4)
txtPassword = Entry(window, width=30)
txtPassword.grid(column=1, row=4)

btnAccount = Button(window, text="Đăng nhập", command=handlingSigninEvent)
btnAccount.grid(column=1, row=5)

# hien thi cua so
window.geometry('500x200')
window.mainloop()
