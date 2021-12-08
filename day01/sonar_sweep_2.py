# AoC 2021 Day 1 Part 2
# Sonar Sweep

# open input file
input_file = open('input.txt')
# read lines of input file to list of strings
depths_str = input_file.readlines()
input_file.close()
# list to contain integer values
depths = []
# convert list of strings to list of integers
for i in depths_str:
	depths.append(int(i))

# number of times the depth increases
num_increases = 0

# two moving windows
window_1 = []
window_2 = []
# initialize windows
for i in range(3):
	window_1.append(depths[i])
	window_2.append(depths[i + 1])
# compare first state of windows
if sum(window_2) > sum(window_1):
	num_increases += 1

# loop through depths
for i in range(3, len(depths) - 1):
	# move windows
	window_1.append(depths[i])
	window_1.pop(0)
	window_2.append(depths[i + 1])
	window_2.pop(0)
	# compare current and previous depths
	if sum(window_2) > sum(window_1):
		num_increases += 1
# print result
print('Number of depth increases: ' + str(num_increases))
