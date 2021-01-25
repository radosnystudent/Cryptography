from module1.prng import generateNumber, generatePrimeNumber
from module1.modular_exponentiation import powMod
from module1.fermat_test import fermatTest

def fx(A, B, p, x):
    return (powMod(x, 3, p) + (A * x) % p + B) % p

def elliptical(k):
    if not(fermatTest(k, 100) and k % 4 == 3):
        p = generatePrimeNumber(k)
    else:
        p = k

    if fermatTest(p, 100) and p % 4 == 3:
        A, B = 0, 0
        discriminant = 0

        while not discriminant:
            A = generateNumber(0, p - 1)
            B = generateNumber(0, p - 1)
            discriminant = (4 * powMod(A, 3, p) + 27 * powMod(B, 2, p)) % p

        return A, B
    else:
        raise Exception('Złe dane!')
