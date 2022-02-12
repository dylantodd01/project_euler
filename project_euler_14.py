#Project Euler Problem 14


def main():

	max_terms = max_start = 0

	for i in range(1, 1_000_000, 2):
		num_terms = seq_len(i)
		if (num_terms > max_terms):
			max_terms, max_start = num_terms, i

	return (max_start, max_terms)


def is_even(n):
	"""
	Check if an input is even (True) or odd (False)
	"""
	if n % 2 == 0:
		return True
	return False


def seq_len(n):
	"""
	Generate the sequence for starting number n and returns length
	"""
	seq = [n]

	while n > 1:

		if is_even(n):
			n = (n / 2)

		else:
			n = (3 * n) + 1

		seq.append(n)

	return len(seq)


print(main())

