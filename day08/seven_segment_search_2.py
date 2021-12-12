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


def get_num_common_segments(pattern_1, pattern_2):
    '''
    Returns the number of lit segments the two given patterns have in common.
    '''

    num_common_segments = 0
    for segment in pattern_1:
        if segment in pattern_2:
            num_common_segments += 1
    return num_common_segments


def identify_5_char_patterns(line):
    '''
    Identifies patterns that are five characters long.
    '''

    # get easy patterns
    patterns = list(line.keys())
    digits = list(line.values())
    pattern_of_1 = patterns[digits.index(1)]
    pattern_of_4 = patterns[digits.index(4)]

    for pattern in line.keys():
        # skip over patterns not five characters long
        if len(pattern) != 5:
            continue
        common_with_1 = get_num_common_segments(pattern, pattern_of_1)
        common_with_4 = get_num_common_segments(pattern, pattern_of_4)
        if common_with_1 == 2:
            # has to be a 3
            line[pattern] = 3
        elif common_with_4 == 2:
            # has to be a 2
            line[pattern] = 2
        else:   # only other option
            # has to be a 5
            line[pattern] = 5


def identify_6_char_patterns(line):
    '''
    Identifies patterns that are six characters long.
    '''

    # get easy patterns
    patterns = list(line.keys())
    digits = list(line.values())
    pattern_of_1 = patterns[digits.index(1)]
    pattern_of_4 = patterns[digits.index(4)]
    pattern_of_7 = patterns[digits.index(7)]
    pattern_of_8 = patterns[digits.index(8)]

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
        identify_5_char_patterns(line)

    print('done')

if __name__ == '__main__':
    main()
