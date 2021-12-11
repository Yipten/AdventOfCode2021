# AoC 2021 Day 7 Part 1
# The Treachery of Whales

def calculate_fuel_cost(crab_positions, target_position):
    '''
    Calculates the fuel cost of moving all crabs to a certain position.
    '''

    fuel_cost = 0
    for i in crab_positions:
        fuel_cost += abs(target_position - i)
    return fuel_cost


def calculate_min_fuel_cost(crab_positions):
    '''
    Calculates the minimum possible fuel cost for all crabs to move to the same
    position.
    '''

    # find position boundaries
    min_position = min(crab_positions)
    max_position = max(crab_positions)
    # find minimum fuel cost
    min_fuel_cost = None
    for i in range(min_position, max_position + 1):
        fuel_cost = calculate_fuel_cost(crab_positions, i)
        if min_fuel_cost == None or fuel_cost < min_fuel_cost:
            min_fuel_cost = fuel_cost
    return min_fuel_cost


def main():
    # get input
    input_file = open('day07/input.txt')
    crab_positions_str = input_file.read()
    input_file.close()

    # convert input to list of integers
    crab_positions = []
    for i in crab_positions_str.split(','):
        crab_positions.append(int(i))

    print(calculate_min_fuel_cost(crab_positions))


if __name__ == '__main__':
    main()
