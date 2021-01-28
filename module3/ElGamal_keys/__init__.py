from module1.prng import generatePrimeNumber, generateNumber
from module2.random_elliptical_curve import elliptical
from module2.elliptical_curve_point import randomPoint
from module3.multiple_point import multPoint
import random

def LargeNumberRoot(number):
    ''' Long integer square roots. Newton's method.

        Written by PM 2Ring. Adapted from C to Python 2008.10.19
    '''
    n, a, k = number, 1, 0
    while n > a:
        n >>= 1
        a <<= 1
        k += 1

    a = n + (a >> 2)

    while k:
        a = (a + number // a) >> 1
        k >>= 1
    return a

def ElGamal(k):
    p = generatePrimeNumber(k)
    A, B = elliptical(p)

    Q = randomPoint(A, B, p)
    maxRange = (p + 1 - (2 * LargeNumberRoot(p))) % p

    while True:
        # x = generateNumber(1, maxRange)
        x = random.randint(1, maxRange)
        if x < maxRange:
            P = multPoint(A, B, p, x, Q[0], Q[1])
            return A, B, p, Q, P, x


def testElG():
    k = 300
    A, B, p, P, Q, x = ElGamal(k)
    print(f'Klucz publiczny to: {[A, B, p, Q, P]}')
    print(f'Klucz prywatny to: {[A, B, p, Q, P, x]}')
