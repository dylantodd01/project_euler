#Project Euler Problem 12

# Old solution took ~2.8s

def main():

	n = tri_num = 1

	while (divisors(tri_num) <= 500):
		tri_num = (n * (n + 1)) / 2
		n += 1

	return tri_num


def divisors(n):
	"""
	Returns number of divisors of n
	"""

	i = 1
	result = 0

	while (i * i < n):

		if (n % i == 0):
			result += 2

		i += 1

	if (i * i == n):
		result += 1

	return result

print(main())
