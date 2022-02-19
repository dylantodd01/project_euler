# Project Euler Problem 24

from itertools import permutations

def main():
	perms = list(permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

	lexi_perms = []
	for perm in perms:

		n = ''
		for d in perm:
			n += str(d)

		lexi_perms.append(int(n))

	lexi_perms.sort()

	return lexi_perms[999999]

print(main())