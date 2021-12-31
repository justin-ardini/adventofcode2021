from utils import read_day
import heapq

WALL = '#'
EMPTY = '.'
SIDE_ROOMS = {3: 'A', 5: 'B', 7: 'C', 9: 'D'}
SCORE_MULTIPLIER = 10000

class Node:
  def __init__(self, pos):
    self.pos = pos
    self.allowed = []
    self.neighbors = []

  def is_room(self):
    return len(self.allowed) == 1

  def is_room_for(self, label):
    return label in self.allowed and len(self.allowed) == 1

  def __str__(self):
    return f'pos: {self.pos}, allowed: {self.allowed}'

  def __repr__(self):
    return f'Node(pos: {self.pos}, allowed: {self.allowed})'

def parse_graph(lines):
  # IMPORTANT: Assumes that all amphipods start in the wrong position. Won't work for all inputs.
  graph = {} # Position -> Node
  pods = []
  for x, row in enumerate(lines):
    for y, c in enumerate(row):
      if c == WALL:
        continue
      node = Node((x, y))
      if c != EMPTY:
        pods.append((c, x, y, False))
      if x == 1:
        node.allowed = [] if y in SIDE_ROOMS.keys() else ['A', 'B', 'C', 'D']
      else:
        node.allowed = [SIDE_ROOMS[y]]
      graph[(x, y)] = node

  for x in range(1, len(lines) - 1):
    for y in range(1, len(lines[x]) - 1):
      node = graph.get((x, y))
      if node:
        for xn, yn in neighbors(x, y):
          neighbor = graph.get((xn, yn))
          if neighbor:
            node.neighbors.append(neighbor)
  pods.sort()
  return graph, pods

def neighbors(x, y):
  return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

lines = read_day(23)
graph, init_pods = parse_graph(lines)

def part1():
  return solve(graph, init_pods)

def solve(graph, init_pods):
  num_pods = len(init_pods)
  q = []
  energies = {tuple(init_pods): 0}
  min_energy = 1000000
  iterations = 1000000
  for pod in init_pods:
    heapq.heappush(q, (0, pod, init_pods))
  while q:
    if iterations <= 0:
      return min_energy
    iterations -= 1
    _, pod, pods = heapq.heappop(q)
    energy = energies[tuple(pods)]
    for move_pods, move_energy in valid_moves(graph, pod, pods):
      tot_energy = energy + move_energy
      move_score = score_correct(graph, move_pods)
      if move_score == SCORE_MULTIPLIER * num_pods:
        min_energy = min(tot_energy, min_energy)
      tuple_pods = tuple(move_pods)
      stored_energy = energies.get(tuple_pods)
      if tuple_pods not in energies or tot_energy < stored_energy:
        energies[tuple_pods] = tot_energy
        for n in incorrect_pods(graph, move_pods):
          heapq.heappush(q, (tot_energy - move_score, n, move_pods))
  return min_energy

def incorrect_pods(graph, pods):
  return [pod for pod in pods if not pod[3]]

def valid_moves(graph, pod, pods):
  label = pod[0]
  node = graph[(pod[1], pod[2])]
  index = pods.index(pod)
  valid = []
  for move, distance in reachable(graph, node, label, pods):
    new_pods = [pods[i] if i != index else move for i in range(len(pods))]
    energy = get_energy(label, distance)
    valid.append((new_pods, energy))
  return valid

def reachable(graph, start, label, pods):
  blocked = {(p[1], p[2]): p[0] for p in pods}
  all_moves = []
  q = [(start, 0)]
  while q:
    node, distance = q.pop()
    for n in node.neighbors:
      if n.pos not in blocked.keys():
        blocked[n.pos] = label
        if label in n.allowed:
          if n.is_room():
            # Rooms below must be walls or same pod type.
            is_valid = True
            for i in range(1, 4):
              below = graph.get((n.pos[0] + i, n.pos[1]))
              if below and blocked.get(below.pos) != label:
                is_valid = False
                break
            if is_valid:
              all_moves.append(((label, *n.pos, True), distance + 1))
          elif start.is_room():
            all_moves.append(((label, *n.pos, False), distance + 1))
        q.append((n, distance + 1))
  return all_moves

def get_energy(label, distance):
  if label == 'A':
    return distance
  elif label == 'B':
    return 10 * distance
  elif label == 'C':
    return 100 * distance
  else:
    return 1000 * distance

def score_correct(graph, pods):
  return SCORE_MULTIPLIER * sum(1 if pod[3] else 0 for pod in pods)

print(f'Part 1: {part1()}')


def part2():
  lines = read_day(23)
  lines.insert(3, '###D#B#A#C###')
  lines.insert(3, '###D#C#B#A###')
  graph, pods = parse_graph(lines)
  return solve(graph, pods)

print(f'Part 2: {part2()}')
