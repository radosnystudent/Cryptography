from module1.modular_exponentiation import powMod
from random import randint

def generateNumber(k, n):
    k = int(k)
    n = int(n)

    if not n:
        n = pow(2, k)

    _min = 0
    _max = 0
    if k < 1 and n < 1:
        pass
    if k == 1:
        _max = 1
    else:
        minBinary = '1' + '0' * (len("{0:b}".format(k)) - 1)
        _min = int(minBinary, 2)
        _max = n - 1

    if _max > _min:
        return randint(_min, _max)

def checkPrimary(n):
    if n == 1:
        return False
    elif n == 2 or n == 3:
        return True

    number = int(n)
    counter = 30

    while counter:
        b = int(generateNumber(2, n - 2))
        if powMod(b, n - 1, n) != 1:
            return False
        counter -= 1
    return True

def generatePrimeNumber(k):
    while True:
        n = generateNumber(k, 0)
        if checkPrimary(n) and n % 4 == 3:
            return n
