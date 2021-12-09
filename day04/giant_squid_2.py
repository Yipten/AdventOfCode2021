# AoC 2021 Day 4 Part 2
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

    for board in boards:
        for row in board:
            if number in row:
                row[number] = True


def check_horizontal_win(board):
    '''Checks for win in horizontal direction.'''

    for row in range(len(board)):
        if sum(board[row].values()) == 5:
            return True
    return False


def check_vertical_win(board):
    '''Checks for win in vertical direction.'''

    # sums of marked numbers in each column
    col_mark_sums = [0] * 5
    for row in range(len(board)):
        for i in range(len(board[row])):
            col_mark_sums[i] += list(board[row].values())[i]
    # check if any columns had all 5 numbers marked
    if 5 in col_mark_sums:
        return board
    return None


def check_wins(boards, winning_boards):
    '''Checks all boards to see if there is a winner.'''

    new_winning_boards = []
    for board in range(len(boards)):
        # don't count wins more than once
        if board in winning_boards:
            continue
        if check_horizontal_win(boards[board]) or check_vertical_win(boards[board]):
            new_winning_boards.append(board)
    return new_winning_boards


def calculate_score(boards, board_index, last_number):
    '''Calculates the score of the winning board.'''

    # calculate sum of unmarked numbers
    sum_unmarked = 0
    for row in boards[board_index]:
        for number, marked in row.items():
            if not marked:
                sum_unmarked += number
    # return sum multiplied by last number
    return sum_unmarked * last_number


def main():
    # get input
    input_file = open('day04/input.txt')
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

    winning_boards = []
    last_winning_board = None
    score = None

    # loop through each number drawn
    for n in numbers:
        mark_number(boards, n)
        for i in check_wins(boards, winning_boards):
            if i != None:
                winning_boards.append(i)
        # only one board that hasn't won yet
        if len(winning_boards) == len(boards) - 1:
            last_winning_board = int(list(set(range(len(boards))).difference(winning_boards))[0])
        elif len(winning_boards) == len(boards):
            score = calculate_score(boards, last_winning_board, n)
            break
    
    print('Score: ' + str(score))


if __name__ == '__main__':
    main()
