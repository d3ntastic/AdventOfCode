import os

depth = 2

energy = {
    "A": 1,
    "B": 10,
    "C": 100,
    "D": 1000
}

destinations = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

class State:
    def __init__(self, state, cost, moves):
        self.state = state
        self.cost = cost
        self.moves = moves

    def move(self, a, b):
        if not self.move_is_valid(a, b):
            print("Attempted an invalid move!")
            exit(1)

        amphipod_type = self.state[a]
        move_cost = self.move_cost(a, b)

        new_state = self.state.copy()
        del new_state[a]
        new_state[b] = amphipod_type

        new_moves = self.moves.copy()
        new_moves.append((a, b))

        return State(new_state, self.cost + move_cost, new_moves)

    def lower_bound_cost(self):
        lower_bound = self.cost
        for pos in self.state:
            amphipod_type = self.state[pos]
            target_room = destinations[amphipod_type]

            if pos[0] == target_room:
                continue

            lower_bound += self.move_cost(pos, (target_room, 1))

        return lower_bound

    def move_cost(self, a, b):
        steps = a[1] + abs(a[0] - b[0]) + b[1]
        amphipod_type = self.state[a]

        return energy[amphipod_type] * steps

    def move_is_valid(self, a, b) -> bool:
        if a not in self.state:
            return False
        if b in self.state:
            return False
        if b[0] in [2, 4, 6, 8] and b[1] == 0:
            return False

        left = min(a[0], b[0])
        right = max(a[0], b[0])
        for i in range(left, right + 1):
            if (i, 0) == a or (i, 0) == b:
                continue

            if (i, 0) in self.state:
                return False

        return True

    def is_complete(self):
        if len(self.state) != depth * 4:
            print("Invalid state!")
            exit(1)

        for amphipod_type in ["A", "B", "C", "D"]:
            if not self.room_is_complete(amphipod_type):
                return False

        return True

    def enumerate_legal_moves(self):
        moves: list[tuple[tuple[int, int]]] = []
        for pos in self.state:
            amphipod_type = self.state[pos]
            target_room = destinations[amphipod_type]

            if pos[1] == 0:
                free_height = self.room_is_free_to_move(amphipod_type)
                if free_height is None:
                    continue
                elif self.hall_free_between(pos[0], target_room):
                    moves.append((pos, (target_room, free_height)))

            else:
                if self.is_blocked_in_room(pos):
                    continue

                if self.room_is_complete(amphipod_type):
                    continue

                if pos[0] == target_room:
                    bottom = True
                    for i in range(pos[1], depth + 1):
                        if (pos[0], i) not in self.state:
                            print("It's halfway up its room? This should never happen!")
                            exit()

                        if self.state[(pos[0], i)] != amphipod_type:
                            bottom = False
                            break
                    if bottom:
                        continue

                hall_min, hall_max = self.hall_free_min_max_around(pos[0])

                free_height = self.room_is_free_to_move(amphipod_type)

                if free_height is not None and target_room in range(hall_min, hall_max + 1) and pos[0] in range(
                        hall_min,
                        hall_max + 1
                ):
                    moves.append((pos, (target_room, free_height)))
                    continue

                for i in range(hall_min, hall_max + 1):
                    if i in [2, 4, 6, 8]:
                        continue

                    moves.append((pos, (i, 0)))

        return moves

    def is_blocked_in_room(self, a):
        for i in range(1, a[1]):
            if (a[0], i) in self.state:
                return True

        return False

    def hall_free_min_max_around(self, pivot):
        hallway_positions = [-1, 11]
        for pos in self.state:
            if pos[1] == 0:
                hallway_positions.append(pos[0])

        hallway_positions.sort()

        for i in range(len(hallway_positions) - 1):
            if hallway_positions[i] < pivot < hallway_positions[i + 1]:
                return hallway_positions[i] + 1, hallway_positions[i + 1] - 1

        print("Messed up hallway")
        exit(1)

    def hall_free_between(self, a: int, b: int) -> bool:
        for i in range(min(a, b) + 1, max(a, b)):
            if (i, 0) in self.state:
                return False

        return True

    def room_is_complete(self, amphipod_type):
        amphipod_room = destinations[amphipod_type]

        for i in range(1, depth + 1):
            if (amphipod_room, i) not in self.state:
                return False
            if self.state[(amphipod_room, i)] != amphipod_type:
                return False

        return True

    def room_is_free_to_move(self, amphipod_type):
        destination_room = destinations[amphipod_type]

        for i in range(depth, 0, -1):
            if (destination_room, i) not in self.state:
                return i

            if self.state[(destination_room, i)] != amphipod_type:
                return None

        return None

    def print(self):
        height = 0
        for pos in self.state:
            height = max(height, pos[1])

        arr = [["#" for _ in range(13)] for _ in range(height + 3)]
        for i in range(1, 12):
            arr[1][i] = "."

        for i in [3, 5, 7, 9]:
            for j in [2, 3]:
                arr[j][i] = "."

        for pos in self.state:
            arr[pos[1] + 1][pos[0] + 1] = self.state[pos]

        print("\n".join(["".join(row) for row in arr]))


def iterate_moves(state: State):
    global best_cost

    if state.is_complete():
        best_cost = state.cost
        print("best cost", best_cost)
        return

    potential_moves = state.enumerate_legal_moves()
    for move_from, move_to in potential_moves:
        new_state = state.move(move_from, move_to)

        if new_state.cost < best_cost and new_state.lower_bound_cost() < best_cost:
            iterate_moves(new_state)

def read_input(filename, part1 = True):
    fileDir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(fileDir, filename)
    with open(filename) as f:
        map = f.read().splitlines()
    if part1:
        starting_state_config = {
            (2, 1): map[2][3],
            (2, 2): map[3][3],
            (4, 1): map[2][5],
            (4, 2): map[3][5],
            (6, 1): map[2][7],
            (6, 2): map[3][7],
            (8, 1): map[2][9],
            (8, 2): map[3][9],
        }
    else:
        starting_state_config = {
            (2, 1): map[2][3],
            (2, 2): "D",
            (2, 3): "D",
            (2, 4): map[3][3],
            (4, 1): map[2][5],
            (4, 2): "C",
            (4, 3): "B",
            (4, 4): map[3][5],
            (6, 1): map[2][7],
            (6, 2): "B",
            (6, 3): "A",
            (6, 4): map[3][7],
            (8, 1): map[2][9],
            (8, 2): "A",
            (8, 3): "C",
            (8, 4): map[3][9],
        }
    return starting_state_config

def part_one():
    starting_state_config = read_input("input.txt")
    global depth
    global best_cost
    depth = 2
    best_cost = 9999999999
    starting_state = State(state=starting_state_config, cost=0, moves=[])
    iterate_moves(state=starting_state)
    return best_cost

def part_two():
    starting_state_config = read_input("input.txt", part1=False)
    global depth
    global best_cost
    depth = 4
    best_cost = 9999999999
    starting_state = State(state=starting_state_config, cost=0, moves=[])
    iterate_moves(state=starting_state)
    return best_cost


def main():
    print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()