# AoC 2021 Day 6 Part 1
# Lanternfish

def create_new_fish(fish_timers):
    '''
    Creates new fish to add to the population.

    One fish is create for each existing fish with a timer at 0. Each new fish
    will initially have their timer set to 8.
    '''

    num_new_fish = fish_timers.count(0)
    fish_timers.extend([8] * num_new_fish)

def decrement_fish_timers(fish_timers, decrement_limit):
    '''
    Decrements all fish timers by 1, rolling over from 0 to 6.
    '''

    for i in range(decrement_limit):
        if fish_timers[i] > 0:
            fish_timers[i] -= 1
        else:
            fish_timers[i] = 6

def main():
    # get input
    input_file = open('day06/input.txt')
    fish_timers_str = input_file.read()
    input_file.close()

    # convert list of strings to list of integers
    fish_timers = []
    for i in fish_timers_str.split(','):
        fish_timers.append(int(i))

    # number of days to simulate
    num_days = 80

    # loop through the days
    for i in range(num_days):
        decrement_limit = len(fish_timers)
        create_new_fish(fish_timers)
        decrement_fish_timers(fish_timers, decrement_limit)

    print('Number of lanternfish: ' + str(len(fish_timers)))


if __name__ == '__main__':
    main()
