from module2.sum_points import sumPoints
from module3.multiple_point import multPoint
from module2.opposite_point import opposite

def decodeElG(A, B, p, C1, C2, x):
    x_c = multPoint(A, B, p, x, C1[0], C1[1])
    x_c = opposite(x_c[0], x_c[1])
    return sumPoints(A, B, p, C2[0], C2[1], x_c[0], x_c[1])
