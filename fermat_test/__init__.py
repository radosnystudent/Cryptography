"""
Zaimplementuj test, który sprawdza liczbe naturalna n jest liczbą pierwsza.
Wykorzystaj test Fermata.
Dane: n ∈ N
Wynik: True jeśli n jest liczbą pierwszą, False w przeciwnym wypadku.
"""

import random as rnd
from modular_exponentiation import powMod, binPowMod
from pseudorandom_number_generator import PRNG
from binary_arithmetic import intToBin

def binFermatTest(n: str):
    n = int(n, 2)
    base = PRNG("{0:b}".format(n - 3), n - 2)
    if binPowMod(base, intToBin(n - 1), intToBin(n)) == 1:
        return False
    return True

#################################################################################

def fermatTest(n: int):
    base = int(PRNG("{0:b}".format(n - 3), n - 2), 2)
    if powMod(base, n - 1, n) == 1:
        return False
    return True
