"""
Niech p będzie liczbą pierwszą. Zaimplementuj test (funkcję), który sprawdza czy element
zbioru Z∗p jest resztą kwadratową w Z∗p. Wykorzystaj twierdzenie Eulera.
Dane: a ∈ Z∗p
Wynik: True jeśli a jest resztą kwadratową, False w przeciwnym wypadku.
"""

from modular_exponentiation import binPowMod
from binary_arithmetic import intToBin

def binQuadraticResidue(b: str, p: str) -> str:
    return b in [binPowMod(intToBin(a), '10', p) for a in range(int(p, 2))]
