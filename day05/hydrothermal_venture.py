# AoC 2021 Day 5 Part 1
# Hydrothermal Venture

def record_vertical_line(grid, x, y1, y2):
    # make sure that y1 is less than y2
    if y1 > y2:
        y1, y2 = y2, y1
    # increment the value of each point along the line
    for i in range(y1, y2 + 1):
        grid[x][i] += 1


def record_horizontal_line(grid, x1, x2, y):
    # make sure that x1 is less than x2
    if x1 > x2:
        x1, x2 = x2, x1
    # increment the value of each point along the line
    for i in range(x1, x2 + 1):
        grid[i][y] += 1


def record_line(grid, x1, y1, x2, y2):
    '''Records a line on the grid between the two points.'''

    if x1 == x2:
        record_vertical_line(grid, x1, y1, y2)
    elif y1 == y2:
        record_horizontal_line(grid, x1, x2, y1)


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
