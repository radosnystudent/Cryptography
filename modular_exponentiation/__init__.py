"""
Zaimplementuj algorytm efektywnego potęgowania w zbiorze Zn.
Wykorzystaj algorytm iterowanego podnoszenia do kwadratu.
Dane: n, k ∈ N, b ∈ Zn
Wynik: b^k
"""
from binary_arithmetic import divBin, intToBin, multBin, addBin


def binPowMod(base: str, power: str, modulus: str) -> str:
    result = '1'
    while int(power, 2) != 0:
        power, degree = divBin(power, intToBin(2))
        if int(degree, 2) != 0:
            result = divBin(multBin(result, base), modulus)[1]
        base = divBin(multBin(base, base), modulus)[1]

    return result

#################################################################################

def powMod(base: int, power: int, modulus: int) -> int:
    result: int = 1
    while power:
        power, degree = power // 2, power % 2
        if degree:
            result = result * base % modulus
        base = base * base % modulus
    return result
