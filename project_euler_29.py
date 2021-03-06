#Project Euler Problem 29

def main() -> int:

	distinct_terms = []

	for a in range(2, 101):
		for b in range(2, 101):
			if (a ** b not in distinct_terms):
				distinct_terms.append(a ** b)

	return len(distinct_terms)

print(main())