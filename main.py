from module1.fermat_test import binFermatTest
from module1.quadratic_residue import binQuadraticResidue
from module1.modular_multiplicative_inverse import binModInvert, modInvert
from module1.modular_exponentiation import binPowMod
from module1.square_root import binSquareRoot
from module1.pseudorandom_number_generator import main
from module1.binary_arithmetic import menu

from module1.prng import generatePrimeNumber
from module2.random_elliptical_curve import elliptical
from module2.elliptical_curve_point import randomPoint
from module2.check_curve_point import checkPoint
from module2.opposite_point import opposite
from module2.sum_points import sumPoints

from module3.codingMessage import encode, decode, testCoding
from module3.ElGamal_keys import ElGamal, testElG
from module3.multiple_point import multPoint, testMult
from module3.ElGamalEncoding import encodeElG, testElEnc
from module3.ElGamalDecoding import decodeElG, testElDec

from module4.sum import sumHex
from module4.xtime import xtime

def convertListToString(x: list) -> str:
    return "".join([str(e) for e in x])

def module1():
    choice: int = int(input("0. Binary arithmetic\n1. Pseudorandom number generator\n2. Modular inverse\n3. Modular exponentiation\n4. Quadratic residue\n5. Square roots\n6. Fermat test\n> "))
    if choice == 0:
        a: str = input("Enter first number (binary): ")
        b: str = input("Enter second number (binary): ")
        operation: str = input("Type add, mult or div for adding, multiplication or division: ")
        print(menu(a, b, operation))
    elif choice == 1:
        main()
    elif choice == 2:
        a: str = input("Enter first number - a (binary): ")
        b: str = input("Enter second number - b (binary): ")
        print(binModInvert(a, b))
    elif choice == 3:
        base: str = input("Base (binary): ")
        power: str = input("Power (binary): ")
        modulus: str = input("Modulus (binary): ")
        print(f'{base}^{power} (mod {modulus}) = {binPowMod(base, power, modulus)}')
    elif choice == 4:
        a: str = input("a (binary): ")
        p: str = input("p (binary; must be 2 or higher): ")
        print(f'{binQuadraticResidue(a, p)}')
    elif choice == 5:
        b: str = input("b (binary): ")
        p: str = input("p (binary): ")
        print(f'{binSquareRoot(b, p)}')
    elif choice == 6:
        print(f'{binFermatTest(int(input("Enter the number to check if its prime number (binary): ")))}')
    else:
        print("Wrong input!")


def module2():
    choice: int = int(input("1. Random elliptical curve\n2. Find random point\n3. Check if point belongs to the curve\n4. Opposite point\n5. Add two points\n> "))
    # przykładowe dane
    k = 300
    A = 494959415971850257699585114547619761767844026066388911234738789463512822241993964720487368
    B = 239614427021073265587611886177902927263167863041565491257781227550405368115731464059190159
    p = 1183779584357076950937981497685946292711107412152534481102525547387604378262522402526266939
    x1 = 598700530906084162596261101440667782569915319623798143751082061599951188013331503150304328
    y1 = 285113634279465403319996581740169338329454608669814309137990174814243655992779447106132850
    x2 = 754012226560385584185626944584346024956384811926095347825887912144866442212994436980092021
    y2 = 402200101831194929544543876137349336349711339762053350086857107410309555983396073023465445
    try:
        if choice == 1:
            print(elliptical(k))
        elif choice == 2:
            print(randomPoint(A, B, p))
        elif choice == 3:
            print(checkPoint(A, B, p, x1, y1))
        elif choice == 4:
            print(opposite(x1, y1))
        elif choice == 5:
            print(sumPoints(A, B, p, x1, y1, x2, y2))
    except Exception as e:
        print(e)


def module3():
    testMult()
    print()
    testElG()
    print()
    testCoding()
    print()
    testElEnc()
    print()
    testElDec()

# module3()
# print(sumHex('3F', 'F2'))
print(f'73 -> {xtime("73")}')
print()
print(f'92 -> {xtime("92")}')
print()
print(f'32 -> {xtime("32")}')
print()
print(f'DC -> {xtime("DC")}')
print()
print(f'C6 -> {xtime("C6")}')
print()
print(f'CC -> {xtime("CC")}')
print()
print(f'2F -> {xtime("2F")}')
# print(multPoint(594, 434, 887, 507, 524, 772))
