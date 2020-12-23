from module1.modular_exponentiation import powMod
from module2.random_elliptical_curve import fx

def checkPoint(A, B, p, x, y):
    return powMod(y, 2, p) == fx(A, B, p, x)  # (powMod(x, 3, p) + (A * x) % p + B) % p
