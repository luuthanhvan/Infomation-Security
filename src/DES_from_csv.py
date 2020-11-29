from Crypto.Cipher import DES
import base64
import pandas as pd

def readFile():
    data = pd.read_csv("../data/country.csv", delimiter=",")
    return data.value

def pad(s):
    return s + (8 - len(s) % 8) * chr(8 - len(s) % 8)

def unpad(s):
    return s[:-ord(s[len(s)-1:])]

def decryptDES(cipherText, arrKeys):
    txt = base64.b64decode(cipherText)
    detxt = ""
    
    for i in range(len(arrKeys)):
        try:
            key = pad(arrKeys[i]).encode("utf-8")
            cipher = DES.new(key, DES.MODE_ECB)
            
            detxt = unpad(cipher.decrypt(txt)).decode("utf-8")
            
            if  detxt != "":
                return detxt, arrKeys[i]

        except ValueError:
            pass

    return detxt, ""

country = readFile()
cipherText1 = "lIZg7tB/NvuG4MXsCDFUsRjvQrjw/UuUGzZw+QMMDF4nGjQCGzY0Uw=="
cipherText2 = "LsmDvf9t1pLPn+NZ99+cVx+V1ROl2/9KNqk9PLTe5uRii/aNc/X3tw=="
cipherText3 = "5cdbWs00vXghkBLECplG8ClNQ2Da5R/9KZ0bAKRs+bPvhwOwIt7Sh2ZZFtxHBAK9"

plainText1, key1 = decryptDES(cipherText1, country)
plainText2, key2 = decryptDES(cipherText2, country)
plainText3, key3 = decryptDES(cipherText3, country)

print("Văn bản được mã hóa số 1: ", cipherText1)
print("Văn bản gốc 1: ", plainText1)

print("=================================================================================\n")

print("Văn bản được mã hóa số 2: ", cipherText2)
print("Văn bản gốc 2: ", plainText2)

print("=================================================================================\n")

print("Văn bản được mã hóa số 3: ", cipherText3)
print("Văn bản gốc 3: ", plainText3)

print("=================================================================================\n")