#Project Euler Problem 21

def main() -> int:

	# No point checking primes
	primes = sieve(10_000)
	non_primes = [n for n in range(10_000) if not primes[n]]
	amicable_nums = []
	sum_amicable_nums = 0

	for a in non_primes:

		b = sum_proper_divisors(a)

		if (sum_proper_divisors(b) == a):

			if (b < 10_000) and (a != b) and ((b, a) not in amicable_nums):
				amicable_nums.append((a, b))
				sum_amicable_nums += a + b

	return sum_amicable_nums


def sum_proper_divisors(n: int) -> int:
	""" 
	Return the sum of the proper divisors of n
	"""
	sum_divisors = 1

	for i in range(2, round((n**0.5)) + 1):
		if n % i == 0:
			sum_divisors += (i + int(n / i))
	
	return sum_divisors 


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
