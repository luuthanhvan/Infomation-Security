'''
Họ và tên: Lưu Thanh Vân
MSSV: B1709639
STT: 63
'''
from tkinter import *
from tkinter import filedialog
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5
import base64

def save_file(content, mode, title, fileTypes, defaultExtension):
    file = filedialog.asksaveasfile(mode=mode, initialdir = "../data", title=title, filetypes=fileTypes, defaultextension=defaultExtension)
    if file is None:
        return
    file.write(content)
    file.close()

def generateKey():
    key = RSA.generate(1024)
    pri = save_file(key.exportKey("PEM"), "wb", "Lưu khóa cá nhân", (("All files", "*.*"), ("PEM files", "*.pem")), ".pem")
    pub = save_file(key.publickey().exportKey("PEM"), "wb", "Lưu khóa công khai", (("All files", "*.*"), ("PEM files", "*.pem")), ".pem")

    txtPrivateKey.insert(INSERT, key.exportKey("PEM"))

    txtPublicKey.insert(INSERT, key.publickey().exportKey("PEM"))

def getKey(keyStyle):
    fileName = filedialog.askopenfilename(initialdir = "../data", title="Open " + keyStyle, filetypes=(("PEM files", "*.pem"), ("All files", "*.*")))
    
    if fileName is None:
        return

    file = open(fileName, "r")
    key = file.read()
    file.close()

    return RSA.importKey(key)

def encryptRSA():
    txt = txtPlainText.get().encode()
    pubKey = getKey("Public Key")

    cipher = PKCS1_v1_5.new(pubKey)
    
    entxt = cipher.encrypt(txt)
    entxt = base64.b64encode(entxt)
    
    txtCipherText.delete(0, END)
    txtCipherText.insert(INSERT, entxt)

def decryptRSA():
    txt = txtCipherText.get()
    txt = base64.b64decode(txt)
    
    dsize = SHA.digest_size
    sentinel = Random.new().read(15+dsize)

    priKey = getKey("Private Key")
    cipher = PKCS1_v1_5.new(priKey)
    
    detxt = cipher.decrypt(txt, sentinel)

    txtDecipherText.delete(0, END)
    txtDecipherText.insert(INSERT, detxt)

# khoi tao man hinh chinh
window = Tk()
window.title("Welcome to Demo An Toàn Bảo Mật Thông Tin")

lbHeader = Label(window, text=" ", font=("Arial Bold", 10))
lbHeader.grid(column=0, row=0)

lbTitle = Label(window, text="CHƯƠNG TRÌNH DEMO", font=("Arial Bold", 20))
lbTitle.grid(column=1, row=1)

lbText = Label(window, text="MẬT MÃ BẤT ĐỐI XỨNG RSA", font=("Arial Bold", 16))
lbText.grid(column=1, row=2)

lbPlainText = Label(window, text="Văn bản gốc", font=("Arial Bold", 14))
lbPlainText.grid(column=0, row=3)
txtPlainText = Entry(window, width=50)
txtPlainText.grid(column=1, row=3)

lbCipherText = Label(window, text="Văn bản được mã hóa", font=("Arial Bold", 14))
lbCipherText.grid(column=0, row=4)
txtCipherText = Entry(window, width=50)
txtCipherText.grid(column=1, row=4)

lbDecipherText = Label(window, text="Văn bản được giải mã", font=("Arial Bold", 14))
lbDecipherText.grid(column=0, row=5)
txtDecipherText = Entry(window, width=50)
txtDecipherText.grid(column=1, row=5)

lbPrivateKey = Label(window, text="Khóa cá nhân", font=("Arial Bold", 14))
lbPrivateKey.grid(column=0, row=6)
txtPrivateKey = Text(window, width=50, height=5)
txtPrivateKey.grid(column=1, row=6)

lbPublicKey = Label(window, text="Khóa công khai", font=("Arial Bold", 14))
lbPublicKey.grid(column=0, row=7)
txtPublicKey = Text(window, width=50, height=5)
txtPublicKey.grid(column=1, row=7)

btnCreateKey = Button(window, text="Tạo khóa", command=generateKey)
btnCreateKey.grid(column=1, row=8)

btnEncrypt = Button(window, text="Mã hóa", command=encryptRSA)
btnEncrypt.grid(column=1, row=9)

btnDecrypt = Button(window, text="Giải mã", command=decryptRSA)
btnDecrypt.grid(column=1, row=10)

# hien thi cua so
window.geometry("700x600")
window.mainloop()