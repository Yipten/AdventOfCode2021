# AoC 2021 Day 14 Part 1
# Extended Polymerization

def insert_elements(polymer, insertion_rules):
    '''
    Inserts elements between pairs as described in the insertion rules.
    '''

    # loop through polymer in reverse to insert elements
    for i in range(len(polymer))[:0:-1]:
        pair = '{0}{1}'.format(polymer[i - 1], polymer[i])
        if pair in insertion_rules.keys():
            polymer.insert(i, insertion_rules[pair])


def find_element_counts(polymer):
    '''
    Returns a set containing the number of each element.
    '''

    unique_elements = set(polymer)
    element_counts = set()
    for element in unique_elements:
        element_counts.add(polymer.count(element))
    return element_counts


def main():
    # get input
    with open('day14/input.txt') as input_file:
        input_lines = input_file.readlines()

    # remove whitespace
    for i in range(len(input_lines)):
        input_lines[i] = input_lines[i].strip()

    polymer = list(input_lines[0])

    insertion_rules = {}
    for line in [i for i in input_lines if '->' in i]:
        split_line = line.split(' -> ')
        insertion_rules[split_line[0]] = split_line[1]

    for i in range(10):
        insert_elements(polymer, insertion_rules)

    element_counts = find_element_counts(polymer)

    diff_max_min = max(element_counts) - min(element_counts)

    print('Difference: {0}'.format(diff_max_min))


if __name__ == '__main__':
    main()
