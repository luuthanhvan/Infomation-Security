# decrypt
def charToNum(c):
    return (ord(c)-65)

def numToChar(n):
    return chr(n+65)

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

def isPrime(num):
    for i in range(2, num):
        if (num % i == 0):
            return False
    return True

def bruteForce(txt):
    m = 26
    for i in range(1, 13):
        for j in range(1, 27):
            if isPrime(i) == True and isPrime(j) == True:
                a = i
                b = j
                print(decryptAffine(cipherText, a, b, m), a, b)

cipherText = "HKLZOVYQPTOBJDVOBLBUBOHKWBGVUVYVZUTZGHOVYQPBYVREOZRBTTBT"
#bruteForce(cipherText) # a: 5, b: 7
print(decryptAffine(cipherText, 5, 7, 26))
# Plain text: algorithms require general definitions of arithmetic processes
