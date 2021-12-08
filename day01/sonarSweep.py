# AoC 2021 Day 1 Part 1
# Sonar Sweep

# open input file
file = open('input.txt')
# read lines of input file to list of strings
depthsStr = file.readlines()
# list to contain integer values
depths = []
# convert list of strings to list of integers
for i in depthsStr:
	depths.append(int(i))

# number of times the depth increases
numIncreases = 0
# set previous value to first depth
prevDepth = depths[0]
# loop through depth values and count number of increases
for depth in depths:
	# compare current and previous depths
	if depth > prevDepth:
		numIncreases += 1
	# remember previous depth
	prevDepth = depth
# print result
print('Number of depth increases: ' + str(numIncreases))
