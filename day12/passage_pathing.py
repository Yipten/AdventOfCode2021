# AoC 2021 Day 12 Part 1
# Passage Pathing

def find_num_paths(connections, current_cave='start', caves_visited=[]):
    '''
    Recursively finds the number of possible paths from the given cave to the
    end cave.
    '''

    caves_visited.append(current_cave)
    if current_cave == 'end':
        num_paths = 1
    else:
        num_paths = 0
        for cave in connections[current_cave]:
            if cave in caves_visited and cave.islower():
                continue
            num_paths += find_num_paths(connections, cave, caves_visited)
    caves_visited.pop()
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
