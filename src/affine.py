from tkinter import *

# khoi tao man hinh chinh
window = Tk()
window.title("Welcome to Demo An toan bao mat thong tin")

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

def encrypt():
    a = int(keyPairTxtA.get())
    b = int(keyPairTxtB.get())
    m = 26
    txt = plainTxt.get()
    enTxt = encryptAffine(txt, a, b, m)
    cipherTxt.delete(0, END)
    cipherTxt.insert(INSERT, enTxt)

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

def decrypt():
    a = int(keyPairTxtA.get())
    b = int(keyPairTxtB.get())
    m = 26
    txt = cipherTxt.get()
    deTxt = decryptAffine(txt, a, b, m)
    decryptTxt.delete(0, END)
    decryptTxt.insert(INSERT, deTxt)

# them cac control
lbHeader = Label(window, text=" ", font=("Arial Bold", 10))
lbHeader.grid(column=0, row=0)

lbTitle = Label(window, text="CHUONG TRINH DEMO", font=("Arial Bold", 20))
lbTitle.grid(column=1, row=1)

lbAffine = Label(window, text="MAT MA AFFINE", font=("Arial Bold", 16))
lbAffine.grid(column=0, row=2)

plainTextlb = Label(window, text="PLAIN TEXT", font=("Arial", 14))
plainTextlb.grid(column=0, row=3)
plainTxt = Entry(window, width=20)
plainTxt.grid(column=1, row=3)

cipherTextlb = Label(window, text="CIPHER TEXT", font=("Arial", 14))
cipherTextlb.grid(column=0, row=4)
cipherTxt = Entry(window, width=20)
cipherTxt.grid(column=1, row=4)

keyPairlb = Label(window, text="KEY PAIR", font=("Arial", 14))
keyPairlb.grid(column=2, row=3)

keyPairTxtA = Entry(window, width=5)
keyPairTxtA.grid(column=3, row=3)

keyPairTxtB = Entry(window, width=5)
keyPairTxtB.grid(column=4, row=3)

encryptBtn = Button(window, text="Encrypt", command=encrypt)
encryptBtn.grid(column=5, row=3)

decryptBtn = Button(window, text="Decrypt", command=decrypt)
decryptBtn.grid(column=2, row=4)
decryptTxt = Entry(window, width=20)
decryptTxt.grid(column=3, row=4)

# hien thi cua so
window.geometry('800x300')
window.mainloop()
