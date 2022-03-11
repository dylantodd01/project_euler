# Project Euler Problem 47

def main() -> int:
	primes = get_primes(150000)
	for n in range(100000, 150000):
		if (num_dist_prime_facs(n, primes) == 4) and (num_dist_prime_facs(n+1, primes) == 4) and (num_dist_prime_facs(n+2, primes) == 4) and (num_dist_prime_facs(n+3, primes) == 4): 
			return n

def num_dist_prime_facs(n: int, primes: list[int]) -> list[int]:
	i = 0
	prime_factors = []
	while True:
		if n % primes[i] == 0:
			prime_factors.append(primes[i])
			n /= primes[i]
		elif n == 1:
			return len(set(prime_factors))
		else:
			i += 1

def get_primes(n: int) -> list[int]:
	primes = sieve(n)
	return [p for p in range(1, n+1) if primes[p]]

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