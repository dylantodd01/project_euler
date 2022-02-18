#Project Euler Problem 22

def main():

	names = import_names()

	total_score = 0
	for i, name in enumerate(names):
		total_score += (i + 1) * name_score(name)

	return total_score


def import_names():
	"""
	Import and return the names in the file
	"""
	filename = 'project_euler_22.txt'
	with open(filename) as file_object:
		names = file_object.read()
	
	# Formatting names
	names = names.replace('"', '')   # Remove the quotation around the names
	names = names.split(",")  # Put the names into a list
	names.sort()   # Sort names alphabetically
	
	return names


def name_score(name):

	score = 0
	for c in name:
		score += (ord(c) - 64)

	return score


print(main())