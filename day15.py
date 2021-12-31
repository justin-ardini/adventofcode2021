from utils import int_grid, read_day
import heapq

grid = read_day(15, int_grid)
size = len(grid)

def part1():
  graph = {}
  for x in range(size):
    for y in range(size):
      graph[(x, y)] = grid[x][y]
  start, end = (0, 0), (size - 1, size - 1)
  return a_star(graph, start, end)

def a_star(graph, start, end):
  q = []
  costs = {start: 0}
  heapq.heappush(q, (start, distance(start, end)))
  while q:
    pos = heapq.heappop(q)[0]
    cost = costs[pos]
    if pos == end:
      return cost
    x, y = pos
    for n in neighbors(*pos, end[0]):
      old_n_cost = costs.get(n)
      new_n_cost = cost + graph.get(n, 0)
      if n not in costs or new_n_cost < old_n_cost:
        costs[n] = new_n_cost
        heapq.heappush(q, (n, new_n_cost + distance(n, end)))

def neighbors(x, y, limit):
  return (n for n in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)) if all(v >= 0 and v <= limit for v in n))

def distance(a, b):
  return sum(abs(x - y) for x, y in zip(a, b))


print(f'Part 1: {part1()}')


def part2():
  graph = {}
  for n in range(5):
    for m in range(5):
      for i in range(size):
        for j in range(size):
          v = grid[i][j] + n + m
          if v > 9:
            v -= 9
          graph[(size * n + i, size * m + j)] = v
  start, end = (0, 0), (5 * size - 1, 5 * size - 1)
  return a_star(graph, start, end)

print(f'Part 2: {part2()}')
