from module4.arithmetic import binToHex, hexToBin


def inverse(alpha):

    if alpha == '00':
        return '00'

    value = hexToBin(alpha)
