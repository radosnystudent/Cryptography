"""
Zaimplementuj algorytm, który generuje losowy element zbioru Zn.
Dane: k,n ∈ N
Wynik: k-bitowa liczba b ∈ Zn
"""
from matplotlib import pyplot as plt
import datetime as dt
from collections import Counter
from modular_exponentiation import powMod

GENERATOR: int = 23
MODULUS: int = 36389

def HFunction(first_half: str, second_half: str) -> str:

    # one-way permutation function
    # function H (x, y)
    #   f(x) <- g^x mod p  where g is a generator and p is prime number
    #   b <- 0
    #   for i <- 0 to |x| do
    #       b <- b XOR (x[i] AND y[i])
    #   return f + y + b

    fx: str = "{0:b}".format(powMod(GENERATOR, int(first_half, 2), MODULUS))
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
    iteration = 0
    while True:
        result: str = '1'
        binary_string: str = "{0:b}".format(int(dt.datetime.now().timestamp() * 100000000) + iteration)
        # print(f'{int(dt.datetime.now().timestamp() * 10000)} : {binary_string}')
        for _ in range(len(initial_seed) - 1):

            first_half: str = binary_string[:int(len(binary_string) / 2)]
            second_half: str = binary_string[int(len(binary_string) / 2):]

            binary_string = HFunction(first_half, second_half)
            # print(binary_string)
            result += binary_string[-1]

            binary_string = binary_string[:-1]
        if int(result, 2) < n:
            break
    return result

def main():
    global MODULUS
    inputValue = "{0:b}".format(int(input("Twoja liczba:\n> ")))

    N = int(input("Ile liczb chcesz wygenerować?\n> "))
    n = int(input("Podaj n:\n> "))

    SEED_SIZE: int = len(inputValue)

    # range [min, max] <- all k-bit numbers
    minValue: int = int('1' + '0' * (SEED_SIZE - 1), 2)
    maxValue: int = int("{0:b}".format(n), 2) - 1 if int("{0:b}".format(n), 2) <= int('1' * (SEED_SIZE), 2) else int('1' * (SEED_SIZE), 2)

    # temp1 = int("{0:b}".format(n), 2)
    # temp2 = int('1' * (SEED_SIZE), 2)

    # print(f'{temp1} vs {temp2} : {temp1 <= temp2}')

    if n > minValue:
        print(f'początkowa liczba: {int(inputValue, 2)}; liczba bitów: {SEED_SIZE}')
        print(f'Przedział liczb: [{minValue}, {maxValue}]')
        results: list = list()

        for _ in range(N):
            inputValue = PRNG(inputValue, n)
            results.append(int(inputValue, 2))
        print(f'results: {results}')
        # results.sort()
        plt.bar(*zip(*Counter(results).items()))
        plt.show()
    else:
        print(f'nie ma {SEED_SIZE}-bitowych liczb, które byłyby w przedziale [0, {n - 1}]')
