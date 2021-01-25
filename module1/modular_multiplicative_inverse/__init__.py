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

def extendedGCD(a, n):
    #
    # zmiana algorytmu na wersje iteracyjna,
    # bo przy duzych liczba dla rekurencji python rzucał błędami
    #

    A = n
    B = a
    U = 0
    V = 1

    while B != 0:
        q = A // B
        x1 = B
        x2 = A - q * B
        A = x1
        B = x2
        x1 = V
        x2 = U - q * V
        U = x1
        V = x2

    d = A
    u = U
    v = (d - a * u) // n
    return u, v, d

def modInvert(a, b):
    g, x, y = extendedGCD(a, b)
    if g < 0:
        g += b
    return g
