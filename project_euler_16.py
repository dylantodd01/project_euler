#Project Euler Problem 16

def main():

	n, s = str(2 ** 1000), 0
	for d in n:
		s += int(d)

	return s


print(main())

