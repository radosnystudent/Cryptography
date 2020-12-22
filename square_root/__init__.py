"""
Zaimplementuj algorytm, który oblicza pierwiastek kwadratowy w ciele Fp, gdzie
p ≡ 3 (mod 4) jest liczbą pierwszą. Wykorzystaj twierdzenie Eulera.
Dane: b ∈ Fp, b jest resztą kwadratową Fp
Wynik: a ∈ Fp taki, że a^2 = b.
"""

from modular_exponentiation import binPowMod
from binary_arithmetic import intToBin

def binSquareRoot(b: str, p: str):
    return binPowMod(b, intToBin((int(p, 2) - 1) // 2), p) == 1
