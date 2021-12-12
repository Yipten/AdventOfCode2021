# AoC Day 8 Part 1
# Seven Segment Search

def find_easy_digits(digit_pattern_lines):
    '''
    Finds which patterns correspond to the digits 1, 4, 7, and 8
    '''

    for line in digit_pattern_lines:
        for i in line.keys():
            # 2 segments used to display 1
            if len(i) == 2:
                line[i] = 1
            # 4 segments used to display 4
            elif len(i) == 4:
                line[i] = 4
            # 3 segments used to display 7
            elif len(i) == 3:
                line[i] = 7
            # 7 segments used to display 8
            elif len(i) == 7:
                line[i] = 8


def main():
    # get input
    input_file = open('day08/input_short.txt')
    entries = input_file.readlines()
    input_file.close()

    # split up input into lists
    digit_pattern_lines = []
    output_digit_patterns = []
    for i in range(len(entries)):
        # split line in two
        split_line = entries[i].split('|')
        # store first part of line in list of dictionaries
        digit_pattern_lines.append({})
        line = split_line[0].split()
        for j in range(len(line)):
            digit_pattern_lines[i][line[j]] = None
        # store second part of line in list of lists
        output_digit_patterns.append(split_line[1].split())

    find_easy_digits(digit_pattern_lines)

    print('done')


if __name__ == '__main__':
    main()
