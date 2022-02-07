#Project Euler Problem 9
#Finding the product of abc where a+b+c=1000 and a^2+b^2=c^2

# a <= 332, b <= 333, c >= 335

def main():

	for a in range(1, 333):

		for b in range(2, 500):
			c = 1000 - a - b

			if (a**2 + b**2 == c**2):
				return a * b * c

print(main())

