# Project Euler Problem 44

import math

def main() -> int:
	N = 2_500
	p = gen_pent_nums(N)
	for j in range(N):
		for k in range(j+1, N):
			p_j, p_k = p[j], p[k]
			if is_pentagonal(p_k + p_j) and is_pentagonal(p_k - p_j):
				return abs(p_k - p_j)

def gen_pent_nums(N: int) -> list[int]:
	return [int(n*(3*n - 1) / 2) for n in range(1, N+1)]

def is_pentagonal(n: int) -> bool:
	k = (math.sqrt(24*n + 1) + 1) / 6
	return k.is_integer()

print(main())

