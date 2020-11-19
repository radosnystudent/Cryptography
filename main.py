from fermat_test import binFermatTest
from quadratic_residue import binQuadraticResidue
from modular_multiplicative_inverse import binModInvert
from modular_exponentiation import binPowMod
from square_root import binSquareRoot
from pseudorandom_number_generator import main
from binary_arithmetic import menu

def convertListToString(x: list) -> str:
    return "".join([str(e) for e in x])

def start():
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
