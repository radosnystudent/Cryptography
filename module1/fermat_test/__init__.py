"""
Zaimplementuj test, który sprawdza liczbe naturalna n jest liczbą pierwsza.
Wykorzystaj test Fermata.
Dane: n ∈ N
Wynik: True jeśli n jest liczbą pierwszą, False w przeciwnym wypadku.
"""

from module1.modular_exponentiation import binPowMod, powMod
from module1.binary_arithmetic import intToBin, divBin
from random import randint

def binNwd(a, b):
    while int(b, 2) != 0:
        a, b = b, divBin(a, b)[1]
    return a

def binFermatTest(n: str, k: str):
    n_int: int = int(n, 2)  # zamieniam sobie te liczby na inty, zeby móc łatwo odejmowac potem
    k_int: int = int(k, 2)  # lub wykorzystywac w petli

    for i in range(k_int):
        b = intToBin(randint(2, n_int - 2))
        if int(binPowMod(b, intToBin(n_int - 1), n), 2) != 1:
            return 'nie'
    return 'tak'

def nwd(a, b):
    while not b:
        a, b = b, a % b
    return a

def fermatTest(n, k):
    for i in range(k):
        b = randint(2, n - 2)
        if powMod(b, n - 1, n) != 1:
            return False
    return True
