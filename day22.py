from utils import clamp, prod, read_day, str_list

def get_splits(start, end, point):
  sx, sy, sz = start
  ex, ey, ez = end
  px, py, pz = point
  return [
    ((sx, sy, sz), (px, py, pz)),
    ((sx, sy, pz), (px, py, ez)),
    ((sx, py, sz), (px, ey, pz)),
    ((sx, py, pz), (px, ey, ez)),
    ((px, sy, sz), (ex, py, pz)),
    ((px, sy, pz), (ex, py, ez)),
    ((px, py, sz), (ex, ey, pz)),
    ((px, py, pz), (ex, ey, ez))]

class Cuboid:
  def __init__(self, on, start, end):
    self.on = on
    self.start = start
    self.end = end
    self.children = []

  def toggle(self, cuboid):
    if self.children:
      for child in self.children:
        child.toggle(cuboid)
    elif self.on != cuboid.on:
      overlap = self.clamped(cuboid)
      if not overlap.size():
        return
      if self.start == overlap.start and self.end == overlap.end:
        self.on = overlap.on
      elif self.start == overlap.start:
        self.split(overlap.end)
        self.children[0].on = overlap.on
      else:
        self.split(overlap.start)
        if self.end == overlap.end:
          self.children[-1].on = overlap.on
        else:
          self.children[-1].toggle(overlap)

  def clamped(self, cuboid):
    start = tuple(clamp(a, b, c) for a, b, c in zip(self.start, cuboid.start, cuboid.end))
    end = tuple(clamp(a, b, c) for a, b, c in zip(self.end, cuboid.start, cuboid.end))
    return Cuboid(cuboid.on, start, end)

  def split(self, split_point):
    assert(not self.children)
    for start, end in get_splits(self.start, self.end, split_point):
       cuboid = Cuboid(self.on, start, end)
       if cuboid.size():
         self.children.append(cuboid)

  def size(self):
    return prod(b - a for a, b in zip(self.start, self.end))

  def size_on(self):
    '''Returns positive for on, negative for off.'''
    if self.children:
      return sum(c.size_on() for c in self.children)
    return self.on * self.size()


def parse_line(line):
  """Output tuple: (0|1, (xmin, ymin, zmin), (xmax, ymax, zmax))"""
  cmd, s = line.split(' ', 1)
  parts = [l.split('=')[1] for l in str_list(s)]
  start = tuple(int(p.split('..')[0]) for p in parts)
  end = tuple(int(p.split('..')[1]) + 1 for p in parts)
  return Cuboid(cmd == 'on', start, end)

cuboids = read_day(22, parse_line)


def part1():
  s = 50
  region = Cuboid(False, (-s, -s, -s), (s+1, s+1, s+1))
  for cuboid in cuboids:
    region.toggle(cuboid)
  return region.size_on()

print(f'Part 1: {part1()}')


def part2():
  s = 100000
  region = Cuboid(False, (-s, -s, -s), (s+1, s+1, s+1))
  for cuboid in cuboids:
    region.toggle(cuboid)
  return region.size_on()

print(f'Part 2: {part2()}')
