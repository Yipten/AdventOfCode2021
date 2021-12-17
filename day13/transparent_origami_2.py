# AoC 2021 Day 13 Part 2
# Transparent Origami


def generate_grid(width, height, default_value=None):
    '''
    Generates a grid of a specific size.
    '''

    grid = []
    for i in range(height):
        grid.append([default_value] * width)
    return grid


def add_coords(coords):
    '''
    Adds points to grid based on coordinates.
    '''

    # find required grid width and height
    width = 0
    height = 0
    for coord in coords:
        if coord[0] + 1 > width:
            width = coord[0] + 1
        if coord[1] + 1 > height:
            height = coord[1] + 1

    # generate empty 2D list
    grid = generate_grid(width, height, False)

    # add coordinates to grid
    for coord in coords:
        grid[coord[1]][coord[0]] = True

    return grid


def fold_grid(grid, fold_direction, fold_position):
    '''
    Simulates folding the grid along the given vertical or horizontal line.
    '''

    original_width = len(grid[0])
    original_height = len(grid)
    folded_grid = []
    if fold_direction == 'x':
        width = max(fold_position, original_width - fold_position - 1)
        folded_grid = generate_grid(width, original_height)
        for r in range(original_height):
            for c in range(width):
                folded_grid[r][c] = grid[r][c] or grid[r][-(c + 1)]
    elif fold_direction == 'y':
        height = max(fold_position, original_height - fold_position - 1)
        folded_grid = generate_grid(original_width, height)
        for r in range(height):
            for c in range(original_width):
                folded_grid[r][c] = grid[r][c] or grid[-(r + 1)][c]
    return folded_grid


def find_num_dots(grid):
    '''
    Returns the number of dots visible on the grid.
    '''

    num_dots = 0
    for row in grid:
        num_dots += row.count(True)
    return num_dots


def main():
    # get input
    input_file = open('day13/input.txt')
    input_lines = input_file.readlines()
    input_file.close()

    # remove whitespace
    for i in range(len(input_lines)):
        input_lines[i] = input_lines[i].strip()

    # store coordinates as list of tuples
    coords = []
    while True:
        coord_strs = input_lines.pop(0).split(',')
        if coord_strs[0] == '':
            break
        coords.append((int(coord_strs[0]), int(coord_strs[1])))

    # store folds as list of tuples
    folds = []
    for line in input_lines:
        line = line.strip('fold along')
        fold_strs = line.split('=')
        folds.append((fold_strs[0], int(fold_strs[1])))

    grid = add_coords(coords)

    for fold in folds:
        grid = fold_grid(grid, fold[0], fold[1])

    # print grid in an easily readable form
    for row in grid:
        print_line = ''
        for col in row:
            if col:
                print_line += '#'
            else:
                print_line += '.'
        print(print_line)


if __name__ == '__main__':
    main()
