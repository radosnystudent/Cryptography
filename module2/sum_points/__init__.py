from module1.modular_multiplicative_inverse import modInvert
from module1.modular_exponentiation import powMod

def sumPoints(A, B, p, x1, y1, x2, y2):

    if x1 == 0 and y1 == 0:
        return (x2, y2)
    elif x2 == 0 and y2 == 0:
        return (x1, y1)

    if x1 != x2 and y1 != y2:
        lambd = ((y2 - y1) % p * modInvert((x2 - x1) % p, p)) % p
        x3 = (powMod(lambd, 2, p) - (x1 % p) - (x2 % p)) % p
        y3 = (lambd * (x1 - x3) - y1) % p
        return (x3, y3)
    elif x1 == x2 and y1 == y2:
        lambd = ((((3 * powMod(x1, 2, p) % p) + A) % p) * modInvert(2 * y1, p)) % p
        x3 = (powMod(lambd, 2, p) - (x1 % p) - (x2 % p)) % p
        y3 = (lambd * (x1 - x3) - y1) % p
        return (x3, y3)

    if x1 == x2 and y1 == -y2:
        return (0, 0)
