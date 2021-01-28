from module2.sum_points import sumPoints
from module3.multiple_point import multPoint
from module2.opposite_point import opposite
from module3.ElGamalEncoding import testElEnc


def decodeElG(A, B, p, C1, C2, x):
    x_c = multPoint(A, B, p, x, C1[0], C1[1])
    x_c = opposite(x_c[0], x_c[1])
    return sumPoints(A, B, p, C2[0], C2[1], x_c[0], x_c[1])

def testElDec():
    x = 774554660470749526582432966976130757257247914729300504386029112760794402376
    A, B, p, C = testElEnc(True)
    print(decodeElG(A, B, p, C[0], C[1], x))
