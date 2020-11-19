def intToBin(x: int) -> str:
    return "{0:b}".format(x)


def removeLeadingZeros(x: str) -> str:
    if '1' in x:
        return x.lstrip('0')
    else:
        return '0'


def addBin(first: str, second: str) -> str:
    first = removeLeadingZeros(first)
    second = removeLeadingZeros(second)
    binLength = max(len(first), len(second))

    first = first.zfill(binLength)
    second = second.zfill(binLength)

    output = ''
    carryover = 0

    for i in range(binLength - 1, -1, -1):
        temp = carryover
        temp += 1 if first[i] == '1' else 0
        temp += 1 if second[i] == '1' else 0

        output = ('1' if temp % 2 == 1 else '0') + output  # temp = {0,1,2,3}, if temp = 1 or 3, result bit = 1 else carryover = 1
        carryover = 0 if temp < 2 else 1  # if carryover = 3, we have to carry 1

    if carryover != 0:
        output = '1' + output

    return output


def multBin(first: str, second: str) -> str:
    if int(first, 2) == 0 or int(second, 2) == 0:
        return '0'
    first = removeLeadingZeros(first)
    second = removeLeadingZeros(second)

    maxLen: int = len(first) + len(second) - 1
    arr: list = list()
    zerosNum = 0

    for i in range(len(second) - 1, -1, -1):
        bitLine: str = ''
        for j in range(len(first) - 1, -1, -1):
            bitLine = ('1' if first[j] == '1' and second[i] == '1' else '0') + bitLine
        if '1' in bitLine:
            arr.append((bitLine + '0' * zerosNum).zfill(maxLen))
        zerosNum += 1
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return addBin(arr[0], arr[1])
    else:
        prev = addBin(arr[0], arr[1])
        for i in range(2, len(arr)):
            prev = addBin(prev, arr[i])
        return prev


def divBin(first: str, second: str) -> str:
    first = removeLeadingZeros(first)
    second = removeLeadingZeros(second)
    dividend = [first[i] for i in range(len(first) - 1, -1, -1)]

    output: str = ''
    actual: str = '0'
    pos: int = 0
    k: int = 0

    if int(second, 2) > int(first, 2):
        return '0', first

    while int(second, 2) > int(actual, 2):
        if k == 0:
            actual = ''
            k += 1
        actual += dividend.pop()

    if len(first) == len(actual):
        output += '1'
        actual = "{0:b}".format(int(first, 2) - int(second, 2))
        return output, actual
    while len(actual) < len(first):
        if not dividend:
            break
        if int(second, 2) <= int(actual, 2):
            output += '1'
            actual = "{0:b}".format(int(actual, 2) - int(second, 2))
            if dividend:
                actual += dividend.pop()
        else:
            output += '0'
            if dividend:
                actual += dividend.pop()

    return output.zfill(len(first)), actual


def menu(a: str, b: str, operation: str) -> str:
    if operation == 'add':
        return addBin(a, b)
    elif operation == 'mult':
        return multBin(a, b)
    elif operation == 'div':
        if b == '' or int(b, 2) == 0:
            return 'divisor cannot be 0'
        if int(a, 2) == 0:
            return '0'
        return divBin(a, b)
    else:
        return 'Wrong input!'
