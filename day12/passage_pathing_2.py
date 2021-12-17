# AoC 2021 Day 12 Part 2
# Passage Pathing


def find_num_duplicates(visited_caves):
    '''
    Finds the number of duplicate lowercase elements.
    '''

    duplicates = []
    for cave in visited_caves:
        if (cave.islower()
                and visited_caves.count(cave) == 2
                and not cave in duplicates):
            duplicates.append(cave)
    return len(duplicates)


def find_num_paths(connections, current_cave='start', visited_caves=[]):
    '''
    Recursively finds the number of possible paths from the given cave to the
    end cave.
    '''

    visited_caves.append(current_cave)
    if current_cave == 'end':
        num_paths = 1
    else:
        num_paths = 0
        for cave in connections[current_cave]:
            # only allow one small cave to be visited twice
            if ((cave in visited_caves
                    and cave.islower()
                    and find_num_duplicates(visited_caves) == 1)
                    or cave == 'start'):
                continue
            num_paths += find_num_paths(connections, cave, visited_caves)
    visited_caves.pop()
    return num_paths


def main():
    # get input
    input_file = open('day12/input.txt')
    input_lines = input_file.readlines()
    input_file.close()

    # convert input into list of tuples representing cave connections
    connection_pairs = []
    for line in input_lines:
        connection_pairs.append(tuple(line.strip().split('-')))

    # convert list of tuples into dictionary
    connections = {}
    for pair in connection_pairs:
        if not pair[0] in connections.keys():
            connections[pair[0]] = []
        connections[pair[0]].append(pair[1])
        if not pair[1] in connections.keys():
            connections[pair[1]] = []
        connections[pair[1]].append(pair[0])

    print('Number of paths: ' + str(find_num_paths(connections)))


if __name__ == '__main__':
    main()
