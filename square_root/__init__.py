from cryptography.modular_exponentiation import powMod
from cryptography.quadratic_residue import quadraticResidue

def squareRoot(b, p):
    if p % 4 == 3 and quadraticResidue(b, p):
        return b in [powMod(a, (p + 1) // 4, p) for a in range(p)]
    else:
        return f'{b} is not quadratic residue in {p} or {p} mod 4 !== 3'

if __name__ == "__main__":
    b: int = int(input("b:\n> "))
    p: int = int(input("p:\n> "))
    print(f'{squareRoot(b, p)}')
