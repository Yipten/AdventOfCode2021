# AoC 2021 Day 2 Part 1
# Dive!

# read input file into list of strings
input_file = open('day02/input.txt')
lines = input_file.readlines()
input_file.close()
# split into two lists (one for direction, one for distance)
directions = []
distances = []
for line in lines:
	line_split = line.split()
	directions.append(line_split[0])
	distances.append(int(line_split[1]))

# horizontal position
position = 0
# depth below sea level
depth = 0

# loop through each instruction
for i in range(len(directions)):
	# check which direction to move in
	if directions[i] == 'forward':
		position += distances[i]
	elif directions[i] == 'down':
		depth += distances[i]
	else:	# must be 'up'
		depth -= distances[i]

# print product of position and depth
print(position * depth)
