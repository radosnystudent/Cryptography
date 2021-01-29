
hexa = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}

def hexToBin(hex_number):
    return hexa[hex_number[0]] + hexa[hex_number[1]]

def binToHex(bin_number):
    first, second, result = bin_number[0:4], bin_number[4:], ''
    if len(first) != 4:
        first = first.zfill(4)
    if len(second) != 4:
        second = second.zfill(4)

    for key, value in hexa.items():
        if first == value:
            result += key
    for key, value in hexa.items():
        if second == value:
            result += key

    return result
