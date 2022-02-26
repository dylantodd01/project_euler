#Project Euler Problem 35

def main() -> int:

    primes = sieve(1000000)

    num_circ_primes = 0
    for n, prime in enumerate(primes):

        if not prime:
            continue

        num_circ_primes += 1  # Assume n is a circular prime
        for n_rotation in get_rotations(n):

            if primes[n_rotation]:
                continue

            # This runs if a rotation isn't prime and takes
            # back the assumption of n being a circular prime
            num_circ_primes -= 1
            break
    
    return num_circ_primes


def get_rotations(n: int) -> list[int]:
    """
    Returns a list of the rotations of the input n
    """
    n = [d for d in str(n)]

    rotations = []
    for i in range(len(n)):
        rotations.append(int(''.join(n)))
        n.append(n[0])
        del n[0]
        
    return rotations


def sieve(n: int) -> list[bool]:
    """
    Sieve of Eratosthenes
    Returns a True / False array representing prime 
    numbers up to n
    """

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