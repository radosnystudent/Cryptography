def fermatTest(x: int):
    return (2**(x - 1) % x) == 1

if __name__ == "__main__":
    print(f'{fermatTest(int(input("Enter the number to check if its prime number: ")))}')
