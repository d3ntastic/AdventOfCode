import os
import math

def read_input(filename):
    fileDir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(fileDir, filename)
    with open(filename) as f:
        input = f.read().splitlines()      
    return input

def part_one():
    input = read_input('./input.txt')
    visible_count = 0
    for rowid, row in enumerate(input):
        for colid, col in enumerate(row):
            col = int(col)
            if (colid == 0 or rowid == 0 or colid == len(row) - 1 or rowid == len(row) - 1):
                visible_count += 1
                continue
            result = [True, True, True, True] # left, right, top, bottom
            for i in range(0, len(row)):
                if (i < colid): #left
                    if (int(input[rowid][i]) >= col):
                        result[0] = False
                if (i > colid): #right
                    if (int(input[rowid][i]) >= col):
                        result[1] = False
                if (i < rowid): #top
                    if (int(input[i][colid]) >= col):
                        result[2] = False
                if (i > rowid): #bottom
                    if (int(input[i][colid]) >= col):
                        result[3] = False     
            if (any(result)):
                visible_count += 1
    return visible_count

def part_two():
    input = read_input('./input.txt')
    results = {}
    for rowid, row in enumerate(input):
        for colid, col in enumerate(row):
            col = int(col)
            result = [0, 0, 0, 0] # left, right, top, bottom
            done = [False, False, False, False]
            for i in range(0, len(row)):
                if (i < colid): #left
                    if (int(input[rowid][i]) >= col):
                        result[0] = abs(colid - i)
                if (i > colid): #right
                    if (int(input[rowid][i]) >= col and not done[1]):
                        result[1] = abs(colid - i)
                        done[1] = True
                if (i < rowid): #top
                    if (int(input[i][colid]) >= col):
                        result[2] = abs(rowid - i)
                if (i > rowid): #bottom
                    if (int(input[i][colid]) >= col and not done[3]):
                        result[3] = abs(rowid - i)
                        done[3] = True 
                        
            for resultid, resultval in enumerate(result):
                if (resultval == 0):
                    if (resultid == 0):
                        result[resultid] = colid
                    if (resultid == 1):
                        result[resultid] = len(row) - 1 - colid
                    if (resultid == 2):
                        result[resultid] = rowid
                    if (resultid == 3):
                        result[resultid] = len(row) - 1 - rowid
            results[str(rowid) + '-' + str(colid)] = math.prod(result)
            
    return max(results.values())

def main():
    print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()
