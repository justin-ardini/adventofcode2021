from utils import read_day
import math

def parse_line(line):
  return int(line.split(': ')[1])

lines = read_day(21, parse_line)
p1_start = lines[0] - 1
p2_start = lines[1] - 1

def part1():
  pos = [p1_start, p2_start]
  scores = [0, 0]
  player = 1
  rolls = 0
  die = 0
  while True:
    player = 1 if player == 0 else 0
    s = 0
    for _ in range(3):
      s += die + 1
      die = (die + 1) % 100
    rolls += 3
    pos[player] = (pos[player] + s) % 10
    scores[player] += pos[player] + 1
    if scores[player] >= 1000:
      break
  return rolls * scores[1 if player == 0 else 0]

print(f'Part 1: {part1()}')

totals = [0, 0]

def part2():
  play((p1_start, p2_start), (0, 0), 0, 3, 1)
  play((p1_start, p2_start), (0, 0), 0, 4, 3)
  play((p1_start, p2_start), (0, 0), 0, 5, 6)
  play((p1_start, p2_start), (0, 0), 0, 6, 7)
  play((p1_start, p2_start), (0, 0), 0, 7, 6)
  play((p1_start, p2_start), (0, 0), 0, 8, 3)
  play((p1_start, p2_start), (0, 0), 0, 9, 1)
  return max(totals)

def play(pos, scores, player, roll, mult):
  n_pos = (pos[player] + roll) % 10
  score = scores[player] + n_pos + 1
  if score >= 21:
    totals[player] += mult
    return
  pos2 = (n_pos, pos[1]) if player == 0 else (pos[0], n_pos)
  scores2 = (score, scores[1]) if player == 0 else (scores[0], score)
  p = 1 if player == 0 else 0
  play(pos2, scores2, p, 3, mult)
  play(pos2, scores2, p, 4, 3 * mult)
  play(pos2, scores2, p, 5, 6 * mult)
  play(pos2, scores2, p, 6, 7 * mult)
  play(pos2, scores2, p, 7, 6 * mult)
  play(pos2, scores2, p, 8, 3 * mult)
  play(pos2, scores2, p, 9, mult)

print(f'Part 2: {part2()}')
