#Project Euler Problem 6
#Finding the difference between the sum of the squares 
#of the first one hundred natural numbers and the square of the sum

def main():

	s = s_squares = 0

	for n in range(1, 101):
		s += n
		s_squares += n**2

	return (s**2 - s_squares)

print(main())
