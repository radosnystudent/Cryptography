"""
Niech p będzie liczbą pierwszą. Zaimplementuj test (funkcję), który sprawdza czy element
zbioru Z∗p jest resztą kwadratową w Z∗p. Wykorzystaj twierdzenie Eulera.
Dane: a ∈ Z∗p
Wynik: True jeśli a jest resztą kwadratową, False w przeciwnym wypadku.
"""

from module1.modular_exponentiation import binPowMod, powMod
from module1.binary_arithmetic import intToBin

def binQuadraticResidue(b: str, p: str) -> str:
    return b in [binPowMod(intToBin(a), '10', p) for a in range(int(p, 2))]

def quadratic_residue(b, p):
    return b in [powMod(a, 2, p) for a in range(p)]
