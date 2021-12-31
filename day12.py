from utils import read_day
import queue

def parse_line(line):
  return line.split('-')

pairs = read_day(12, parse_line)
graph = {}
for a, b in pairs:
  graph.setdefault(a, []).append(b)
  graph.setdefault(b, []).append(a)

def part1():
  return bfs(graph, 'start')

def bfs(graph, start):
  q = queue.Queue()
  q.put((start, [start]))
  paths = 0
  while not q.empty():
    curr, visited = q.get()
    if curr == 'end':
      paths += 1
      continue
    for n in graph[curr]:
      if n not in visited:
        v = [x for x in visited]
        if not is_big(n):
          v.append(n)
        q.put((n, v))

  return paths

def is_big(cave):
  return cave.isupper()

print(f'Part 1: {part1()}')


def part2():
  return bfs2(graph, 'start')

def bfs2(graph, start):
  q = queue.Queue()
  q.put((start, [start], True))
  paths = 0
  while not q.empty():
    curr, visited, can_visit = q.get()
    if curr == 'end':
      paths += 1
      continue
    for n in graph[curr]:
      if n not in visited:
        v = [x for x in visited]
        if not is_big(n):
          v.append(n)
        q.put((n, v, can_visit))
      elif n not in ('start', 'end') and can_visit:
        q.put((n, visited, False))

  return paths

print(f'Part 2: {part2()}')
