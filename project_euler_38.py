#Project Euler Problem 38


def main() -> int:

	multiplier = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	max_result = 0

	for n in range(1, 9):
		current_multiplier = multiplier[:n+1]

		for i in range(1, 9999):

			result = ''
			for number in current_multiplier:
				result += str(number * i)

				if len(result) > 9:
					break
			
			if sorted(result) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
				max_result = max(max_result, int(result))

	return max_result


print(main())