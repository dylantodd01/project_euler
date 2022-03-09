# Project Euler Problem 49

from itertools import permutations

def main() -> str:
	primes = sieve(9999)
	four_digit_primes = [p for p in range(1000, 3339) if (primes[p] and p != 1487)]

	for a in four_digit_primes:
		perms = list(permutations(str(a)))
		b = a + 3330
		if primes[b] and (tuple(str(b)) in perms):
			c = b + 3330
			if primes[c] and (tuple(str(c)) in perms):
				return str(a) + str(b) + str(c)

def sieve(n: int) -> list[bool]:
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