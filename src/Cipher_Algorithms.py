'''
Họ và tên: Lưu Thanh Vân
MSSV: B1709639
STT: 63
'''

from tkinter import *
from tkinter import filedialog
import tkinter as tk
from Crypto.Cipher import DES
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5
import base64

class MainWindow(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self)

        self.btnAffine = Button(text="Mã hóa Affine", font=("Time New Roman", 11), command=self.affine)
        self.btnAffine.pack()

        self.btnDES = Button(text="Mã hóa DES", font=("Time New Roman", 11), command=self.des)
        self.btnDES.pack()

        self.btnRSA = Button(text="Mã hóa RSA", font=("Time New Roman", 11), command=self.rsa)
        self.btnRSA.pack()

        self.btnExit = Button(text="Kết thúc", font=("Time New Roman", 11), command=quit)
        self.btnExit.pack()
    
    def affine(self):
        ENCRYPT_AFFINE(self)

    def des(self):
        ENCRYPT_DES(self)
    
    def rsa(self):
        ENCRYPT_RSA(self)

# encrypt
def charToNum(c):
    return (ord(c)-65)

def numToChar(n):
    return chr(n+65)

def encryptAffine(txt, a, b, m):
    r = ""
    for c in txt:
        e = (a*charToNum(c) + b) % m
        r = r + numToChar(e)
    return r

# decrypt
def xgcd(a, m):
    temp = m
    x0, x1, y0, y1 = 1, 0, 0, 1
    while m != 0:
        q, a, m = a // m, m, a % m
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    if x0 < 0:
        x0 = x0 + temp
    return x0

def decryptAffine(txt, a, b, m):
    r = ""
    a1 = xgcd(a, m)
    for c in txt:
        e = (a1 * (charToNum(c) - b)) % m
        r = r + numToChar(e)
    return r

class ENCRYPT_AFFINE(tk.Toplevel):
    def __init__(self, parent):
        self.parent = parent
        Toplevel.__init__(self)
        self.title("Chương trình mã hóa Affine")
        self.geometry("900x300")

        self.lbHeader = Label(self, text=" ", font=("Arial Bold", 10))
        self.lbHeader.grid(column=0, row=0)

        self.lbTitle = Label(self, text="CHƯƠNG TRÌNH DEMO", font=("Arial Bold", 20))
        self.lbTitle.grid(column=1, row=1)

        self.lbAffine = Label(self, text="MẬT MÃ AFFINE", font=("Arial Bold", 16))
        self.lbAffine.grid(column=0, row=2)

        self.lbPlainText = Label(self, text="PLAIN TEXT", font=("Arial", 14))
        self.lbPlainText.grid(column=0, row=3)
        self.txtPlainText = Entry(self, width=20)
        self.txtPlainText.grid(column=1, row=3)

        self.lbCipherText = Label(self, text="CIPHER TEXT", font=("Arial", 14))
        self.lbCipherText.grid(column=0, row=4)
        self.txtCipherText = Entry(self, width=20)
        self.txtCipherText.grid(column=1, row=4)

        self.lbKeyPair = Label(self, text="KEY PAIR", font=("Arial", 14))
        self.lbKeyPair.grid(column=2, row=3)

        self.txtKeyPairA = Entry(self, width=5)
        self.txtKeyPairA.grid(column=3, row=3)

        self.txtKeyPairB = Entry(self, width=5)
        self.txtKeyPairB.grid(column=4, row=3)

        self.btnEncrypt = Button(self, text="Mã hóa", command=self.encrypt)
        self.btnEncrypt.grid(column=5, row=3)

        self.btnDecrypt = Button(self, text="Giải mã", command=self.decrypt)
        self.btnDecrypt.grid(column=2, row=4)
        self.txtDecrypt = Entry(self, width=20)
        self.txtDecrypt.grid(column=3, row=4)

        self.btnBack = Button(self, text="Quay về màn hình chính", command=self.destroy)
        self.btnBack.grid(column=0, row=7)

    def encrypt(self):
        a = int(self.txtKeyPairA.get())
        b = int(self.txtKeyPairB.get())
        m = 26
        
        txt = self.txtPlainText.get()
        entxt = encryptAffine(txt, a, b, m)

        self.txtCipherText.delete(0, END)
        self.txtCipherText.insert(INSERT, entxt)

    def decrypt(self):
        a = int(self.txtKeyPairA.get())
        b = int(self.txtKeyPairB.get())
        m = 26

        txt = self.txtCipherText.get()
        detxt = decryptAffine(txt, a, b, m)

        self.txtDecrypt.delete(0, END)
        self.txtDecrypt.insert(INSERT, detxt)

