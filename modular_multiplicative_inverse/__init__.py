"""
Zaimplementuj algorytm do obliczania odwrotności w grupie Φ(n).
Wykorzystaj Rozszerzony Algorytm Euklidesa.
Dane: n ∈ N, b ∈ Φ(n)
Wynik: b^−1 ∈ Φ(n)
"""

def extendedGCD(a: int, b: int) -> tuple:
    if a != 0:
        g, y, x = extendedGCD(b % a, a)
        return (g, x - (b // a) * y, y)
    else:
        return (b, 0, 1)

def modInvert(a: int, b: int) -> str:
    g, x, y = extendedGCD(a, b)
    print(f'{g} {x} {y}')
    if g == 1:
        return f'inverse: {x % b}'
    else:
        return 'modular inverse not exist'

# if __name__ == "__main__":
#     a: int = int(input("enter first number - a:\n> "))
#     b: int = int(input("enter second number b:\n> "))
#     print(modInvert(a, b))
