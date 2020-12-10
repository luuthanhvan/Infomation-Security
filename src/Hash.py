'''
Họ và tên: Lưu Thanh Vân
MSSV: B1709639
STT: 63
'''

from tkinter import *
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import MD5, SHA1, SHA256, SHA512
from Crypto.Cipher import PKCS1_v1_5
import base64

def hashing():
    content = txtPlainText.get().encode()
    func = hashmode.get()

    if func == 0:
        result = MD5.new(content)
    if func == 1:
        result = SHA1.new(content)
    if func == 2:
        result = SHA256.new(content)
    if func == 3:
        result = SHA512.new(content)
    
    result = result.hexdigest().upper()

    txtHash.delete(0, END)
    txtHash.insert(INSERT, result)

'''
print("md5:", len("15F3DB2508FC6676BF5F36C4B0E4409E"))
print("sha1:", len("EFC4E00D9DE3DD3034D0C11A2374A954FE18A264"))
print("sha256:", len("BC5326510E50C56342CD70CA36E41EC5D0500A8599CE2A708E04641428A3DD3D"))
print("sha512:", len("E01607FE985C6788A3BC5064330CC56B5289EC28226FE9981D4442DBABE4C1011A5B90CC4F5BAEA86544C0F669D869B19EE8158291DEF730ED80331E96675B84"))
'''

# khoi tao man hinh chinh
window = Tk()
window.title("Welcome to Demo An toàn bảo mật thông tin")

# them cac control
lbHeader = Label(window, text=" ", font=("Arial Bold", 10))
lbHeader.grid(column=0, row=0)

lbTitle = Label(window, text="Chương trình băm", font=("Arial Bold", 20))
lbTitle.grid(column=1, row=1)

lbPlainText = Label(window, text="Văn bản", font=("Arial", 14))
lbPlainText.grid(column=0, row=3)
txtPlainText = Entry(window, width=70)
txtPlainText.grid(column=1, row=3)

radioGroup = LabelFrame(window, text="Hàm băm")
radioGroup.grid(column=1, row=4)
hashmode = IntVar()
hashmode.set(-1)

md5Function = Radiobutton(radioGroup, text="Hash MD5", font=("Times New Roman", 11), variable=hashmode, value=0, command=hashing)
md5Function.grid(column=0, row=5)

sha1Function = Radiobutton(radioGroup, text="Hash SHA1", font=("Times New Roman", 11), variable=hashmode, value=1, command=hashing)
sha1Function.grid(column=0, row=6)

sha256Function = Radiobutton(radioGroup, text="Hash SHA256", font=("Times New Roman", 11), variable=hashmode, value=2, command=hashing)
sha256Function.grid(column=0, row=7)

sha512Function = Radiobutton(radioGroup, text="Hash SHA512", font=("Times New Roman", 11), variable=hashmode, value=3, command=hashing)
sha512Function.grid(column=0, row=8)


lbHash = Label(window, text="Giá trị băm", font=("Arial", 14))
lbHash.grid(column=0, row=9)
txtHash = Entry(window, width=70)
txtHash.grid(column=1, row=9)

# hien thi cua so
window.geometry('800x300')
window.mainloop()