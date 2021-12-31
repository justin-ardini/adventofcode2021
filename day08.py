from utils import read_day

def parse_line(line):
  parts = line.split(' | ')
  return tuple([''.join(sorted(s)) for s in part.split(' ')] for part in parts)

lines = read_day(8, parse_line)

def part1():
  count = 0
  for _, outputs in lines:
    for output in outputs:
      if len(output) in [2, 4, 3, 7]:
        count += 1
  return count

print(f'Part 1: {part1()}')

def part2():
  total = 0
  for inputs, outputs in lines:
    total += solve(inputs, outputs)
  return total

# Solves for a single 4-digit code.
def solve(inputs, outputs):
  l_to_n = {}
  remaining = inputs.copy()

  # Start easy: 1, 4, 7, 8
  for i in inputs:
    if len(i) in [2, 4, 3, 7]:
      remaining.remove(i)
      if len(i) == 2:
        l_to_n[i] = 1
      elif len(i) == 4:
        l_to_n[i] = 4
      elif len(i) == 3:
        l_to_n[i] = 7
      elif len(i) == 7:
        l_to_n[i] = 8

  # Use overlaps to solve 9 and 6.
  n_to_l = {v: k for k, v in l_to_n.items()}
  for i in inputs:
    if len(i) == 6:
      if all(c in i for c in n_to_l[4]):
        l_to_n[i] = 9
        remaining.remove(i)
      elif any(c not in i for c in n_to_l[1]):
        l_to_n[i] = 6
        remaining.remove(i)

  # 0 is the only remaining 6 length.
  for i in remaining:
    if len(i) == 6:
      l_to_n[i] = 0
      remaining.remove(i)

  # Use overlaps to solve 3 and 5.
  n_to_l = {v: k for k, v in l_to_n.items()}
  for i in inputs:
    if len(i) == 5:
      if all(c in i for c in n_to_l[7]):
        l_to_n[i] = 3
        remaining.remove(i)
      elif all(c in n_to_l[6] for c in i):
        l_to_n[i] = 5
        remaining.remove(i)

  # Only 2 remains.
  for i in remaining:
    l_to_n[i] = 2

  total = 0
  m = 1000
  for o in outputs:
    total += l_to_n[o] * m;
    m = m // 10
  return total

print(f'Part 2: {part2()}')
