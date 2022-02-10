#Project Euler Problem 13

def main():

	filename = 'project_euler_13.txt'
	with open(filename) as f:
		lines = f.readlines()

	numbers = [int(line.strip()) for line in lines]
	
	return str(sum(numbers))[:10]

print(main())