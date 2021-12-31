from utils import read_day

PAIRS = {'(': ')', '[': ']', '{': '}', '<': '>'}
ILLEGAL_SCORES = {')': 3, ']': 57, '}': 1197, '>': 25137}
AUTOCOMPLETE_SCORES = {')': 1, ']': 2, '}': 3, '>': 4}

lines = read_day(10)

def part1():
  return sum([corrupt_score(l) for l in lines])

def corrupt_score(line):
  stack = []
  for c in line:
    if c in ['(', '[', '<', '{']:
      stack.append(PAIRS[c])
    else:
      expected = stack.pop()
      if c != expected:
        return ILLEGAL_SCORES[c]
  return 0

print(f'Part 1: {part1()}')


def part2():
  scores = sorted([autocomplete_score(l) for l in lines if corrupt_score(l) == 0])
  return scores[(len(scores) - 1) // 2]

def autocomplete_score(line):
  stack = []
  for c in line:
    if c in ['(', '[', '<', '{']:
      stack.append(PAIRS[c])
    else:
      stack.pop()
  score = 0
  while len(stack) > 0:
    c = stack.pop()
    score = score * 5 + AUTOCOMPLETE_SCORES[c]
  return score

print(f'Part 2: {part2()}')
