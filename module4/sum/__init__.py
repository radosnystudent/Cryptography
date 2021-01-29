from module4.arithmetic import binToHex, hexToBin

def sumHex(a, b):
    first, second, result = hexToBin(a), hexToBin(b), ''
    for i in range(len(first)):
        result += str((int(first[i]) + int(second[i])) % 2)
    return binToHex(result)
