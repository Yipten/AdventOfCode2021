# AoC 2021 Day 9 Part 1
# Smoke Basin

def check_vertical_neighbors(heightmap, r, c):
    '''
    Checks if the given point is less than both of its vertical neighbors.
    '''

    if r == 0:
        return heightmap[r][c] < heightmap[r + 1][c]
    elif r == len(heightmap) - 1:
        return heightmap[r][c] < heightmap[r - 1][c]
    return heightmap[r][c] < heightmap[r - 1][c] and heightmap[r][c] < heightmap[r + 1][c]


def find_low_point_heights(heightmap):
    '''
    Find all low points and return a list of their heights.
    '''

    low_point_heights = []
    # RC Cola
    for r in range(len(heightmap)):
        for c in range(len(heightmap[r])):
            if c == 0:
                if (heightmap[r][c] < heightmap[r][c + 1]
                        and check_vertical_neighbors(heightmap, r, c)):
                    low_point_heights.append(heightmap[r][c])
            elif c == len(heightmap[r]) - 1:
                if (heightmap[r][c] < heightmap[r][c - 1]
                        and check_vertical_neighbors(heightmap, r, c)):
                    low_point_heights.append(heightmap[r][c])
            elif (heightmap[r][c] < heightmap[r][c - 1]
                  and heightmap[r][c] < heightmap[r][c + 1]
                  and check_vertical_neighbors(heightmap, r, c)):
                low_point_heights.append(heightmap[r][c])
    return low_point_heights


def calculate_risk_level_sum(heightmap):
    '''
    Calculates and returns the sum of the risk levels of all low points.
    '''

    low_point_heights = find_low_point_heights(heightmap)
    # effectively add one to each height in the list
    risk_level_sum = sum(low_point_heights) + len(low_point_heights)
    return risk_level_sum


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

    print('Sum of risk levels: ' + str(calculate_risk_level_sum(heightmap)))


if __name__ == '__main__':
    main()
