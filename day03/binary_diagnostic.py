# AoC 2021 Day 3 Part 1
# Binary Diagnostic

def most_common_bits(bin_vals):
	# string to store most common bits
	mcb = '';
	# weights of zeros (negative) vs ones (positive)
	weights = [0] * len(bin_vals[0])
	# loop through binary values
	for i in bin_vals:
		# loop through bits
		for j in range(len(i)):
			if i[j] == 0:
				weights[j] -= 1
			else:	# must be 1
				weights[j] += 1
	# loop through weights
	for i in weights:
		# append 0 or 1 depending on weights
		mcb += str((weights > 0) * 1)

def invert(bin_val):

def main():
	# get input
	input_file = open('input.txt')
	diagnostic_report = input_file.readlines()
	input_file.close()
	# get gamma rate
	gamma = most_common_bits(diagnostic_report)
	# get epsilon rate
	epsilon = invert(gamma)

if __name__ == '__main__':
	main()
