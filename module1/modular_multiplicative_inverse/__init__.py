"""
Zaimplementuj algorytm do obliczania odwrotności w grupie Φ(n).
Wykorzystaj Rozszerzony Algorytm Euklidesa.
Dane: n ∈ N, b ∈ Φ(n)
Wynik: b^−1 ∈ Φ(n)
"""

from module1.binary_arithmetic import divBin, multBin, intToBin

def binExtendedGCD(a: str, b: str) -> tuple:
    if int(a, 2) != 0:
        g, y, x = binExtendedGCD(divBin(b, a)[1], a)
        return (g, intToBin(int(x, 2) - int(multBin(divBin(b, a)[0], y), 2)), y)
    else:
        return (b, '0', '1')

def binModInvert(a: str, b: str) -> str:
    g, x, y = binExtendedGCD(a, b)

    if int(g, 2) == 1:
        return divBin(x, b)[1]
    else:
        return ''

def extendedGCD(a, b):
    if a != 0:
        g, y, x = extendedGCD(b % a, a)
        return (g, x - y * b // a, y)
    else:
        return (b, 0, 1)

def modInvert(a, b):
    g, x, y = extendedGCD(a, b)
    if g == 1:
        return x // b
    return None
