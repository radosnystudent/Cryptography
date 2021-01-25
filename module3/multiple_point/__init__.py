from module2.sum_points import sumPoints

def multPoint(A, B, p, x, y, n):
    pointP = (x, y)
    resultPoint = (0, 0)

    while n:
        if n % 2 == 1:
            resultPoint = sumPoints(A, B, p, resultPoint[0], resultPoint[1], pointP[0], pointP[1])
            n -= 1
        pointP = sumPoints(A, B, p, pointP[0], pointP[1], pointP[0], pointP[1])
        n //= 2

    return resultPoint


def testMult():
    a = 33
    b = 54
    p = 71

    n = 35

    x = 15
    y = 44

    print(multPoint(a, b, p, x, y, n))
