import datetime as dt

# dowolne stałe
GENERATOR: int = 391
MODULUS: int = 735651

inputValue = "{0:b}".format(int(input("Twoja liczba:\n> ")))
N = int(input("Ile liczb chcesz wygenerować?\n> "))
n = int(input("Podaj n:\n> "))
SEED_SIZE: int = len(inputValue)


def function_L(x: int) -> int:
    # any polynomial function
    return 3 * x ** 2 - 5 * x + 9


def function_F(x: str):
    # f(x) <- 2^x mod p
    return bin(pow(GENERATOR, int(x, 2), MODULUS)).replace('0b', '').zfill(SEED_SIZE)


def HFunction(first_half: str, second_half: str) -> str:

    # one-way permutation function
    # function H (x, y)
    #   f(x) <- 2^x mod p
    #   b <- 0
    #   for i <- 0 to |x| do
    #       b <- b XOR (x[i] AND y[i])
    #   return f + y + b

    fx: str = function_F(first_half)
    hard_core_bit: int = 0
    for i in range(len(first_half)):
        hard_core_bit = (hard_core_bit ^ (int(first_half[i]) & int(second_half[i]))) % 2
    return fx + second_half + str(hard_core_bit)


def PRNG(initial_seed: str, n: int) -> str:

    # pseudorandom number generator
    # function G(x0)
    #   t <- aftual time in miliseconds convert to binary number
    #   output <- '1' (because we want 1 on first bit)
    #   for i <- 0 to |x0|- 1 do
    #       t <- H(first_half(t), second_half(t))
    #       output <- output * last_bit(t)
    #       t <- remove_last_bit(t)
    #   return output

    # result: str = '1'
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

minValue: str = '1' + '0' * (SEED_SIZE - 1)
maxValue: str = "{0:b}".format(n)

if __name__ == '__main__':
    print(f'początkowa liczba: {int(inputValue, 2)}; liczba bitów: {SEED_SIZE}')
    print(f'Przedział liczb: [{int(minValue,2)}, {int(maxValue,2)})')
    results: list = list()
    for _ in range(N):
        results.append(int(PRNG(inputValue, n), 2))
        MODULUS = abs(MODULUS - function_L(SEED_SIZE))
    print(f'results: {results}')
