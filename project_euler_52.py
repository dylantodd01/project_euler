# Project Euler Problem 52

def main() -> int:
	n = 1
	while True:
		n_sorted = sorted(str(n))
		for i in range(2, 7):
			candidate = n * i
			if sorted(str(candidate)) != n_sorted:
				break
			if i == 6:
				return n

		n += 1
			

print(main())