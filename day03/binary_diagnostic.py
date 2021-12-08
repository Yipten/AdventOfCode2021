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
			if i[j] == '0':
				weights[j] -= 1
			else:	# must be '1'
				weights[j] += 1
	# loop through weights
	for weight in weights:
		# append 0 or 1 depending on weights
		mcb += str((weight > 0) * 1)
	return mcb

def invert(bin_val):
	# inverted value
	inv = '';
	# loop through bits
	for i in bin_val:
		if i == '0':
			inv += '1'
		else:	# must be '1'
			inv += '0'
	return inv

def str_to_bin(str_val):
	# binary value to return
	bin_val = 0
	for i in str_val:
		# left-shift one to make room for next bit
		bin_val <<= 1
		# set next bit based on character in string
		bin_val |= i == '1'
	return bin_val

def main():
	# get input
	input_file = open('input.txt')
	diagnostic_report = input_file.readlines()
	input_file.close()
	# remove whitespace
	for i in range(len(diagnostic_report)):
		diagnostic_report[i] = diagnostic_report[i].strip()
	# get gamma
	gamma = most_common_bits(diagnostic_report)
	# get epsilon by inverting gamma
	epsilon = invert(gamma)
	# get binary values of both
	gamma_bin = str_to_bin(gamma)
	epsilon_bin = str_to_bin(epsilon)
	# print result
	print('Power consumption: ' + str(gamma_bin * epsilon_bin))

if __name__ == '__main__':
	main()
