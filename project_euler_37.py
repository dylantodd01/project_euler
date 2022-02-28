#Project Euler Problem 37


def main() -> int:

	primes = sieve(750000)
	truncatable_primes = []

	for n, prime in enumerate(primes):

		if (n in {2, 3, 5, 7}) or (not primes[n]):
			continue

		truncatable_prime = True

		candidate = n
		while len(str(candidate)) > 1 and truncatable_prime:
			candidate = truncate_right(candidate)
			if not primes[candidate]:
				truncatable_prime = False

		candidate = n
		while len(str(candidate)) > 1 and truncatable_prime:
			candidate = truncate_left(candidate)
			if not primes[candidate]:
				truncatable_prime = False

		if truncatable_prime:
			truncatable_primes.append(n)

	return sum(truncatable_primes)



def truncate_right(n: int) -> int:

	if len(str(n)) < 2: return None
	return int(str(n)[:-1])


def truncate_left(n: int) -> int:

	if len(str(n)) < 2: return None
	return int(str(n)[1:])


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