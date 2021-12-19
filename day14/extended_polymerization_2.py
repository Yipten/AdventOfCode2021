# AoC 2021 Day 14 Part 2
# Extended Polymerization

def insert_elements(element_pairs, insertion_rules):
    '''
    Inserts elements between pairs as described in the insertion rules.
    '''

    # make copy of dictionary
    element_pairs_copy = element_pairs.copy()
    # loop through every pair in the polymer
    for pair in element_pairs_copy.keys():
        if pair in insertion_rules.keys():
            # new pair ending with inserted element
            new_pair_0 = pair[0] + insertion_rules[pair]
            if not new_pair_0 in element_pairs.keys():
                element_pairs[new_pair_0] = 0
            element_pairs[new_pair_0] += element_pairs_copy[pair]
            # new pair starting with inserted element
            new_pair_1 = insertion_rules[pair] + pair[1]
            if not new_pair_1 in element_pairs.keys():
                element_pairs[new_pair_1] = 0
            element_pairs[new_pair_1] += element_pairs_copy[pair]
            # previously existing pair is destroyed
            element_pairs[pair] -= element_pairs_copy[pair]


def convert_pairs_to_elements(element_pairs, polymer):
    '''
    Converts dictionary representing element pairs into one representing
    individual elements.
    '''

    elements = {}
    # count first element of each pair
    for pair, count in element_pairs.items():
        if not pair[0] in elements.keys():
            elements[pair[0]] = 0
        elements[pair[0]] += count
    # count last element of last pair
    last_element = polymer[-1]
    if not last_element in elements.keys():
        elements[last_element] = 0
    elements[last_element] += 1
    return elements


def main():
    # get input
    with open('day14/input.txt') as input_file:
        input_lines = input_file.readlines()

    # remove whitespace
    for i in range(len(input_lines)):
        input_lines[i] = input_lines[i].strip()

    # make dictionary to store the number of each element pair
    polymer = list(input_lines[0])
    element_pairs = {}
    for i in range(len(polymer) - 1):
        pair = '{0}{1}'.format(polymer[i], polymer[i + 1])
        if not pair in element_pairs.keys():
            element_pairs[pair] = 0
        element_pairs[pair] += 1

    insertion_rules = {}
    for line in [i for i in input_lines if '->' in i]:
        split_line = line.split(' -> ')
        insertion_rules[split_line[0]] = split_line[1]

    for i in range(40):
        insert_elements(element_pairs, insertion_rules)

    elements = convert_pairs_to_elements(element_pairs, polymer)

    diff_max_min = max(elements.values()) - min(elements.values())

    print('Difference: {0}'.format(diff_max_min))


if __name__ == '__main__':
    main()
