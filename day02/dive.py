# AoC 2021 Day 2 Part 1
# Dive!

# read input file into list of strings
inputFile = open('input.txt')
lines = inputFile.readlines()
inputFile.close()
# split into two lists (one for direction, one for distance)
directions = []
distances = []
for line in lines:
	lineSplit = line.split()
	directions.append(lineSplit[0])
	distances.append(lineSplit[1])
