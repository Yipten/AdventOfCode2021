# AoC 2021 Day 10 Part 2
# Syntax Scoring

def is_corrupted(line, matching_chars):
    '''
    Return whether the given line is corrupted.
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
                return True
    return False


def calculate_score(completion_str, char_points):
    '''
    Calculates and returns the score of the given completion string.
    '''

    score = 0
    for char in completion_str:
        score *= 5
        score += char_points[char]
    return score


def make_completion_str(line, matching_chars):
    '''
    Returns the completion string for the given line.
    '''

    # list of currently active opening characters
    opening_chars = []
    for char in line:
        # opening character
        if char in matching_chars.keys():
            opening_chars.append(char)
        # closing character
        elif char in matching_chars.values():
            del opening_chars[-1]
    # build completion string
    completion_str = ''
    for i in range(len(opening_chars) - 1, -1, -1):
        completion_str += matching_chars[opening_chars[i]]
    return completion_str

def get_middle_score(scores):
    '''
    Returns the middle score.
    '''

    scores_sorted = sorted(scores)
    return scores_sorted[int(len(scores_sorted) / 2)]


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
    # define character point values
    char_points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    # list and remove all corrupted lines
    for i in range(len(lines) - 1, -1, -1):
        if is_corrupted(lines[i], matching_chars):
            del lines[i]

    # list completion strings
    completion_strs = []
    for line in lines:
        completion_strs.append(make_completion_str(line, matching_chars))

    # list scores
    scores = []
    for string in completion_strs:
        scores.append(calculate_score(string, char_points))

    print('Score: ' + str(get_middle_score(scores)))


if __name__ == '__main__':
    main()
