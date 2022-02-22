# Project Euler Problem 27

def main() -> int:

    primes = sieve(200_000)
    # b must be prime when n = 0
    b_values = [i for i in range(1001) if primes[i]]  
    max_num_primes = 0

    for a in range(-999, 1000):
        for b in b_values:
            current_num_primes = num_primes(a, b, primes)

            if current_num_primes > max_num_primes:
                max_num_primes = current_num_primes
                prod_ab = a * b

    return prod_ab


def num_primes(a: int, b: int, primes: list) -> int:
    """
    Returns the number of consecutive primes produced
    by the formula n**2 + a*n + b with n starting at 0
    """

    n, n_primes = 0, 0
    while primes[n**2 + a*n + b]:
        n_primes += 1
        n += 1
    return n_primes


def sieve(n):
    """
    Sieve of Eratosthenes
    Returns a True / False array representing prime 
    numbers up to n
    """

    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    i = 2
    while (i * i <= n):
        if sieve[i]:
            k = i * i
            while (k <= n):
                sieve[k] = False
                k += i
        i += 1
    return sieve


print(main())









