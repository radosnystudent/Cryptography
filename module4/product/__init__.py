from module4.arithmetic import binToHex, hexToBin
from module4.xtime import xtime
from module4.sum import sumHex

def product(a, b):
    first, second, result = hexToBin(a), hexToBin(b), '00'

    length = len(first) - 1

    for i in first:
        if i == '1':
            counter = length
            r = second
            while counter:
                r = hexToBin(xtime(r))
                counter -= 1
            result = hexToBin(sumHex(binToHex(result), binToHex(r)))
        length -= 1

    return binToHex(result)
