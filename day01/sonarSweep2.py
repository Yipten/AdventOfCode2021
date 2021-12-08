# AoC 2021 Day 1 Part 2
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

# two moving windows
window1 = []
window2 = []
# initialize windows
for i in range(3):
	window1.append(depths[i])
	window2.append(depths[i + 1])
# compare first state of windows
if sum(window2) > sum(window1):
	numIncreases += 1

# loop through depths
for i in range(3, len(depths) - 1):
	# move windows
	window1.append(depths[i])
	window1.pop(0)
	window2.append(depths[i + 1])
	window2.pop(0)
	# compare current and previous depths
	if sum(window2) > sum(window1):
		numIncreases += 1
# print result
print('Number of depth increases: ' + str(numIncreases))
