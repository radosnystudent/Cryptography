from cryptography.modular_exponentiation import powMod

def quadraticResidue(a, p):
    if p < 2:
        return "p must be 2 or higher"
    else:
        return powMod(a, (p - 1) / 2, p) == 1

if __name__ == "__main__":
    a: int = int(input("a:\n> "))
    p: int = int(input("p (must be 2 or higher):\n> "))
    print(f'{quadraticResidue(a, p)}')
