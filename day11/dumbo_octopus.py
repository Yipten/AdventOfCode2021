# AoC 2021 Day 11 Part 1
# Dumbo Octopus

def increment_all_energy_levels(energy_levels):
    '''
    Increments the energy level of each octopus.
    '''

    for row in energy_levels:
        for i in range(len(row)):
            row[i] += 1


def increment_adjacent_energy_levels(energy_levels, r, c):
    '''
    Increment the energy levels of octopuses adjacent to the given location.
    '''

    dr_options = (-1, 0, 1)
    if r == 0:
        dr_options = (0, 1)
    elif r == len(energy_levels) - 1:
        dr_options = (-1, 0)

    dc_options = (-1, 0, 1)
    if c == 0:
        dc_options = (0, 1)
    elif c == len(energy_levels) - 1:
        dc_options = (-1, 0)

    for dr in dr_options:
        for dc in dc_options:
            if dr == 0 and dc == 0:
                continue
            energy_levels[r + dr][c + dc] += 1


def find_num_flashes(energy_levels, num_cycles):
    '''
    Simulates the specified number of cycles of dumbo octopus flashing.
    '''

    num_flashes = 0
    for i in range(num_cycles):
        # each octopus gets its energy incremented
        increment_all_energy_levels(energy_levels)
        # initialize 2D list to keep track of which octopuses have flashed
        flashed = []
        for j in range(len(energy_levels)):
            flashed.append([False] * len(energy_levels[j]))
        # loop as many times as necessary
        prev_num_flashes = -1
        while num_flashes > prev_num_flashes:
            prev_num_flashes = num_flashes
            # energy of octopuses adjacent to those that will flash is incremented
            for r in range(len(energy_levels)):
                for c in range(len(energy_levels[r])):
                    if energy_levels[r][c] > 9 and not flashed[r][c]:
                        increment_adjacent_energy_levels(energy_levels, r, c)
                        num_flashes += 1
                        flashed[r][c] = True
        # reset energy of octopuses that flashed to 0
        for row in energy_levels:
            for j in range(len(row)):
                if row[j] > 9:
                    row[j] = 0
    return num_flashes


def main():
    # get input
    input_file = open('day11/input.txt')
    input_lines = input_file.readlines()
    input_file.close()

    # remove whitespace
    for i in range(len(input_lines)):
        input_lines[i] = input_lines[i].strip()

    # store input as 2D list of integers
    energy_levels = []
    for i in range(len(input_lines)):
        energy_levels.append([None] * len(input_lines[i]))
        for j in range(len(input_lines[i])):
            energy_levels[i][j] = int(input_lines[i][j])

    num_cycles = 100

    print('Number of flashes: ' + str(find_num_flashes(energy_levels, num_cycles)))


if __name__ == '__main__':
    main()
