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


def existedUser(username):
    data = pd.read_csv("../data/database.csv", delimiter="\t", header=None)
        
    usernameValues = data.iloc[:,0] # username column

    for rowIndex in range(len(usernameValues)):
        name = usernameValues[rowIndex]
        if name == username:
            return True # username existed
    
    return False # username didn't exist

def handlingSignupEvent():
    username = txtUsername.get()
    password = txtPassword.get().encode()

    # print(username)
    # print(password)
    func = np.random.randint(4) # generate a random integer from 0 to 3
    # print(func)
    
    if func == 0:
        passEncrypted = MD5.new(password)
    elif func == 1:
        passEncrypted = SHA1.new(password)
    elif func == 2:
        passEncrypted = SHA256.new(password)
    elif func == 3:
        passEncrypted = SHA512.new(password)

    passEncrypted = passEncrypted.hexdigest().upper()

    # print(passEncrypted)
    
    if os.path.isfile("../data/database.csv"):
        # print("File existed")
        if existedUser(username):
            messagebox.showinfo("Thông báo", "Tên đăng nhập đã tồn tại!")
            return

        userInfo = {
            'Username': username,
            'Password': passEncrypted
        }

        df = pd.DataFrame(userInfo, columns= ['Username', 'Password'], index=['Username'])
        df.to_csv("../data/database.csv", index=False, header=None, sep='\t', mode='a')
        messagebox.showinfo("Thông báo", "Bạn đã tạo tài khoản thành công!")

    else:
        # print("File did not exist")
        userInfo = {
            'Username': username,
            'Password': passEncrypted
        }

        df = pd.DataFrame(userInfo, columns= ['Username', 'Password'], index=['Username'])

        df.to_csv("../data/database.csv", index=False, header=None, sep='\t')

        messagebox.showinfo("Thông báo", "Bạn đã tạo tài khoản thành công!")

# khoi tao man hinh chinh
window = Tk()
window.title("Welcome to Demo An toàn bảo mật thông tin")

# them cac control
lbHeader = Label(window, text=" ", font=("Arial Bold", 10))
lbHeader.grid(column=0, row=0)

lbTitle = Label(window, text="Tạo tài khoản", font=("Arial Bold", 20))
lbTitle.grid(column=1, row=1)

lbUsername = Label(window, text="Tên đăng nhập", font=("Arial", 14))
lbUsername.grid(column=0, row=3)
txtUsername = Entry(window, width=30)
txtUsername.grid(column=1, row=3)

lbPassword = Label(window, text="Mật khẩu", font=("Arial", 14))
lbPassword.grid(column=0, row=4)
txtPassword = Entry(window, width=30)
txtPassword.grid(column=1, row=4)

btnAccount = Button(window, text="Tạo tài khoản", command=handlingSignupEvent)
btnAccount.grid(column=1, row=5)

# hien thi cua so
window.geometry('500x200')
window.mainloop()
