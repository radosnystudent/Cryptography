from module4.arithmetic import binToHex, hexToBin
from module4.product import product
from module4.xtime import xtime
from module1.binary_arithmetic import intToBin

def extendedEuclideanGF2(a, b):
    a, b = int(a, 2), int(b, 2)
    x, prevx = 0, 1
    y, prevy = 1, 0
    while b:
        q = a // b
        a, b = b, a % b
        x, prevx = prevx - q * x, x
        y, prevy = prevy - q * y, y

    return intToBin(a), intToBin(prevx), intToBin(prevy)

def inverse(x):
    for i in range(255):
        if product(x, binToHex(intToBin(i).zfill(8))) == '01':
            return binToHex(intToBin(i).zfill(8))
