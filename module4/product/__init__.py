from module4.arithmetic import binToHex, hexToBin
from module4.xtime import xtime
from module4.sum import sumHex
from module1.binary_arithmetic import intToBin


# def product(a, b):
#     first, second, result = hexToBin(a), hexToBin(b), '0'

#     length = len(first) - 1

#     for i in first:
#         if i == '1':
#             counter = length
#             r = second
#             while counter:
#                 r = hexToBin(xTime(r))
#                 counter -= 1
#             result = hexToBin(sumHex(binToHex(result), binToHex(r)))
#         length -= 1

#     # print(f'{result=}')

#     return binToHex(result)

def product(a, b):
    res = '00'
    binA = hexToBin(a)
    iterator = len(binA) - 1

    for x in binA:
        if x == '1':
            temp = b
            c = iterator
            while c:
                temp = xtime(temp)
                c -= 1
            res = sumHex(temp, res)
        iterator -= 1

    return res
