#Project Euler Problem 2
#Finding the sum of all even Fibonacci terms below four million

def main():
	even_terms = [n for n in fib(4000000) if (n % 2 == 0)]
	return sum(even_terms)

def fib(max_val):
	seq = [1, 2]
	while seq[-1] <= max_val:
		seq.append(seq[-1] + seq[-2])
	return seq

print(main())
