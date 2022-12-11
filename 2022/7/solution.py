import os

class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.files = []

    def add_file(self, file):
        self.files.append(file)
    
    def get_size(self):
        size = 0
        for file in self.files:
            size += file
        for child in self.children:
            size += child.get_size()
        return size

    def add_child(self, child):
        self.children.append(child)

    def get_parent(self):
        return self.parent

    def get_children(self):
        return self.children

    def get_name(self):
        return self.name

    def get_path(self):
        path = self.name
        parent = self.parent
        while parent is not None:
            path = parent.get_name() + '/' + path
            parent = parent.get_parent()
        return path

    def __str__(self):
        return self.get_path()

def get_directory_tree(input):
    directory_tree = Directory('/', None)
    current_directory = directory_tree
    list_of_dirs = []
    for line in input:
        if (line == '$ cd /'):
            current_directory = directory_tree
        elif (line == '$ cd ..'):
            current_directory = current_directory.get_parent()
        elif (line.startswith('$ cd')):
            name = line.split(' ')[2]
            for child in current_directory.get_children():
                if (child.get_name() == name):
                    current_directory = child
                    break
        elif (line.startswith('$ ls')):
            continue
        elif (line.startswith('dir')):
            name = line.split(' ')[1]
            list_of_dirs.append(name)
            directory = Directory(name, current_directory)
            current_directory.add_child(directory)
        else:
            file = int(line.split(' ')[0])
            current_directory.add_file(file)
    return directory_tree, list_of_dirs

def read_input(filename):
    fileDir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(fileDir, filename)
    with open(filename) as f:
        input = f.read().splitlines()      
    return get_directory_tree(input)

def get_all_sizes_recursive(directory):
    sizes = {}
    for child in directory.get_children():
        size = child.get_size()
        sizes[child.get_name() + '-' + str(size)] = size
        sizes.update(get_all_sizes_recursive(child))
    return sizes

def part_one():
    input, list_of_dirs = read_input('./input.txt')
    directory_sizes = get_all_sizes_recursive(input)
    return sum([element for element in directory_sizes.values() if element <= 100000])

def part_two():
    input, list_of_dirs = read_input('./input.txt')
    directory_sizes = get_all_sizes_recursive(input)
    current_input_size = input.get_size()
    current_free_space = 70000000 - current_input_size
    needed_space = 30000000 - current_free_space
    closest_result = 3000000
    closest_dir = ''
    sizes = list(directory_sizes.values())
    sizes.sort()
    for current_size in sizes:
        if (current_size > needed_space):
            return current_size
    return closest_dir

def main():
    print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()
