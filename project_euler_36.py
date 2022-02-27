#Project Euler Problem 36


def main() -> int:

	return sum([n for n in range(1000000) if (is_palindrome(n) and is_palindrome(bin(n)[2:]))])


def is_palindrome(n: int) -> bool:
	"""
	Returns True if n is a palindrome or False if not
	"""
	n = str(n)
	for i in range(len(n) // 2):

		if n[i] != n[-1-i]: 
			return False
	
	return True

print(main())