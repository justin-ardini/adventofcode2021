from utils import read_day
import math

MAX_LEVEL = 4

def parse_line(line):
  stack = []
  level = 0
  if line[0] == '[':
    level = 0
    for i, c in enumerate(line[1:]):
      if c == '[':
        level += 1
      elif c == ']':
        level -= 1
      elif level == 0 and c == ',':
        return [parse_line(line[1:i+1]), parse_line(line[i+2:-1])]
  return int(line)

nums = read_day(18, parse_line)

def part1():
  n = nums[0]
  for i in range(1, len(nums)):
    n = reduce([n, nums[i]])
  return magnitude(n)

def magnitude(n):
  if isinstance(n, int):
    return n
  return 3 * magnitude(n[0]) + 2 * magnitude(n[1])

def reduce(n):
  while True:
    exploded, n = explode(n, 0)
    if exploded:
      continue
    was_split, n = split(n)
    if not was_split:
      break
  return n

def explode(n, level):
  if isinstance(n, int):
    return None, n
  if level >= MAX_LEVEL and isinstance(n[0], int) and isinstance(n[1], int):
    return n, 0
  pair, a = explode(n[0], level + 1)
  if pair:
    if pair[1]:
      return (pair[0], None), [a, add_to_side(n[1], pair[1], 0)]
    else:
      return pair, [a, n[1]]
  pair, b = explode(n[1], level + 1)
  if pair:
    if pair[0]:
      return (None, pair[1]), [add_to_side(n[0], pair[0], 1), b]
    else:
      return pair, [n[0], b]
  return None, n

def add_to_side(n, to_add, side):
  if isinstance(n, int):
    return n + to_add
  s = add_to_side(n[side], to_add, side)
  if side == 0:
    return s, n[1]
  return n[0], s

def split(n):
  if isinstance(n, int):
    if n > 9:
      return True, [math.floor(n / 2), math.ceil(n / 2)]
    else:
      return False, n
  was_split, a = split(n[0])
  if was_split:
    return (was_split, [a, n[1]])
  was_split, b = split(n[1])
  return (was_split, [n[0], b])

print(f'Part 1: {part1()}')


def part2():
  max_magnitude = 0
  for i in range(len(nums)):
    for j in range(1, len(nums)):
      a, b = nums[i], nums[j]
      max_magnitude = max(max_magnitude, magnitude(reduce([a, b])))
      max_magnitude = max(max_magnitude, magnitude(reduce([b, a])))
  return max_magnitude

print(f'Part 2: {part2()}')
