#Project Euler Problem 21

def main():

	amicable_nums = []
	sum_amicable_nums = 0

	for a in range(1, 10_000):

		b = sum_of_divisors(a)

		if (sum_of_divisors(b) == a):

			if (b < 10_000) and (a != b) and ((b, a) not in amicable_nums):
				amicable_nums.append((a, b))
				sum_amicable_nums += a + b

	return sum_amicable_nums


def sum_of_divisors(n):

	sum_divisors = 0
	for i in range(1, n//2 + 1):

		if (n % i == 0):
			sum_divisors += i

	return sum_divisors


print(main())