def pad(s):
    return s + (8 - len(s) % 8) * chr(8 - len(s) % 8)

def unpad(s):
    return s[:-ord(s[len(s)-1:])]

class ENCRYPT_DES(tk.Toplevel):
    def __init__(self, parent):
        self.parent = parent
        Toplevel.__init__(self)
        self.title("Chương trình mã hóa đối xứng")
        self.geometry("800x400")

        self.lbTitle = Label(self, text="CHƯƠNG TRÌNH DEMO", font=("Arial Bold", 20))
        self.lbTitle.grid(column=1, row=1)

        self.lbName = Label(self, text="MẬT MÃ ĐỐI XỨNG DES", font=("Arial Bold", 15))
        self.lbName.grid(column=1, row=2)

        self.lbPlainText = Label(self, text="Văn bản gốc", font=("Arial Bold", 14))
        self.lbPlainText.grid(column=0, row=4)
        self.txtPlainText = Entry(self, width=70)
        self.txtPlainText.grid(column=1, row=4)

        self.lbKey = Label(self, text="Khóa", font=("Arial Bold", 14))
        self.lbKey.grid(column=0, row=5)
        self.txtKey = Entry(self, width=70)
        self.txtKey.grid(column=1, row=5)

        self.lbCipherText = Label(self, text="Văn bản được mã hóa", font=("Arial Bold", 14))
        self.lbCipherText.grid(column=0, row=6)
        self.txtCipherText = Entry(self, width=70)
        self.txtCipherText.grid(column=1, row=6)

        self.lbDecipherText = Label(self, text="Văn bản được giải mã", font=("Arial Bold", 14))
        self.lbDecipherText.grid(column=0, row=7)
        self.txtDecipherText = Entry(self, width=70)
        self.txtDecipherText.grid(column=1, row=7)

        self.btnEncrypt = Button(self, text="Mã hóa", command=self.encryptDES)
        self.btnEncrypt.grid(column=1, row=9)

        self.btnDecrypt = Button(self, text="Giải mã", command=self.decryptDES)
        self.btnDecrypt.grid(column=1, row=10)

        self.btnBack = Button(self, text="Quay về màn hình chính", command=self.destroy)
        self.btnBack.grid(column=1, row=11)
    
    def encryptDES(self):
        txt = pad(self.txtPlainText.get()).encode()
        key = pad(self.txtKey.get()).encode()

        cipher = DES.new(key, DES.MODE_ECB)
        entxt = cipher.encrypt(txt)
        entxt = base64.b64encode(entxt)

        self.txtCipherText.delete(0, END)
        self.txtCipherText.insert(INSERT, entxt)

    def decryptDES(self):
        txt = self.txtCipherText.get()
        txt = base64.b64decode(txt)
        key = pad(self.txtKey.get()).encode()
        
        cipher = DES.new(key, DES.MODE_ECB)
        detxt = unpad(cipher.decrypt(txt))

        self.txtDecipherText.delete(0, END)
        self.txtDecipherText.insert(INSERT, detxt)

def save_file(content, mode, title, fileTypes, defaultExtension):
    file = filedialog.asksaveasfile(mode=mode, initialdir = "../data", title=title, filetypes=fileTypes, defaultextension=defaultExtension)
    if file is None:
        return
    file.write(content)
    file.close()

def getKey(keyStyle):
    fileName = filedialog.askopenfilename(initialdir = "../data", title="Open " + keyStyle, filetypes=(("PEM files", "*.pem"), ("All files", "*.*")))
    
    if fileName is None:
        return

    file = open(fileName, "r")
    key = file.read()
    file.close()

    return RSA.importKey(key)

