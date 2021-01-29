from module4.arithmetic import hexToBin, binToHex

def xtime(alpha):
    xy, c, result = hexToBin(alpha), hexToBin("02"), ''

    if xy[0] == 0:
        return xy[1:].zfill(8)
    for i in range(0, len(xy)):
        if i == len(xy) - 1:
            result += str(int(xy[0]) * int(c[i]))
        else:
            result += str((int(xy[0]) * int(c[i]) + int(xy[i + 1])) % 2)
    return binToHex(result), result
