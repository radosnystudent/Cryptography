"""
Zaimplementuj algorytm, który oblicza pierwiastek kwadratowy w ciele Fp, gdzie
p ≡ 3 (mod 4) jest liczbą pierwszą. Wykorzystaj twierdzenie Eulera.
Dane: b ∈ Fp, b jest resztą kwadratową Fp
Wynik: a ∈ Fp taki, że a^2 = b.
"""

from modular_exponentiation import powMod, binPowMod
from quadratic_residue import quadraticResidue, binQuadraticResidue
from binary_arithmetic import addBin, divBin, intToBin

def binSquareRoot(b: str, p: str):
    if int(divBin(p, intToBin(4))[1], 2) == 3 and binQuadraticResidue(b, p):
        return b in [binPowMod(a, divBin(addBin(p, '1'), intToBin(4)), p) for a in range(p)]
    else:
        return f'{int(b, 2)} is not quadratic residue in {int(p, 2)} or {int(p, 2)} mod 4 !== 3'

#################################################################################

def squareRoot(b, p):
    if p % 4 == 3 and quadraticResidue(b, p):
        return b in [powMod(a, (p + 1) // 4, p) for a in range(p)]
    else:
        return f'{b} is not quadratic residue in {p} or {p} mod 4 !== 3'
