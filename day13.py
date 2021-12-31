from utils import int_list, read_day

def parse_fold(line):
  parts = line.split(' ')[2].split('=')
  return parts[0], int(parts[1])

lines = read_day(13)
dots = set(tuple(int_list(l)) for l in lines[:lines.index('')])
folds = [parse_fold(l) for l in lines[lines.index('') + 1:]]

def part1():
  new_dots = dots
  new_dots = do_fold(folds[0], new_dots)
  return len(new_dots)

def do_fold(fold, dots):
  f = fold[1]
  new_dots = set()
  if fold[0] == 'x':
    for x, y in dots:
      if x < f:
        new_dots.add((f - x - 1, y))
      elif x > f:
        new_dots.add((x - f - 1, y))
  else:
    for x, y in dots:
      if y < f:
        new_dots.add((x, f - y - 1))
      elif y > f:
        new_dots.add((x, y - f - 1))
  return new_dots

print(f'Part 1: {part1()}')


def part2():
  new_dots = dots
  for fold in folds:
    new_dots = do_fold(fold, new_dots)
  draw(new_dots)

def draw(paper):
  l = [['.' for _ in range(40)] for _ in range(40)]
  for x, y in paper:
    l[39 - y][39 - x] = '#'
  print('\n'.join(''.join(x) for x in l))

print(f'Part 2: {part2()}')
