#Project Euler Problem 7
#Finding the 10_001st prime number

def main():

	primes = sieve(999999)
	n = 0
	for i, p in enumerate(primes):
		if p:
			n += 1
		if n == 10001:
			return i

def sieve(n):
    
    ''' Sieve of Eratosthenes '''

    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    i = 2

    while (i * i <= n):

        if sieve[i]:
            k = i * i

            while (k <= n):
                sieve[k] = False
                k += i

        i += 1

    return sieve


print(main())
