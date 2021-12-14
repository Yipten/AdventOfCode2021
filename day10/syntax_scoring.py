# AoC 2021 Day 10 Part 1
# Syntax Scoring

def find_illegal_char(line, matching_chars):
    '''
    Find the first illegal character, if it exists.
    '''

    # list of currently active opening characters
    opening_chars = []
    for char in line:
        # opening character
        if char in matching_chars.keys():
            opening_chars.append(char)
        # closing character
        elif char in matching_chars.values():
            if matching_chars[opening_chars.pop()] != char:
                return char
    return None


def main():
    # get input
    input_file = open('day10/input.txt')
    lines = input_file.readlines()
    input_file.close()

    # define matching characters
    matching_chars = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    # define illegal character point values
    char_points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    # create a list of all illegal characters
    illegal_chars = []
    for line in lines:
        illegal_char = find_illegal_char(line, matching_chars)
        if illegal_char != None:
            illegal_chars.append(illegal_char)

    # calculate syntax error score
    score = 0
    for char in illegal_chars:
        score += char_points[char]

    print('Syntax error score: ' + str(score))


if __name__ == '__main__':
    main()
