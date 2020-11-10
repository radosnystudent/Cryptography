"""
Zaimplementuj algorytm, który generuje losowy element zbioru Zn.
Dane: k,n ∈ N
Wynik: k-bitowa liczba b ∈ Zn
"""

import datetime as dt

# dowolne stałe
GENERATOR: int = 2057
MODULUS: int = 3167

inputValue = "{0:b}".format(int(input("Twoja liczba:\n> ")))
N = int(input("Ile liczb chcesz wygenerować?\n> "))
n = int(input("Podaj n:\n> "))
SEED_SIZE: int = len(inputValue)


def L_function(x: int) -> int:
    # any polynomial function
    return 3 * x ** 2 - 5 * x + 9


def F_function(x: str):
    # f(x) <- g^x mod p
    return "{0:b}".format(pow(GENERATOR, int(x, 2), MODULUS))


def HFunction(first_half: str, second_half: str) -> str:

    # one-way permutation function
    # function H (x, y)
    #   f(x) <- g^x mod p  where g is a generator
    #   b <- 0
    #   for i <- 0 to |x| do
    #       b <- b XOR (x[i] AND y[i])
    #   return f + y + b

    fx: str = F_function(first_half)
    hard_core_bit: int = 0
    for i in range(len(first_half)):
        hard_core_bit = (hard_core_bit ^ (int(first_half[i]) & int(second_half[i]))) % 2
    return fx + second_half + str(hard_core_bit)


def PRNG(initial_seed: str, n: int) -> str:

    # pseudorandom number generator
    # function G(x0)
    #   t <- aftual time in miliseconds convert to binary number
    #   output <- '1' (because we want 1 on first bit and thats because we don't want k-bit numbers to be like: k=5, k-bit number = 00000 )
    #   for i <- 0 to |x0|- 1 do
    #       t <- H(first_half(t), second_half(t))
    #       output <- output * last_bit(t)
    #       t <- remove_last_bit(t)
    #   return output

    # because we need k-bit numbers form range [0, n-1], we need to check if generated number is in given range
    # if not, generate another
    while True:
        result: str = '1'
        binary_string: str = "{0:b}".format(int(dt.datetime.now().timestamp() * 10000))
        for _ in range(SEED_SIZE - 1):

            first_half: str = binary_string[:int(len(binary_string) / 2)]
            second_half: str = binary_string[int(len(binary_string) / 2):]

            binary_string = HFunction(first_half, second_half)
            result += binary_string[-1]

            binary_string = binary_string[:-1]
        if int(result, 2) < n:
            break
    return result

# range [min, max] <- all k-bit numbers
minValue: int = int('1' + '0' * (SEED_SIZE - 1), 2)
maxValue: int = int("{0:b}".format(n), 2)

if __name__ == '__main__':
    if n > minValue:
        print(f'początkowa liczba: {int(inputValue, 2)}; liczba bitów: {SEED_SIZE}')
        print(f'Przedział liczb: [{minValue}, {maxValue})')
        results: list = list()
        for _ in range(N):
            results.append(int(PRNG(inputValue, n), 2))
            MODULUS = abs(MODULUS - L_function(SEED_SIZE))
        print(f'results: {results}')
    else:
        print(f'nie ma {SEED_SIZE}-bitowych liczb, które byłyby w przedziale [0, {n - 1}]')
