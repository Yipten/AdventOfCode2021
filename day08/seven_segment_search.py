# AoC Day 8 Part 1
# Seven Segment Search

def main():
    # get input
    input_file = open('day08/input.txt')
    entries = input_file.readlines()
    input_file.close()

    # separate out ouput digits
    output_digits = []
    for i in entries:
        output_line = i.split('|')[1]
        output_digits.append(output_line.split())

    # count number of digits that must be
    # - 1 (2 segments)
    # - 4 (4 segments)
    # - 7 (3 segments)
    # - 8 (7 segments)
    num_unique_digits = 0
    for line in output_digits:
        for digit in line:
            if len(digit) in (2, 3, 4, 7):
                num_unique_digits += 1

    print('Number of unique digits: ' + str(num_unique_digits))


if __name__ == '__main__':
    main()
