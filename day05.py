from collections import Counter
from utils import read_day, vec_pair

SIZE = 1000

def parse_endpoints(line):
  parts = line.split(' -> ')
  return vec_pair(parts[0]), vec_pair(parts[1])

lines = read_day(5, parse_endpoints)

def part1():
  counts = Counter()
  for start, end in lines:
    x_min, x_max = min(start.x, end.x), max(start.x, end.x)
    y_min, y_max = min(start.y, end.y), max(start.y, end.y)
    if x_min == x_max:
      for y in range(y_min, y_max + 1):
        counts[(x_min, y)] += 1
    elif y_min == y_max:
      for x in range(x_min, x_max + 1):
        counts[(x, y_min)] += 1
  return count_overlap(counts)

def count_overlap(counts):
  return sum(1 if c >= 2 else 0 for c in counts.values())

print(f'Part 1: {part1()}')

def part2():
  counts = Counter()
  for start, end in lines:
    x_step = 1 if start.x < end.x else -1 if start.x > end.x else 0
    y_step = 1 if start.y < end.y else -1 if start.y > end.y else 0
    if x_step == 0:
      # Vertical
      for y in range(start.y, end.y + y_step, y_step):
        counts[(start.x, y)] += 1
    else:
      # Horizontal and diagonal
      y = start.y
      for x in range(start.x, end.x + x_step, x_step):
        counts[(x, y)] += 1
        y += y_step
  return count_overlap(counts)

print(f'Part 2: {part2()}')
