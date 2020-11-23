"""
Zaimplementuj algorytm do obliczania odwrotności w grupie Φ(n).
Wykorzystaj Rozszerzony Algorytm Euklidesa.
Dane: n ∈ N, b ∈ Φ(n)
Wynik: b^−1 ∈ Φ(n)
"""

from binary_arithmetic import divBin, multBin, intToBin

def binExtendedGCD(a: str, b: str) -> tuple:
    if int(a, 2) != 0:
        g, y, x = binExtendedGCD(divBin(b, a)[1], a)
        return (g, intToBin(int(x, 2) - int(multBin(divBin(b, a)[0], y), 2)), y)
    else:
        return (b, '0', '1')

def modInverse(a: str, b: str) -> str:
    g, x, y = binExtendedGCD(a, b)

    if int(g, 2) == 1:
        return divBin(x, b)[1]
    else:
        return ''
