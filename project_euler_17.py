#Project Euler Problem 17

#Correct answer is 21124

from num2words import num2words

def main():

	letter_sum = 0
	for n in range(1, 1001):
		number = num2words(n).replace(" ", "").replace("-", "")
		letter_sum += len(number)

	return(letter_sum)

print(main())