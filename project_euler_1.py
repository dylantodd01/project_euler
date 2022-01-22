#Project Euler Problem 1
#Finding the sum of all the multiples of 3 or 5 below 1000

def main():
	multiples = [n for n in range(1, 1001) if (n % 3 == 0) or (n % 5 == 0)]
	return sum(multiples)

print(main())

