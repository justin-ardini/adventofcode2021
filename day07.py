import math
from utils import int_list, read_day

positions = read_day(7, int_list)[0]

def part1():
  min_fuel = math.inf
  for pos in positions:
    fuel = sum(abs(pos2 - pos) for pos2 in positions)
    min_fuel = min(fuel, min_fuel)
  return min_fuel

print(f'Part 1: {part1()}')

def part2():
  min_fuel = math.inf
  for pos in positions:
    fuel = 0
    for pos2 in positions:
      steps = abs(pos2 - pos)
      fuel += steps * (steps + 1) // 2
    min_fuel = min(fuel, min_fuel)
  return min_fuel

print(f'Part 2: {part2()}')