class ENCRYPT_RSA(tk.Toplevel):
    def __init__(self, parent):
        self.parent = parent
        Toplevel.__init__(self)
        self.title("Chương trình mã hóa RSA")
        self.geometry("800x500")

        self.lbTitle = Label(self, text="CHƯƠNG TRÌNH DEMO", font=("Arial Bold", 20))
        self.lbTitle.grid(column=1, row=1)

        self.lbName = Label(self, text="MẬT MÃ BẤT ĐỐI XỨNG RSA", font=("Arial Bold", 15))
        self.lbName.grid(column=1, row=2)

        self.lbPlainText = Label(self, text="Văn bản gốc", font=("Arial Bold", 14))
        self.lbPlainText.grid(column=0, row=4)
        self.txtPlainText = Entry(self, width=70)
        self.txtPlainText.grid(column=1, row=4)

        self.lbCipherText = Label(self, text="Văn bản được mã hóa", font=("Arial Bold", 14))
        self.lbCipherText.grid(column=0, row=5)
        self.txtCipherText = Entry(self, width=70)
        self.txtCipherText.grid(column=1, row=5)

        self.lbDecipherText = Label(self, text="Văn bản được giải mã", font=("Arial Bold", 14))
        self.lbDecipherText.grid(column=0, row=6)
        self.txtDecipherText = Entry(self, width=70)
        self.txtDecipherText.grid(column=1, row=6)

        self.lbPrivateKey = Label(self, text="Khóa cá nhân", font=("Arial Bold", 14))
        self.lbPrivateKey.grid(column=0, row=7)
        self.txtPrivateKey = Text(self, width=70, height=5)
        self.txtPrivateKey.grid(column=1, row=7)

        self.lbPublicKey = Label(self, text="Khóa công khai", font=("Arial Bold", 14))
        self.lbPublicKey.grid(column=0, row=8)
        self.txtPublicKey = Text(self, width=70, height=5)
        self.txtPublicKey.grid(column=1, row=8)

        self.btnCreateKey = Button(self, text="Tạo khóa", command=self.generateKey)
        self.btnCreateKey.grid(column=1, row=9)

        self.btnEncrypt = Button(self, text="Mã hóa", command=self.encryptRSA)
        self.btnEncrypt.grid(column=1, row=10)

        self.btnDecrypt = Button(self, text="Giải mã", command=self.decryptRSA)
        self.btnDecrypt.grid(column=1, row=11)

        self.btnBack = Button(self, text="Quay về màn hình chính", command=self.destroy)
        self.btnBack.grid(column=1, row=12)
    
    def generateKey(self):
        key = RSA.generate(1024)
        pri = save_file(key.exportKey("PEM"), "wb", "Lưu khóa cá nhân", (("All files", "*.*"), ("PEM files", "*.pem")), ".pem")
        pub = save_file(key.publickey().exportKey("PEM"), "wb", "Lưu khóa công khai", (("All files", "*.*"), ("PEM files", "*.pem")), ".pem")

        self.txtPrivateKey.insert(INSERT, key.exportKey("PEM"))

        self.txtPublicKey.insert(INSERT, key.publickey().exportKey("PEM"))

    def encryptRSA(self):
        txt = self.txtPlainText.get().encode()
        pubKey = getKey("Public Key")

        cipher = PKCS1_v1_5.new(pubKey)
        
        entxt = cipher.encrypt(txt)
        entxt = base64.b64encode(entxt)
        
        self.txtCipherText.delete(0, END)
        self.txtCipherText.insert(INSERT, entxt)

    def decryptRSA(self):
        txt = self.txtCipherText.get()
        txt = base64.b64decode(txt)
        
        dsize = SHA.digest_size
        sentinel = Random.new().read(15+dsize)

        priKey = getKey("Private Key")
        cipher = PKCS1_v1_5.new(priKey)
        
        detxt = cipher.decrypt(txt, sentinel)

        self.txtDecipherText.delete(0, END)
        self.txtDecipherText.insert(INSERT, detxt)

def main():
    window = tk.Tk()
    window.title("Chương trình chính")
    window.geometry("300x200")
    MainWindow(window)
    window.mainloop()

if __name__=="__main__":
    main()
