from utils import read_day

MODEL_SIZE = 14
CHUNK_SIZE = 18

def parse_line(line):
  parts = line.split()
  cmd = parts[0]
  a = parts[1]
  if cmd in ('add', 'mul', 'div', 'mod', 'eql'):
    b = parts[2]
    try:
      b = int(b)
    except:
      pass
  else:
    b = None
  return cmd, a, b

def get_chunks(cmds):
  chunks = []
  for i in range(MODEL_SIZE):
    chunk = cmds[4 + CHUNK_SIZE * i:CHUNK_SIZE * (i + 1)]
    a = chunk[0][2]
    b = chunk[1][2]
    c = chunk[11][2]
    chunks.append((a, b, c))
  return chunks

cmds = read_day(24, parse_line)
chunks = get_chunks(cmds)

def part1():
  return solve_max(chunks)

def is_valid(digits, chunks):
  stack = []
  for n, chunk in zip(digits, chunks):
    if chunk[0] == 1:
      stack.append(n + chunk[2])
    else:
      p = stack.pop()
      if n != p + chunk[1]:
        return False
  return True

def solve_max(chunks):
  solution = [0 for _ in range(len(chunks))]
  stack = []
  for i, chunk in enumerate(chunks):
    if chunk[0] == 1:
      stack.append((i, chunk[2]))
    else:
      j, p = stack.pop()
      diff = p + chunk[1]
      if diff > 0:
        solution[i] = 9
        solution[j] = 9 - diff
      else:
        solution[j] = 9
        solution[i] = 9 + diff
  return sum(n * 10**(len(solution) - 1 - i) for i, n in enumerate(solution))

print(f'Part 1: {part1()}')


def part2():
  return solve_min(chunks)

def solve_min(chunks):
  solution = [0 for _ in range(len(chunks))]
  stack = []
  for i, chunk in enumerate(chunks):
    if chunk[0] == 1:
      stack.append((i, chunk[2]))
    else:
      j, p = stack.pop()
      diff = p + chunk[1]
      if diff > 0:
        solution[i] = 1 + diff
        solution[j] = 1
      else:
        solution[j] = 1 - diff
        solution[i] = 1
  return sum(n * 10**(len(solution) - 1 - i) for i, n in enumerate(solution))

print(f'Part 2: {part2()}')
