"""
Zaimplementuj test, który sprawdza liczbe naturalna n jest liczbą pierwsza.
Wykorzystaj test Fermata.
Dane: n ∈ N
Wynik: True jeśli n jest liczbą pierwszą, False w przeciwnym wypadku.
"""

def fermatTest(x: int):
    return (2**(x - 1) % x) == 1

if __name__ == "__main__":
    print(f'{fermatTest(int(input("Enter the number to check if its prime number: ")))}')
