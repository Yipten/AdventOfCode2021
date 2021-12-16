# AoC 2021 Day 11 Part 1
# Dumbo Octopus

def increment_energy_levels(energy_levels):
    '''
    Increments the energy level of each octopus.
    '''

    for row in energy_levels:
        for i in range(len(row)):
            row[i] += 1


def increment_adjacent_energy_levels(energy_levels, r, c):
    '''
    Recursively increment the energy levels of octopuses adjacent to the given
    location.
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
            energy_levels[r + dr][c + dc] += 1
            if energy_levels[r + dr][c + dc] > 9:
                # TODO: this currently causes infinite recursion (I think)
                increment_adjacent_energy_levels(energy_levels, r + dr, c + dc)


def find_num_flashes(energy_levels, num_cycles):
    '''
    Simulates the specified number of cycles of dumbo octopus flashing.
    '''

    num_flashes = 0
    for i in range(num_cycles):
        # each octopus gets its energy incremented
        increment_energy_levels(energy_levels)
        # energy of octopuses adjacent to those that will flash is incremented
        for r in range(len(energy_levels)):
            for c in range(len(energy_levels[r])):
                if energy_levels[r][c] > 9:
                    increment_adjacent_energy_levels(energy_levels, r, c)
        # octopuses flash and their energy is reset to 0
        for row in energy_levels:
            for i in range(len(row)):
                if row[i] > 9:
                    num_flashes += 1
                    row[i] = 0
    return num_flashes


def main():
    # get input
    input_file = open('day11/input_short.txt')
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
