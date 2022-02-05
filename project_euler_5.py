#Project Euler Problem 5
#Finding the smallest positive number that is evenly divisible by the numbers from 1 to 20


def main():

	primes = [2, 3, 5, 7, 11, 13, 17, 19]
	non_primes = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]

	multiple = 1
	for p in primes:
		multiple *= p

	multiplier = 1
	while True:

		candidate = multiple * multiplier
		multiplier += 1

		for n in non_primes:

			if (candidate % n) != 0:
				break

			elif n == 20:
				return candidate
		

print(main())
