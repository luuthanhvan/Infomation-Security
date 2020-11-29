from Crypto.Cipher import DES
import base64

def readFile():
    message = open("../data/message.txt", "r")
    return message.read()

def pad(s):
    return s + (8 - len(s) % 8) * chr(8 - len(s) % 8)

def unpad(s):
    return s[:-ord(s[len(s)-1:])]

def encryptDES(plainText, key):
    cipher = DES.new(key, DES.MODE_ECB)
    entxt = cipher.encrypt(plainText)
    entxt = base64.b64encode(entxt)
    return entxt.decode("utf8")

def decryptDES(cipherText, key):
    txt = base64.b64decode(cipherText)
    cipher = DES.new(key, DES.MODE_ECB)
    detxt = unpad(cipher.decrypt(txt))

    return detxt.decode("utf8")


orgMessage = readFile()
print("Văn bản gốc:\n", orgMessage)
print("=======================================================\n")

key = pad("abcxyz").encode("utf8")
# print(key)
message = pad(orgMessage).encode("utf8")

cipherText = encryptDES(message, key)
print("Văn bản được mã hóa\n", cipherText)
print("=======================================================\n")

plainText = decryptDES(cipherText, key)
print("Văn bản sau khi được giải mã:\n", plainText)
print("=======================================================\n")
