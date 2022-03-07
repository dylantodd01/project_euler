# Project Euler Problem 45

# All hexagonal numbers are triangular

import math

def main() -> int:
	n = 286
	while True:
		H = n * (2*n - 1)
		
		if is_pentagonal(H):
			return H
			break

		n += 1

def is_pentagonal(n: int) -> bool:
	k = (math.sqrt(24*n + 1) + 1) / 6
	return k.is_integer()


print(main())
