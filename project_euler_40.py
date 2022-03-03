# Project Euler Problem 40

import math

def main() -> int:

	n, i = '', 1
	while len(n) <= 1_000_000:
		n += str(i)
		i += 1

	return (int(n[0]) * int(n[9]) * int(n[99]) * int(n[999]) * int(n[9999]) * int(n[99999]) * int(n[999999]))

print(main())

