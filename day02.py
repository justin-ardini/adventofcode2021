from utils import prod, read_day

def parse_cmd(s):
  parts = s.split()
  return parts[0], int(parts[1])

commands = read_day(2, parse_cmd)

def part1():
  pos = [0, 0]
  for cmd, n in commands:
    if cmd == 'down':
      pos[1] += n
    elif cmd == 'up':
      pos[1] -= n
    elif cmd == 'forward':
      pos[0] += n
    else:
      raise Exception(f'invalid command: {cmd}')
  return prod(pos)

print(f'Part 1: {part1()}')

def part2():
  pos = [0, 0]
  aim = 0
  for cmd, n in commands:
    if cmd == 'down':
      aim += n
    elif cmd == 'up':
      aim -= n
    elif cmd == 'forward':
      pos[0] += n
      pos[1] += n * aim
    else:
      raise Exception(f'invalid command: {cmd}')
  return prod(pos)

print(f'Part 2: {part2()}')
