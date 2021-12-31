from utils import int_list, read_day

start_fish = read_day(6, int_list)[0]

def part1():
  fish = start_fish.copy()
  for _ in range(80):
    added = 0
    for i, f in enumerate(fish):
      if f == 0:
        fish[i] = 6
        added += 1
      else:
        fish[i] -= 1
    for j in range(added):
      fish.append(8)
  return len(fish)

print(f'Part 1: {part1()}')

def part2():
  buckets = [0 for _ in range(9)]
  for f in start_fish:
    buckets[f] += 1
  i = 0
  day = 0
  while day < 256:
    buckets[(i + 7) % 9] += buckets[i]
    i = (i + 1) % 9
    day += 1
  return sum(buckets)

print(f'Part 2: {part2()}')
