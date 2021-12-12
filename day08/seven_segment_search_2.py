# AoC Day 8 Part 1
# Seven Segment Search

def identify_possible_digits(pattern):
    '''
    Identifies the possible digits that could be represented by each pattern
    depending on the length of each pattern.
    '''

    pattern_length = len(pattern)

    if pattern_length == 2:
        # 2 segments used to display 1
        return 1
    elif pattern_length == 3:
        # 3 segments used to display 7
        return 7
    elif pattern_length == 4:
        # 4 segments used to display 4
        return 4
    elif pattern_length == 5:
        # 5 segments used to display 2, 3, and 5
        return (2, 3, 5)
    elif pattern_length == 6:
        # 6 segments used to display 0, 6, and 9
        return (0, 6, 9)
    elif pattern_length == 7:
        # 7 segments used to display 8
        return 8


def identify_digits(line):
    '''
    Identifies which digits correspond to each pattern.
    '''

    for pattern in line.keys():
        line[pattern] = identify_possible_digits(pattern)


def main():
    # get input
    input_file = open('day08/input_short.txt')
    entries = input_file.readlines()
    input_file.close()

    # split up input into lists
    pattern_lines = []
    output_pattern_lines = []
    for i in range(len(entries)):
        # split line in two
        split_line = entries[i].split('|')
        # store first part of line in list of dictionaries
        pattern_lines.append({})
        line = split_line[0].split()
        for j in range(len(line)):
            pattern_lines[i][line[j]] = None
        # store second part of line in list of lists
        output_pattern_lines.append(split_line[1].split())

    for line in pattern_lines:
        identify_digits(line)

    print('done')


if __name__ == '__main__':
    main()
