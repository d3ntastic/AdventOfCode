import os

pickScores = {
    "A": 1, # Rock
    "B": 2, # Paper
    "C": 3, # Scissors
    "X": 1, # Rock
    "Y": 2, # Paper
    "Z": 3 # Scissors
}

resultScores = {
    "X": 0, # Loss
    "Y": 3, # Draw
    "Z": 6 # Win
}

results = {}

def read_input(filename):
    fileDir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(fileDir, filename)
    with open(filename) as f:
        lines = [line.split(" ") for line in f.read().splitlines()]
    return lines

def get_score_part_one(round):
    opponent = round[0]
    you = round[1]
    opponentPickScore = pickScores[opponent]
    pickScore = pickScores[you]
    resultScore = 0
    if (pickScore == opponentPickScore):
        resultScore = 3
    elif ((pickScore == (opponentPickScore + 1)) or (pickScore == 1 and opponentPickScore == 3)):
        resultScore = 6
    return pickScore + resultScore

def get_score_part_two(round):
    opponent = round[0]
    result = round[1]
    opponentPickScore = pickScores[opponent]
    resultScore = resultScores[result]
    pickScore = -1
    
    if (result == "Y"):
        return resultScore + opponentPickScore
    elif (result == "Z"):
        if (opponent == "A"):
            return resultScore + 2
        if (opponent == "B"):
            return resultScore + 3
        return resultScore + 1    
    elif (result == "X"):
        if (opponent == "A"):
            return resultScore + 3
        if (opponent == "B"):
            return resultScore + 1
        return resultScore + 2
        

def part_one():
    input = read_input('./input.txt')
    roundResults = [get_score_part_one(round) for round in input]
    result = sum(roundResults)
    return result

def part_two():
    input = read_input('./input.txt')
    roundResults = [get_score_part_two(round) for round in input]
    result = sum(roundResults)
    return result

def main():
    print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()