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

def main():
    # get input
    input_file = open('day07/input_short.txt')
    crab_positions_str = input_file.read()
    input_file.close()

    # convert input to list of integers
    crab_positions = []
    for i in crab_positions_str.split(','):
        crab_positions.append(int(i))

    print(calculate_fuel_cost(crab_positions, 2))
    print(calculate_fuel_cost(crab_positions, 1))
    print(calculate_fuel_cost(crab_positions, 3))
    print(calculate_fuel_cost(crab_positions, 10))


if __name__ == '__main__':
    main()
