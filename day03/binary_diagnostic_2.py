# AoC 2021 Day 3 Part 2
# Binary Diagnostic

def find_o2_rating(diagnostic_report):
	# temporary list to manipulate
	bin_vals = diagnostic_report.copy()
	# number of bits in each value
	num_bits = len(bin_vals[0])
	# loop through each bit
	for i in range(num_bits):
		weight = 0
		# loop through each value
		for val in bin_vals:
			if val[i] == '0':
				weight -= 1
			else:	# must be '1'
				weight += 1
		# keep only values with the most common bit
		bit_to_keep = weight >= 0
		# counting backwards to prevent skipping elements
		for j in range(len(bin_vals) - 1, -1, -1):
			if int(bin_vals[j][i]) != bit_to_keep:
				bin_vals.remove(bin_vals[j])
		# check if there's only one value left
		if len(bin_vals) == 1:
			break
	return bin_vals[0]

def find_co2_rating(diagnostic_report):
	# temporary list to manipulate
	bin_vals = diagnostic_report.copy()
	# number of bits in each value
	num_bits = len(bin_vals[0])
	# loop through each bit
	for i in range(num_bits):
		weight = 0
		# loop through each value
		for val in bin_vals:
			if val[i] == '0':
				weight -= 1
			else:	# must be '1'
				weight += 1
		# keep only values with the least common bit
		bit_to_keep = weight < 0
		# counting backwards to prevent skipping elements
		for j in range(len(bin_vals) - 1, -1, -1):
			if int(bin_vals[j][i]) != bit_to_keep:
				bin_vals.remove(bin_vals[j])
		# check if there's only one value left
		if len(bin_vals) == 1:
			break
	return bin_vals[0]

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
	# get oxygen generator rating
	o2 = find_o2_rating(diagnostic_report)
	# get CO2 scrubber rating
	co2 = find_co2_rating(diagnostic_report)
	# get binary values
	o2_bin = str_to_bin(o2)
	co2_bin = str_to_bin(co2)
	# print result
	print('Life support rating: ' + str(o2_bin * co2_bin))

if __name__ == '__main__':
	main()
