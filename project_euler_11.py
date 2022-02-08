#Project Euler Problem 11

def main():

	data = import_data()

	mp_across = mp_vertical = mp_diagonal_1 = mp_diagonal_2 = 0

	products = [check_across(data), check_vertical(data), check_diagonal_1(data), check_diagonal_2(data)]

	return max(products)

def import_data():
	filename = 'project_euler_11.txt'
	with open(filename) as file_object:
		lines = file_object.readlines()

	data = []
	for line in lines:
		formatted_line = []
		formatted_line = list(map(int, line.split()))
		data.append(formatted_line)

	return data
 

def check_across(data):
	mp_across = 0
	for row in range(20):

		for number in range(17):
			product = data[row][number] * data[row][number + 1] * data[row][number + 2] + data[row][number + 3]
			mp_across = max(product, mp_across)

	return mp_across

def check_vertical(data):
	mp_vertical = 0
	for number in range(20):
		for row in range(17):
			product = data[row][number] * data[row + 1][number] * data[row + 2][number] + data[row + 3][number]
			mp_vertical = max(product, mp_vertical)

	return mp_vertical

def check_diagonal_1(data):
	mp_diagonal_1 = 0
	for row in range(17):
		for number in range(17):
			product = data[row][number] * data[row + 1][number + 1] * data[row + 2][number + 2] * data[row + 3][number + 3]
			mp_diagonal_1 = max(product, mp_diagonal_1)

	return mp_diagonal_1

def check_diagonal_2(data):
	mp_diagonal_2 = 0
	for row in range(17):
		for number in range(3, 20):
			product = data[row][number] * data[row + 1][number - 1] * data[row + 2][number - 2] * data[row + 3][number - 3]
			mp_diagonal_2 = max(product, mp_diagonal_2)

	return mp_diagonal_2


print(main())