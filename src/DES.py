from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import base64

def pad(s):
    return s + (8 - len(s) % 8) * chr(8 - len(s) % 8)

def unpad(s):
    return s[:-ord(s[len(s)-1:])]

def encryptDES():
    txt = pad(plainTxt.get()).encode("utf8")
    key = pad(keyTxt.get()).encode("utf8")
    cipher = DES.new(key, DES.MODE_ECB)
    entxt = cipher.encrypt(txt)
    entxt = base64.b64encode(entxt)
    cipherTxt.delete(0, END)
    cipherTxt.insert(INSERT, entxt)

def decryptDES():
    txt = cipherTxt.get()
    txt = base64.b64decode(txt)
    key = pad(keyTxt.get()).encode("utf8")
    cipher = DES.new(key, DES.MODE_ECB)
    detxt = unpad(cipher.decrypt(txt))
    decipherTxt.delete(0, END)
    decipherTxt.insert(INSERT, detxt)

# name = pad("Luu Thanh Van")
# print(len(name))
# newName = unpad(name)
# print(len(newName))

# khoi tao man hinh chinh
window = Tk()
window.title("Welcome to Demo An Toàn Bảo Mật Thông Tin")

lbHeader = Label(window, text=" ", font=("Arial Bold", 10))
lbHeader.grid(column=0, row=0)

lbTitle = Label(window, text="CHƯƠNG TRÌNH DEMO", font=("Arial Bold", 20))
lbTitle.grid(column=1, row=1)

lbText = Label(window, text="MẬT MÃ ĐỐI XỨNG DES", font=("Arial Bold", 16))
lbText.grid(column=1, row=2)

lbPlainText = Label(window, text="Văn bản gốc", font=("Arial Bold", 14))
lbPlainText.grid(column=0, row=3)
plainTxt = Entry(window, width=40)
plainTxt.grid(column=1, row=3)

lbKeyText = Label(window, text="Khóa", font=("Arial Bold", 14))
lbKeyText.grid(column=0, row=4)
keyTxt = Entry(window, width=40)
keyTxt.grid(column=1, row=4)

lbCipherText = Label(window, text="Văn bản được mã hóa", font=("Arial Bold", 14))
lbCipherText.grid(column=0, row=5)
cipherTxt = Entry(window, width=40)
cipherTxt.grid(column=1, row=5)

lbDecipherText = Label(window, text="Văn bản được giải mã", font=("Arial Bold", 14))
lbDecipherText.grid(column=0, row=6)
decipherTxt = Entry(window, width=40)
decipherTxt.grid(column=1, row=6)

encryptBtn = Button(window, text="Mật mã", command=encryptDES)
encryptBtn.grid(column=0, row=7)

decryptBtn = Button(window, text="Giải mã", command=decryptDES)
decryptBtn.grid(column=1, row=7)

# hien thi cua so
window.geometry("800x300")
window.mainloop()