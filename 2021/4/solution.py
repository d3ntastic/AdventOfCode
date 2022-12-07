def read_input(filename):
    input = open(filename, "r").read().split("\n\n")
    numbers = input[0].split(",")
    boards_split = [board.split("\n") for board in input[1:]]
    boards = [[row.lstrip().replace("  ", " ").split(" ") for row in board] for board in boards_split]
    return numbers, boards

def check_row(row):
    for element in row:
        if element == 0:
            return False
    return True

def check_board(board):
    for row in board:
        if (check_row(row)):
            return True
    for i in range(len(board[0])):
        is_incomplete = False
        for row in board:
            if row[i] == 0:
                is_incomplete = True
        if not is_incomplete:
            return True
    return False

def calculate_checksum(board, marked_board, current_number):
    checksum = 0
    for row_id, row in enumerate(board):
        for element_id, element in enumerate(row):
            if marked_board[row_id][element_id] == 0:
                checksum += int(element)
    return checksum * int(current_number)

def part_one():
    numbers, boards = read_input('input.txt')
    marked_numbers = [[[0 for element in row] for row in board] for board in boards]
    for number in numbers:
        for board_id, board in enumerate(boards):
            for row_id, row in enumerate(board):
                for element_id, element in enumerate(row):
                    if element == number:
                        marked_numbers[board_id][row_id][element_id] = 1
                        if check_board(marked_numbers[board_id]):
                            return calculate_checksum(board, marked_numbers[board_id], number)

def part_two():
    numbers, boards = read_input('input.txt')
    solved_boards = []
    marked_numbers = [[[0 for element in row] for row in board] for board in boards]
    for number in numbers:
        for board_id, board in enumerate(boards):
            for row_id, row in enumerate(board):
                for element_id, element in enumerate(row):
                    if element == number:
                        marked_numbers[board_id][row_id][element_id] = 1
                        if check_board(marked_numbers[board_id]) and board_id not in solved_boards:
                            solved_boards.append(board_id)
                            if (len(solved_boards) == len(boards)):
                                return calculate_checksum(board, marked_numbers[board_id], number)

def main():
    print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()