# Project Euler Problem 41


#                            Divisible by
# 1+2+3+4 = 10               -  
# 1+2+3+4+5 = 15             3 
# 1+2+3+4+5+6 = 21           3
# 1+2+3+4+5+6+7 = 28         - 
# 1+2+3+4+5+6+7+8 = 36       3 
# 1+2+3+4+5+6+7+8+9 = 45     3 
#
# Therefore we will only check 7 and 4 digit pandigital numbers 
# as the others cannot be prime due to the special property above


def main() -> int:

    # Try 7 digit numbers
    len_n = 7
    for n in range(7654321, 1234567, -2):
        if not is_prime(n):
            continue

        if not is_pandigital(n, len_n):
            continue

        return n

    # Try 4 digit numbers
    len_n = 4
    for n in range(4321, 2144, -2):
        if not is_prime(n):
            continue

        if not is_pandigital(n, len_n):
            continue

        return n


def is_pandigital(n: int, len_n: int) -> bool:
    n = str(n)
    if sorted(n) == ['1', '2', '3', '4', '5', '6', '7'][:len_n]:
        return True
    else:
        return False


def is_prime(n: int) -> bool:
    i = 2
    while (i * i <= n):
        if (n % i == 0):
            return False
        i += 1
    return True


print(main())
