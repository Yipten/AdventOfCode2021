# AoC 2021 Day 6 Part 2
# Lanternfish

def create_new_fish(fish_timer_values):
    '''
    Creates new fish to add to the population.

    One fish is create for each existing fish with a timer at 0. Each new fish
    will initially have their timer set to 8. Returns the number of fish added.
    '''

    num_new_fish = fish_timer_values[0]
    # fish_timers.extend([8] * num_new_fish)
    fish_timer_values[8] += num_new_fish
    return num_new_fish

def decrement_fish_timers(fish_timer_values, num_new_fish):
    '''
    Decrements fish timers.

    All timers are decremented by 1, rolling over from 0 to 6, with the
    exception of the most recently created fish.
    '''

    # remember number of fish timers at 0
    num_timers_at_zero = fish_timer_values[0]
    # decrement each fish timer from 1 to 6
    for i in range(len(fish_timer_values) - 2):
        fish_timer_values[i] = fish_timer_values[i + 1]
    # roll over timers from 0 to 6
    fish_timer_values[6] += num_timers_at_zero
    # only decrement timers from 8 to 7 if they've been around for a day
    fish_timer_values[7] = fish_timer_values[8] - num_new_fish
    fish_timer_values[8] -= fish_timer_values[7]
    

def main():
    # get input
    input_file = open('day06/input.txt')
    fish_timers_str = input_file.read()
    input_file.close()

    # record number of fish with each timer value (9 total from 0 to 8)
    fish_timer_values = [0] * 9
    for i in fish_timers_str.split(','):
        fish_timer_values[int(i)] += 1

    # number of days to simulate
    num_days = 256

    # loop through the days
    for i in range(num_days):
        num_new_fish = create_new_fish(fish_timer_values)
        decrement_fish_timers(fish_timer_values, num_new_fish)

    print('Number of lanternfish: ' + str(sum(fish_timer_values)))


if __name__ == '__main__':
    main()
