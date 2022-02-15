# Project Euler 19

import math

def main():

	num_sundays = 0

	# Calculate in range of 1901 - 1999
	for Y in range(1, 100):

		for m in range(1, 13):

			if not weekday(1, m, 19, Y):  # Sunday = 0
				num_sundays += 1

	# Calculate for 2000
	for m in range(1, 13):

		if not weekday(1, m, 20, 0):
			num_sundays += 1

	return num_sundays



def weekday(k, m, C, Y):
	"""
	Returns the day of the week of a given date
	(Sunday = 0, Monday = 1 etc)

	k is day (1-31)
	m is month (1-12)
	C is century (1987 has C = 19)
	Y is year (1987 has Y = 87)
	"""

	m -= 2
	if m <= 0:
		m += 12
		Y -= 1

	return ((k + math.floor(2.6*m - 0.2) - 2*C + Y + 
		math.floor(Y/4) + math.floor(C/4)) % 7)

print(main())