from utils import read_day, str_list
from collections import Counter

lines = read_day(14)
polymer = lines[0]
rules = dict(str_list(l, ' -> ') for l in lines[2:])

def part1():
  out = polymer
  for i in range(10):
    out = step(out)
  c = Counter(out)
  return max(c.values()) - min(c.values())

def step(poly):
  out = ''
  for i in range(len(poly) - 1):
    pair = poly[i] + poly[i + 1]
    out += poly[i] + rules.get(pair, '')
  out += poly[-1]
  return out

print(f'Part 1: {part1()}')


def part2():
  pair_counts = Counter()
  for i in range(len(polymer) - 1):
    pair = polymer[i] + polymer[i + 1]
    pair_counts[pair] += 1

  for i in range(40):
    pair_counts = step2(pair_counts)

  letter_counts = Counter({polymer[0]: 1})
  for pair, count in pair_counts.items():
    letter_counts[pair[1]] += count
  return max(letter_counts.values()) - min(letter_counts.values())

def step2(pair_counts):
  new_counts = Counter()
  for pair, count in pair_counts.items():
    i = rules[pair]
    new_counts[pair[0] + i] += count
    new_counts[i + pair[1]] += count
  return new_counts

print(f'Part 2: {part2()}')
