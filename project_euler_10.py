#Project Euler Problem 10
#Finding the sum of all the primes below two million

def main():

    primes = sieve(1999999)
    sum_primes = 0

    for i, p in enumerate(primes):
        if p:
            sum_primes += i

    return sum_primes


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