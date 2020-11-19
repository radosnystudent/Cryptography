"""
Niech p będzie liczbą pierwszą. Zaimplementuj test (funkcję), który sprawdza czy element
zbioru Z∗p jest resztą kwadratową w Z∗p. Wykorzystaj twierdzenie Eulera.
Dane: a ∈ Z∗p
Wynik: True jeśli a jest resztą kwadratową, False w przeciwnym wypadku.
"""

from modular_exponentiation import powMod, binPowMod
from binary_arithmetic import divBin, intToBin

def binQuadraticResidue(a: str, p: str):
    if int(p, 2) < 2:
        return "p must be 2 or higher"
    else:
        return int(binPowMod(a, divBin(intToBin(int(p, 2) - 1), intToBin(2))[0], p), 2) == 1

#################################################################################

def quadraticResidue(a, p):
    if p < 2:
        return "p must be 2 or higher"
    else:
        return powMod(a, (p - 1) / 2, p) == 1
