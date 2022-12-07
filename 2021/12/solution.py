import os

all_paths = []

class Cave:
    def __init__(self, name, neighbors, is_small):
        self.name = name
        self.neighbors = neighbors
        self.is_small = is_small
    
    def __str__(self):
        return self.name
    

def read_input(filename):
    fileDir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(fileDir, filename)
    with open(filename) as f:
        input = f.read().splitlines()
    return [line.split("-") for line in input]

def get_all_caves(input):
    caves = []
    for path in input:
        for cave in path:
            if cave not in [cave.name for cave in caves]:
                caves.append(Cave(cave, [], cave[0].islower()))

    for cave in caves:
        for path in input:
            if cave.name in path:
                for neighbor in path:
                    if neighbor not in cave.neighbors and cave.name != neighbor and neighbor != "start":
                        cave.neighbors.append(neighbor)
    return caves

def get_cave_by_name(caves, name):
    return [cave for cave in caves if cave.name == name][0]

def get_all_paths(start_cave, caves, new_rules = False):
    global all_paths
    for neighbor in start_cave.neighbors:
        neighbor_cave = get_cave_by_name(caves, neighbor)
        get_path(neighbor_cave, caves, [start_cave], new_rules)
    
    return all_paths

def get_path(current_cave, caves, current_path, new_rules = False, double_visit = False):
    new_current_path = current_path[:]
    new_current_path.append(current_cave)
    if current_cave.name != "end":
        for neighbor in current_cave.neighbors:
            new_current_cave = get_cave_by_name(caves, neighbor)
            if (new_rules and not double_visit):
                if not new_current_cave.name == 'start':
                    if new_current_cave.is_small:
                        is_double = new_current_cave in current_path
                        get_path(new_current_cave, caves, new_current_path, new_rules, is_double)
                    else:          
                        get_path(new_current_cave, caves, new_current_path, new_rules)


            else: 
                if not (new_current_cave.is_small and new_current_cave in current_path):
                    get_path(new_current_cave, caves, new_current_path, new_rules, True)
    else:
        global all_paths
        print([x.name for x in new_current_path])
        all_paths.append(new_current_path)

def part_one():
    input = read_input('./input.txt')
    caves = get_all_caves(input)
    start_cave = [cave for cave in caves if cave.name == "start"][0]
    global all_paths
    all_paths = []
    all_paths = get_all_paths(start_cave, caves)
    return len(all_paths)

def part_two():
    input = read_input('./input.txt')
    caves = get_all_caves(input)
    start_cave = [cave for cave in caves if cave.name == "start"][0]
    global all_paths
    all_paths = []
    all_paths = get_all_paths(start_cave, caves, True)
    return len(all_paths)

def main():
    #print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()