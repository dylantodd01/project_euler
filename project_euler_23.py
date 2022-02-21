# Project Euler Problem 23

def main() -> int:

	#primes = sieve(28124)
	abundant_nums = [n for n in range(28124) if (is_abundant(n))]

	output = [False] * 28124
	N = len(abundant_nums)

	for i in range(N):
		for j in range(i, N):
			abundant_sum = abundant_nums[i] + abundant_nums[j]
			if abundant_sum <= 28123:
				output[abundant_sum] = True

	final_sum = 0
	for n, ab_sum in enumerate(output):
		if not ab_sum:
			final_sum += n

	return final_sum



def is_abundant(n: int) -> bool:
	""" 
	Return True if n is an abundant number, else False
	"""
	if not n: return False

	sum_divisors = 1

	for i in range(2, round((n**0.5)) + 1):
		if n % i == 0:
			# Making sure we don't double count sqrt(n)
			sum_divisors += (i + int(n / i)) if (i != int(n / i)) else (i)

	return (sum_divisors > n)


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

import time
t0 = time.time()
print(main())
t1 = time.time()
print(t1-t0)

# 2.0s