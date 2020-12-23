from module1.square_root import squareRoot
from module1.modular_exponentiation import powMod
from module1.prng import generateNumber
from module2.random_elliptical_curve import fx

def calculate_square_root(b, p):
    return powMod(b, (p + 1) // 4, p)

def randomPoint(A, B, p):
    x, y = 0, 0

    while True:
        x = generateNumber(0, p - 1)
        y = fx(A, B, p, x)
        if squareRoot(y, p):
            y = calculate_square_root(y, p)
            return (x, y)
