from utils import int_grid, read_day
import queue

heights = read_day(9, int_grid)
size = len(heights)

def part1():
  total = 0
  for i, row in enumerate(heights):
    for j, height in enumerate(row):
      risk = height + 1
      for i2, j2 in neighbors(i, j, size):
        if height >= heights[i2][j2]:
          risk = 0
      total += risk
  return total

def neighbors(x, y, limit):
  return (n for n in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)) if all(v >= 0 and v < limit for v in n))

print(f'Part 1: {part1()}')

def part2():
  low_points = []
  for i, row in enumerate(heights):
    for j, height in enumerate(row):
      is_low = True
      for i2, j2 in neighbors(i, j, size):
        if height >= heights[i2][j2]:
          is_low = False
      if is_low:
        low_points.append((i, j))
  sizes = []
  for point in low_points:
    sizes.append(basin_size(heights, point))
  sizes = sorted(sizes, reverse=True)
  return sizes[0] * sizes[1] * sizes[2]

def basin_size(heights, start):
  visited = [start]
  q = queue.Queue()
  q.put(start)
  total = 0
  while not q.empty():
    i, j = q.get()
    total += 1
    for n in neighbors(i, j, size):
      if n not in visited and heights[n[0]][n[1]] < 9:
        visited.append(n)
        q.put(n)
  return total

print(f'Part 2: {part2()}')
