from utils import read_day

def get_beacons(lines):
  scanners = []
  beacons = []
  for line in lines:
    if line == '':
      scanners.append(beacons)
      beacons = []
    elif not line.startswith('--'):
      beacons.append(parse_line(line))
  scanners.append(beacons)
  return scanners

def parse_line(line):
  return tuple(int(n) for n in line.split(','))

scanners = get_beacons(read_day(19))

def find_aligned_scanner(oriented_scanners, scanner_rotations):
  for base_points in oriented_scanners:
    for i, rotations in enumerate(scanner_rotations):
      new_points, offset = align_scanner(base_points, rotations)
      if new_points:
        return new_points, offset, i
  return None, -1

def get_rotations(points):
  '''Returns 24 rotations of the given points.'''
  rotations = [all_rotations(p) for p in points]
  return [set(r[i] for r in rotations) for i in range(len(rotations[0]))]

def all_rotations(point):
  x, y, z = point
  return [
      (x, y, z),
      (z, y, -x),
      (-x, y, -z),
      (-z, y, x),
      (-x, -y, z),
      (-z, -y, -x),
      (x, -y, -z),
      (z, -y, x),
      (x, -z, y),
      (y, -z, -x),
      (-x, -z, -y),
      (-y, -z, x),
      (x, z, -y),
      (-y, z, -x),
      (-x, z, y),
      (y, z, x),
      (z, x, y),
      (y, x, -z),
      (-z, x, -y),
      (-y, x, z),
      (-z, -x, y),
      (y, -x, z),
      (z, -x, -y),
      (-y, -x, -z)]

def align_scanner(base_points, rotations):
  '''Returns aligned points or None if not possible.'''
  for points in rotations:
    for point_a in base_points:
      for point_b in points:
        offset = sub(point_a, point_b)
        aligned_points = set(add(offset, p) for p in points)
        if len(base_points & aligned_points) >= 12:
          return aligned_points, offset
  return None, None

def add(a, b):
  return a[0] + b[0], a[1] + b[1], a[2] + b[2]

def sub(a, b):
  return a[0] - b[0], a[1] - b[1], a[2] - b[2]

def unique_points(all_points):
  return len(set(p for points in all_points for p in points))

def distance(a, b):
  return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])

def max_distance(scanners):
  m = 0
  for a in scanners:
    for b in scanners:
      m = max(distance(a, b), m)
  return m

def parts_1_and_2():
  '''Slow, no cache solution to both parts.'''
  scanner_rotations = [get_rotations(s) for s in scanners[1:]]
  oriented_scanners = [set(scanners[0])]
  offsets = [(0, 0, 0)]
  while len(oriented_scanners) < len(scanners):
    print(f'Oriented scanners: {len(oriented_scanners)}')
    points, offset, i = find_aligned_scanner(oriented_scanners, scanner_rotations)
    if points:
      oriented_scanners.insert(0, points)
      offsets.insert(0, offset)
      del scanner_rotations[i]
    else:
      raise RuntimeError('Failed to align all scanners')

  count = unique_points(oriented_scanners)
  print(f'Part 1: {count}')

  distance = max_distance(offsets)
  print(f'Part 2: {distance}')

parts_1_and_2()
