# AoC 2021 Day 5 Part 2
# Hydrothermal Venture

def record_vertical_line(grid, x, y1, y2):
    # make sure that y1 is less than y2
    if y1 > y2:
        y1, y2 = y2, y1
    # increment the value of each point along the line
    for i in range(y1, y2 + 1):
        grid[i][x] += 1


def record_horizontal_line(grid, x1, x2, y):
    # make sure that x1 is less than x2
    if x1 > x2:
        x1, x2 = x2, x1
    # increment the value of each point along the line
    for i in range(x1, x2 + 1):
        grid[y][i] += 1


def record_diagonal_line(grid, x1, y1, x2, y2):
    # make sure that x1 is less than x2
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    # figure out if y values require counting up or down
    up = y1 < y2
    # find the length of the line
    length = x2 - x1 + 1
    # increment the value of each point along the line
    j = y1
    for i in range(x1, x2 + 1):
        grid[j][i] += 1
        if up:
            j += 1
        else:
            j -= 1


def record_line(grid, x1, y1, x2, y2):
    '''Records a line on the grid between the two points.'''

    if x1 == x2:
        record_vertical_line(grid, x1, y1, y2)
    elif y1 == y2:
        record_horizontal_line(grid, x1, x2, y1)
    else:
        record_diagonal_line(grid, x1, y1, x2, y2)


def count_overlaps(grid):
    '''Counts the number of points where at least two lines overlap.'''

    num_overlaps = 0
    for row in grid:
        for i in row:
            num_overlaps += i > 1
    return num_overlaps


def main():
    # get input
    input_file = open('day05/input.txt')
    raw_input = input_file.readlines()
    input_file.close()

    # separate raw input into usable data
    x1_list = []
    y1_list = []
    x2_list = []
    y2_list = []
    for line in raw_input:
        points = line.split('->')
        point1 = points[0].split(',')
        point2 = points[1].split(',')
        x1_list.append(int(point1[0]))
        y1_list.append(int(point1[1]))
        x2_list.append(int(point2[0]))
        y2_list.append(int(point2[1]))

    # make 1,000 by 1,000 grid for keeping track of lines
    grid = []
    for i in range(1000):
        grid.append([0] * 1000)

    for i in range(len(raw_input)):
        record_line(grid, x1_list[i], y1_list[i], x2_list[i], y2_list[i])

    num_overlaps = count_overlaps(grid)

    print('Number of overlaps: ' + str(num_overlaps))


if __name__ == '__main__':
    main()
