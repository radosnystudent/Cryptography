from fermat_test import fermatTest
from quadratic_residue import quadraticResidue
from modular_multiplicative_inverse import modInvert
from modular_exponentiation import powMod
from square_root import squareRoot
from pseudorandom_number_generator import main

if __name__ == "__main__":
    choice: int = int(input("1. Pseudorandom number generator \n2. Modular inverse\n3. Modular exponentiation\n4. Quadratic residue\n5. Square roots\n6. Fermat test\n> "))
    if choice == 1:
        main()
    elif choice == 2:
        a: int = int(input("Enter first number - a: "))
        b: int = int(input("Enter second number b: "))
        print(modInvert(a, b))
    elif choice == 3:
        base = int(input("Base: "))
        power = int(input("Power: "))
        modulus = int(input("Modulus: "))
        print(f'{base}^{power} (mod {modulus}) = {powMod(base, power, modulus)}')
    elif choice == 4:
        a: int = int(input("a: "))
        p: int = int(input("p (must be 2 or higher): "))
        print(f'{quadraticResidue(a, p)}')
    elif choice == 5:
        b: int = int(input("b: "))
        p: int = int(input("p: "))
        print(f'{squareRoot(b, p)}')
    elif choice == 6:
        print(f'{fermatTest(int(input("Enter the number to check if its prime number: ")))}')
    else:
        print("Wrong input!")
