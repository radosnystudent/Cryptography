def powMod(base: int, power: int, modulus: int) -> int:
    result: int = 1
    while power:
        power, degree = power // 2, power % 2
        if degree:
            result = result * base % modulus
        base = base * base % modulus
    return result

if __name__ == "__main__":
    base = int(input("Base:\n> "))
    power = int(input("Power:\n> "))
    modulus = int(input("Modulus:\n> "))
    print(f'{base}^{power} mod {modulus} = {powMod(base, power, modulus)}')
