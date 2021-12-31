from collections import Counter
from utils import bit_grid, bits_to_dec, read_day

lines = read_day(3, lambda x: bit_grid(x, '1'))

def part1():
  gamma = []
  epsilon = []
  counts = Counter()
  for line in lines:
    for i, n in enumerate(line):
      counts[(i, n)] += 1
  for i in range(len(lines[0])):
    if counts[(i, 0)] > counts[(i, 1)]:
      gamma.append(0)
      epsilon.append(1)
    else:
      gamma.append(1)
      epsilon.append(0)
  return bits_to_dec(gamma) * bits_to_dec(epsilon)

print(f'Part 1: {part1()}')


def part2():
  o2 = get_o2([l.copy() for l in lines])
  co2 = get_co2([l.copy() for l in lines])
  return bits_to_dec(o2) * bits_to_dec(co2)

def get_o2(nums):
  for i in range(len(nums[0])):
    counts = [0, 0]
    for num in nums:
      counts[num[i]] += 1
    if counts[0] > counts[1]:
      v = 0
    else:
      v = 1
    nums = [n for n in nums if n[i] == v]
    if len(nums) == 1:
      return nums[0]
  raise RuntimeError('No O2 rating found')

def get_co2(nums):
  for i in range(len(nums[0])):
    counts = [0, 0]
    for num in nums:
      counts[num[i]] += 1
    if counts[0] > counts[1]:
      v = 1
    else:
      v = 0
    nums = [n for n in nums if n[i] == v]
    if len(nums) == 1:
      return nums[0]
  raise RuntimeError('No CO2 rating found')

print(f'Part 2: {part2()}')
