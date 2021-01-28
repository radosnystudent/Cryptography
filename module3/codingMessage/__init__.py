from module1.prng import generateNumber
from module1.modular_exponentiation import powMod
from module1.fermat_test import fermatTest
from module2.random_elliptical_curve import fx


def ifSquareRoot(x, p):
    return powMod(x, (p - 1) // 2, p) and fermatTest(p, 30)

def encode(A, B, p, M, u=None):
    n = generateNumber(0, 1000000) + M
    if u is None:
        u = 30  # generateNumber(30, 50)

    if n * u < p:
        temp = M * u
        for i in range(1, u + 1):
            x = M * u % p + i % p
            ys = fx(A, B, p, x)
            if ifSquareRoot(ys, p):
                return (x, powMod(ys, (p + 1) // 4, p))
    else:
        return (None, None)


def decode(x, k):
    return (x - 1) // k

def testCoding():
    A = 985487021788484437436713103381676411350189319115517630809482936843345302961106356764248597
    B = 4984725568969670490954065053055446177717282626797328613040442205729457781644339973492726123
    p = 7275637152949605397191062869087589305268826416203902676025543852365781993930070670634601359
    M = 2021
    u = 30

    P = encode(A, B, p, M)  # encode(A, B, p, m, u)
    print(P)
    print(decode(P[0], u))
