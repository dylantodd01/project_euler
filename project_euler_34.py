#Project Euler Problem 34

import math

# 8 * 9! = 2_903_040 which is only a 7-digit number
# Therefore, the maximum number I will test is 7 * 9! 
# which is 2540160

def main() -> int:

	return sum([candidate for candidate in range(3, 2_540_161) if candidate == sum([math.factorial(int(digit)) for digit in str(candidate)])])

print(main())