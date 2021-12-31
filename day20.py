from utils import bit_grid, bits_to_dec, read_day

lines = read_day(20)
code = bit_grid(lines[0])
grid = [bit_grid(l) for l in lines[2:]]

def part1():
  image = grid
  for i in range(2):
    image = enhance(image, 0 if i % 2 == 0 else 1)
  return lit(image)

def lit(image):
  return sum(n for r in image for n in r)

def enhance(image, d):
  s = len(image)
  out = [[0 for _ in range(s + 2)] for _ in range(s + 2)]
  for i in range(s + 2):
    for j in range(s + 2):
      out[i][j] = extract(image, i - 1, j - 1, d)
  return out

def extract(image, x, y, d):
  bits = []
  for i in range(x - 1, x + 2):
    for j in range(y - 1, y + 2):
      bits.append(pixel(image, i, j, d))
  return code[bits_to_dec(bits)]

def pixel(image, i, j, d):
  s = len(image)
  if i < 0 or j < 0 or i >= s or j >= s:
    return d
  return image[i][j]

print(f'Part 1: {part1()}')


def part2():
  image = grid
  for i in range(50):
    image = enhance(image, 0 if i % 2 == 0 else 1)
  return lit(image)

print(f'Part 2: {part2()}')
