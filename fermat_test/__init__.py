"""
Zaimplementuj test, który sprawdza liczbe naturalna n jest liczbą pierwsza.
Wykorzystaj test Fermata.
Dane: n ∈ N
Wynik: True jeśli n jest liczbą pierwszą, False w przeciwnym wypadku.
"""

import random as rnd
from modular_exponentiation import powMod
from pseudorandom_number_generator import PRNG

def fermatTest(n: int):
    # base = rnd.randint(2, n - 2)
    base = int(PRNG("{0:b}".format(n - 3), n - 2), 2)
    if powMod(base, n - 1, n) == 1:
        return False
    return True

# if __name__ == "__main__":
#     print(f'{fermatTest(int(input("Enter the number to check if its prime number: ")))}')
