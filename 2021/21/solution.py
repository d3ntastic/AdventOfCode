import os
import copy
import functools

def read_input(filename):
    fileDir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(fileDir, filename)
    with open(filename) as f:
        input = f.read().splitlines()
    player_data = [[int(x.split(" ")[-1]), 0] for x in input]
    return player_data

def part_one():
    player_data = read_input('./input.txt')
    dice_data = [0, 0]
    current_player = 0
    i = 1
    while player_data[0][1] < 1000 and player_data[1][1] < 1000:
        for i in range(3):
            dice_data[0] += 1
            dice_data[1] += 1
            if (dice_data[1] > 100):
                dice_data[1] -= 100
            i += 1
            player_data[current_player][0] += dice_data[1]
            while (player_data[current_player][0] > 10):
                player_data[current_player][0] -= 10
        player_data[current_player][1] += player_data[current_player][0]
        current_player = (current_player + 1) % 2
    loser_player_score = player_data[current_player][1]
    return dice_data[0] * loser_player_score

@functools.cache
def play(pos1, pos2, score1=0, score2=0):
  if score2 >= 21: return 0, 1

  wins1, wins2 = 0, 0
  for move, number_of_possibilities in (3,1),(4,3),(5,6),(6,7),(7,6),(8,3),(9,1):
      pos1_ = (pos1 + move) % 10 or 10
      w2, w1 = play(pos2, pos1_, score2, score1 + pos1_)
      wins1, wins2 = wins1 + number_of_possibilities * w1, wins2 + number_of_possibilities * w2
  return wins1, wins2

def part_two():
    player_data = read_input('./input.txt')
    return max(play(player_data[0][0], player_data[1][0]))

def main():
    print(part_one())
    print(part_two())


if __name__ == "__main__":
    main()