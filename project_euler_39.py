#Project Euler Problem 39

from collections import Counter

def main() -> int:

	solutions = []
	for a in range(1, 333):
		for b in range(a, 500):
			c = (a**2 + b**2) ** 0.5

			if (c // 1) == c and (a + b + c) <= 1000:
				solutions.append(int(a + b + c))

	return Counter(solutions).most_common(1)[0][0]

print(main())



