from utils import read_day, str_list, Vec2d

parts = [part.split('=')[1] for part in str_list(read_day(17)[0].split(': ')[1])]
min_target = Vec2d(*(int(part.split('..')[0]) for part in parts))
max_target = Vec2d(*(int(part.split('..')[1]) for part in parts))

def part1():
  max_y = 0
  for x in range(1, 50):
    for y in range(-50, 200):
      is_hit, curr_y = hits_target(Vec2d(x, y))
      if is_hit:
        max_y = max(max_y, curr_y)
  return max_y

def hits_target(v):
  pos = Vec2d(0, 0)
  max_y = 0
  while True:
    pos, v = step(pos, v)
    max_y = max(max_y, pos.y)
    if pos.x >= min_target.x and pos.x <= max_target.x and pos.y >= min_target.y and pos.y <= max_target.y:
      return True, max_y
    if pos.x > max_target.x or pos.y < min_target.y and pos.y < 0:
      return False, max_y

def step(pos, v):
  pos += v
  if v.x > 0:
    v.x -= 1
  elif v.x < 0:
    v.x += 1
  v.y -= 1
  return pos, v

print(f'Part 1: {part1()}')


def part2():
  count = 0
  for x in range(1, 300):
    for y in range(-300, 300):
      hits, curr_max_y = hits_target(Vec2d(x, y))
      if hits:
        count += 1
  return count

print(f'Part 2: {part2()}')
