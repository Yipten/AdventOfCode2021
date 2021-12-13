# AoC 2021 Day 9 Part 1
# Smoke Basin

def main():
    # get input
    input_file = open('day09/input_short.txt')
    input_lines = input_file.readlines()
    input_file.close()

    # remove whitespace
    for i in range(len(input_lines)):
        input_lines[i] = input_lines[i].strip()

    # store input as 2D list of integers
    heightmap = []
    for i in range(len(input_lines)):
        heightmap.append([None] * len(input_lines[i]))
        for j in range(len(input_lines[i])):
            heightmap[i][j] = int(input_lines[i][j])

    print('done')


if __name__ == '__main__':
    main()
