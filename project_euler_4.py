#Project Euler Problem 4
#Finding the largest palindrome made from the product of two 3-digit numbers

def main():
	max_palindrome = 0

	for i in range(100, 1000):
		for j in range(100, 1000):
			if is_palindrome(i*j) and (i * j) > max_palindrome:
				max_palindrome = i * j

	return max_palindrome

def is_palindrome(n):
	n = str(n)
	for i in range(len(n) // 2):
		if n[i] != n[-1-i]:
			return False
	return True

print(main())