# AoC 2021 Day 4 Part 1
# Giant Squid

def convert_numbers(numbers_str):
    '''Converts list of strings to list of integers.'''

    numbers = []
    for i in numbers_str:
        numbers.append(int(i))
    return numbers


def convert_boards(boards_str):
    '''Converts 3D list of strings to 2D list of dictionaries.'''

    # the big list
    boards = []
    # loop through boards
    for board in range(len(boards_str)):
        boards.append([])
        # loop through rows
        for row in range(len(boards_str[board])):
            # each row is a dictionary
            boards[board].append({})
            # loop through individual values
            for i in range(len(boards_str[board][row])):
                boards[board][row][int(boards_str[board][row][i])] = False
    return boards


def mark_number(boards, number):
    '''Marks the number drawn on all boards that contain it.'''

    # loop through each board and mark the number if it's there
    for board in boards:
        for row in board:
            if number in row:
                row[number] = True


def main():
    # get input
    input_file = open('day04/input_short.txt')
    numbers_str = input_file.readline().split(',')
    # ignore blank line
    input_file.readline()
    # array to store raw board info
    boards_str = []
    # used to get one board at a time from input
    temp_board = []
    for line in input_file:
        # build a 2D list, ignoring blank lines
        if line != '\n':
            temp_board.append(line.split())
        # got all 5 rows
        if len(temp_board) == 5:
            # save board
            boards_str.append(temp_board)
            # reset for next board
            temp_board = []
    input_file.close()

    # convert raw input data into a more usable form
    numbers = convert_numbers(numbers_str)
    boards = convert_boards(boards_str)

    # loop through each number drawn
    for n in numbers:
        mark_number(boards, n)

    print(boards)


if __name__ == '__main__':
    main()
