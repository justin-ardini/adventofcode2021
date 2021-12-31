from utils import read_day

nums = read_day(1, int)

def part1():
  count = 0
  prev = 999999
  for n in nums:
    if n > prev:
      count += 1
    prev = n
  return count

print(f'Part 1: {part1()}')

def part2():
  count = 0
  triple = [0, 0, 0]
  prev = 999999
  i = 0
  triples = []
  for n in nums:
    triple[i] = n
    if all(x != 0 for x in triple):
      s = sum(triple)
      if s > prev:
        count += 1
      prev = s
    i = (i + 1) % 3
  return count

print(f'Part 2: {part2()}')
