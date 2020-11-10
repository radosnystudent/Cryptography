"""
Niech p będzie liczbą pierwszą. Zaimplementuj test (funkcję), który sprawdza czy element
zbioru Z∗p jest resztą kwadratową w Z∗p. Wykorzystaj twierdzenie Eulera.
Dane: a ∈ Z∗p
Wynik: True jeśli a jest resztą kwadratową, False w przeciwnym wypadku.
"""

from modular_exponentiation import powMod

def quadraticResidue(a, p):
    if p < 2:
        return "p must be 2 or higher"
    else:
        return powMod(a, (p - 1) / 2, p) == 1

# if __name__ == "__main__":
#     a: int = int(input("a:\n> "))
#     p: int = int(input("p (must be 2 or higher):\n> "))
#     print(f'{quadraticResidue(a, p)}')
