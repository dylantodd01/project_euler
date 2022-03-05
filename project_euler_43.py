# Project Euler Problem 43

from itertools import permutations

def main() -> int:

	perms = list(permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']))
	divisors = [2, 3, 5, 7, 11, 13, 17]

	output_sum = 0
	for perm in perms:
		output_sum += check_for_property(perm, divisors)

	return output_sum


def check_for_property(perm: tuple, divisors: list) -> int:

	for i in range(7):
		if perm[0] == '0':
			return 0

		n = int(perm[i+1] + perm[i+2] + perm[i+3])

		# If n is not divisible by the required divisor, exit loop
		if (n % divisors[i]) != 0:
			return 0

	return int(''.join(perm))


print(main())
