#Project Euler Problem 3
#Finding the largest prime factor of 600851475143

def main():
	prime_factors = []
	N, i = 600851475143, 2
	while i <= N:
		if (N % i) == 0:
			prime_factors.append(i)
			N /= i
		else:
			i += 1
	return prime_factors[-1]

print(main())
