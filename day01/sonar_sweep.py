# AoC 2021 Day 1 Part 1
# Sonar Sweep

# open input file
file = open('input.txt')
# read lines of input file to list of strings
depths_str = file.readlines()
# list to contain integer values
depths = []
# convert list of strings to list of integers
for i in depths_str:
	depths.append(int(i))

# number of times the depth increases
num_increases = 0
# set previous value to first depth
prev_depth = depths[0]
# loop through depth values and count number of increases
for depth in depths:
	# compare current and previous depths
	if depth > prev_depth:
		num_increases += 1
	# remember previous depth
	prev_depth = depth
# print result
print('Number of depth increases: ' + str(num_increases))
