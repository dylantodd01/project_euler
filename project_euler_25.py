#Project Euler Problem 25

def main():

	fib_seq = [1, 1]

	while len(str(fib_seq[-1])) < 1000:

		new_term = fib_seq[-2] + fib_seq[-1]
		fib_seq.append(new_term)

	return len(fib_seq)

print(main())