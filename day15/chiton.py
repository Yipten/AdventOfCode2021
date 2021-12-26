# AoC 2021 Day 15 Part 1
# Chiton

def generate_grid(width, height, default_value=None):
    '''
    Generates a grid of a specific size.
    '''

    grid = []
    for i in range(height):
        grid.append([default_value] * width)
    return grid


def find_min_risk(risk_levels, visited=[], x=0, y=0):
    '''
    Finds the minimum possible risk of going from the top-left corner to the
    bottom-right corner of the grid.
    '''

    # record that the current position has been visited
    visited.append((x, y))

    # don't count the risk level of the starting position
    if y == x == 0:
        risk = 0
    else:
        risk = risk_levels[y][x]

    # check if the bottom-right corner has been reached
    width = len(risk_levels[0])
    height = len(risk_levels)
    if x < width - 1 or y < height - 1:
        # find direction that leads to minimum risk value (no diagonals)
        # index 0 = risk value, index 1 = position
        path_options = [[], []]
        if y < height - 1 and not (x, y + 1) in visited:
            path_options[0].append(risk_levels[y + 1][x])
            path_options[1].append((x, y + 1))
        # if y > 0 and not (x, y - 1) in visited:
        #     path_options[0].append(risk_levels[y - 1][x])
        #     path_options[1].append((x, y - 1))
        if x < width - 1 and not (x + 1, y) in visited:
            path_options[0].append(risk_levels[y][x + 1])
            path_options[1].append((x + 1, y))
        # if x > 0 and not (x - 1, y) in visited:
        #     path_options[0].append(risk_levels[y][x - 1])
        #     path_options[1].append((x - 1, y))
        # list of risk levels of all paths from current position
        risk_options = []
        for i in range(len(path_options[1])):
            next_x = path_options[1][i][0]
            next_y = path_options[1][i][1]
            risk_options.append(find_min_risk(risk_levels, visited, next_x, next_y))
        # keep track of minimum possible risk value
        risk += min(risk_options)

    # remove points from list when moving back up down the stack
    visited.remove((x, y))

    return risk


def main():
    # get input
    with open('day15/input_example.txt') as input_file:
        input_lines = input_file.readlines()

    # remove whitespace
    for i in range(len(input_lines)):
        input_lines[i] = input_lines[i].strip()

    # convert input to grid
    risk_levels = generate_grid(len(input_lines[0]), len(input_lines))
    for i in range(len(input_lines)):
        for j in range(len(input_lines[i])):
            risk_levels[i][j] = int(input_lines[i][j])

    print('Minimum risk: ' + str(find_min_risk(risk_levels)))


if __name__ == '__main__':
    main()
