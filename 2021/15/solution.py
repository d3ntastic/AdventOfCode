import os

class Node:
    def __init__(self, row, col, risk):
        self.row = row
        self.col = col
        self.risk = risk

class Grid:
    def __init__(self, data):
        self._data = data
        self._height = len(data)
        self._width = len(data[0])

    def __getitem__(self, pos):
        row, col = pos
        return self._data[row][col]

    def neighbors(self, node):
        neighbors = []
        row, col = node.row, node.col
        if row > 0:
            neighbors.append(self._data[row - 1][col])
        if row < self._height - 1:
            neighbors.append(self._data[row + 1][col])
        if col > 0:
            neighbors.append(self._data[row][col - 1])
        if col < self._width - 1:
            neighbors.append(self._data[row][col + 1])
        return neighbors

    def min_cost(self, start: Node, end: Node) -> int:
        cost = [[float("inf") for _ in range(self._width)] for _ in range(self._height)]
        cost[start.row][start.col] = 0

        queue = [start]
        while queue:
            current = queue.pop(0)
            for neighbor in self.neighbors(current):
                neighbor_cost = cost[neighbor.row][neighbor.col]
                cost_to_neighbor = cost[current.row][current.col] + neighbor.risk
                if neighbor_cost > cost_to_neighbor:
                    cost[neighbor.row][neighbor.col] = cost_to_neighbor
                    queue.append(neighbor)

        return cost[end.row][end.col]

def read_input(filename):
    fileDir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(fileDir, filename)
    with open(filename) as f:
        map = f.read().splitlines()
    return [[int(x) for x in lines] for lines in map]

def format_input(input):
    return '\n'.join([''.join(map(str, line)) for line in input])

def part_one():
    map = read_input('./input.txt')
    grid_data = [
        [Node(row, col, int(weight)) for col, weight in enumerate(row_data)]
        for row, row_data in enumerate(map)
    ]
    grid = Grid(grid_data)
    return grid.min_cost(grid[0, 0], grid[-1, -1])

def part_two():
    base_map = read_input('./input.txt')
    new_map = [[0 for _ in range(len(base_map[0]) * 5)] for _ in range(len(base_map) * 5)]
    for i in range(5):
        for row_id, row in enumerate(base_map):
            for col_id, col in enumerate(base_map[row_id]):
                new_map[row_id][col_id + i * len(base_map[row_id])] = (col + i) % 9 if col + i > 9 else col + i
    for i in range(5):
        for row_id, row in enumerate(base_map):
            for col_id, col in enumerate(new_map[row_id]):
                new_map[row_id + i * len(base_map[row_id])][col_id] = (col + i) % 9 if col + i > 9 else col + i
    grid_data = [
        [Node(row, col, int(weight)) for col, weight in enumerate(row_data)]
        for row, row_data in enumerate(new_map)
    ]
    grid = Grid(grid_data)
    return grid.min_cost(grid[0, 0], grid[-1, -1])

def main():
    print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()