#Project Euler Problem 30

def main() -> int:

	sum_nums = 0
	for n in range(200000):
		sum_powers = 0

		for d in str(n):
			sum_powers += int(d) ** 5

		if sum_powers == n:
			sum_nums += n

	return sum_nums

print(main())
