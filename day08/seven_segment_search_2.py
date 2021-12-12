# AoC Day 8 Part 1
# Seven Segment Search

def identify_easy_patterns(line):
    '''
    Identifies which patterns correspond to 1, 4, 7, and 8
    '''

    for pattern in line.keys():
        pattern_length = len(pattern)
        if pattern_length == 2:
            # 2 segments used to display 1
            line[pattern] = 1
        elif pattern_length == 4:
            # 4 segments used to display 4
            line[pattern] = 4
        elif pattern_length == 3:
            # 3 segments used to display 7
            line[pattern] = 7
        elif pattern_length == 7:
            # 7 segments used to display 8
            line[pattern] = 8


def identify_5_char_patterns(line):
    '''
    Identifies patterns that are 5 characters long.
    '''

    pass


def identify_6_char_patterns(line):
    '''
    Identifies patterns that are 6 characters long.
    '''

    pass


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
        identify_easy_patterns(line)

    print('done')


if __name__ == '__main__':
    main()
