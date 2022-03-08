# Project Euler Problem 48

def main() -> int:
	return str(sum([(n ** n) for n in range(1, 1001)]))[-10:]

print(main())

