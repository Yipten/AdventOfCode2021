# AoC 2021 Day 9 Part 2
# Smoke Basin

from math import prod


def check_vertical_neighbors(heightmap, r, c):
    '''
    Checks if the given point is less than both of its vertical neighbors.
    '''

    # prevent index errors by checking if the point is at an edge
    if r == 0:
        return heightmap[r][c] < heightmap[r + 1][c]
    elif r == len(heightmap) - 1:
        return heightmap[r][c] < heightmap[r - 1][c]
    return (heightmap[r][c] < heightmap[r - 1][c]
            and heightmap[r][c] < heightmap[r + 1][c])


def calculate_basin_size(heightmap, r, c, counted_points=[]):
    '''
    Recursively calculates and returns the size of the basin surrounding the
    given point.
    '''

    # only allow each point to be counted once
    if (r, c) in counted_points:
        return 0

    # record which points have been counted
    counted_points.append((r, c))

    # start counting at 1 to include the given point
    basin_size = 1

    # TODO: should the comparisons use ">" or ">="?
    # TODO: make it so points can't be counted twice (that happens right now) (maybe keep track of already counted points using a list of tuples)
    # up
    if (r > 0
            and heightmap[r - 1][c] > heightmap[r][c]
            and heightmap[r - 1][c] != 9):
        basin_size += calculate_basin_size(heightmap, r - 1, c, counted_points)

    # down
    if (r < len(heightmap) - 1
            and heightmap[r + 1][c] > heightmap[r][c]
            and heightmap[r + 1][c] != 9):
        basin_size += calculate_basin_size(heightmap, r + 1, c, counted_points)

    # right
    if (c < len(heightmap[0]) - 1
            and heightmap[r][c + 1] > heightmap[r][c]
            and heightmap[r][c + 1] != 9):
        basin_size += calculate_basin_size(heightmap, r, c + 1, counted_points)

    # left
    if (c > 0
        and heightmap[r][c - 1] > heightmap[r][c]
            and heightmap[r][c - 1] != 9):
        basin_size += calculate_basin_size(heightmap, r, c - 1, counted_points)

    return basin_size


def calculate_basin_sizes(heightmap):
    '''
    Calculates and returns a list of basin sizes.
    '''

    basin_sizes = []
    # RC Cola
    for r in range(len(heightmap)):
        for c in range(len(heightmap[r])):
            # prevent index errors by checking if the point is at an edge
            if c == 0:
                if (heightmap[r][c] < heightmap[r][c + 1]
                        and check_vertical_neighbors(heightmap, r, c)):
                    basin_sizes.append(calculate_basin_size(heightmap, r, c))
            elif c == len(heightmap[r]) - 1:
                if (heightmap[r][c] < heightmap[r][c - 1]
                        and check_vertical_neighbors(heightmap, r, c)):
                    basin_sizes.append(calculate_basin_size(heightmap, r, c))
            elif (heightmap[r][c] < heightmap[r][c - 1]
                  and heightmap[r][c] < heightmap[r][c + 1]
                  and check_vertical_neighbors(heightmap, r, c)):
                basin_sizes.append(calculate_basin_size(heightmap, r, c))
    return basin_sizes


def find_three_largest(basin_sizes):
    '''
    Finds and returns the sizes of the three largest basins.
    '''

    three_largest = []
    for i in range(3):
        temp_max = max(basin_sizes)
        three_largest.append(temp_max)
        basin_sizes.remove(temp_max)
    return three_largest


def main():
    # get input
    input_file = open('day09/input.txt')
    input_lines = input_file.readlines()
    input_file.close()

    # remove whitespace
    for i in range(len(input_lines)):
        input_lines[i] = input_lines[i].strip()

    # store input as 2D list of integers
    heightmap = []
    for i in range(len(input_lines)):
        heightmap.append([None] * len(input_lines[i]))
        for j in range(len(input_lines[i])):
            heightmap[i][j] = int(input_lines[i][j])

    basin_sizes = calculate_basin_sizes(heightmap)
    three_largest = find_three_largest(basin_sizes)
    three_largest_prod = prod(three_largest)
    print('Product of three largest basin sizes: ' + str(three_largest_prod))


if __name__ == '__main__':
    main()
