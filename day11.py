from utils import int_grid, read_day

start_octos = read_day(11, int_grid)
size = len(start_octos)

def part1():
  octos = [r.copy() for r in start_octos]
  count = 0
  for i in range(100):
    for i, row in enumerate(octos):
      for j, octo in enumerate(row):
        octos[i][j] += 1
    count += flash(octos)
  return count

def flash(octos):
  flashed = set()
  while True:
    found = False
    for i, row in enumerate(octos):
      for j, octo in enumerate(row):
        o = octos[i][j]
        if (i, j) not in flashed and o > 9:
          found = True
          flashed.add((i, j))
          for i2, j2 in neighbors(i, j, size):
            octos[i2][j2] += 1
    if not found:
      break
  for i, j in flashed:
    octos[i][j] = 0
  return len(flashed)

def neighbors(x, y, limit):
  out = []
  for xn in range(max(0, x - 1), min(limit, x + 2)):
    for yn in range(max(0, y - 1), min(limit, y + 2)):
      if xn == x and yn == y:
        continue
      out.append((xn, yn))
  return out

print(f'Part 1: {part1()}')


def part2():
  octos = [r.copy() for r in start_octos]
  for step in range(1000000):
    for i, row in enumerate(octos):
      for j, octo in enumerate(row):
        octos[i][j] += 1
    if flash(octos) == 100:
      return step + 1
  return None

print(f'Part 2: {part2()}')
