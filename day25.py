from utils import char_grid, read_day

EMPTY = '.'
EAST = '>'
SOUTH = 'v'

grid = read_day(25, char_grid)

def part1():
  curr_grid = grid
  i = 0
  while True:
    next_grid = step(curr_grid)
    i += 1
    if curr_grid == next_grid:
      return i
    curr_grid = next_grid

def step(grid):
  next_grid = []
  # East
  for row in grid:
    next_row = []
    for j, c in enumerate(row):
      w = row[(j - 1) % len(row)]
      e = row[(j + 1) % len(row)]
      if c == EMPTY and w == EAST:
        next_row.append(w)
      elif c == EAST and e == EMPTY:
        next_row.append(e)
      else:
        next_row.append(c)
    next_grid.append(next_row)
  # South
  out = []
  for i, row in enumerate(next_grid):
    out_row = []
    for j, c in enumerate(row):
      n = next_grid[(i - 1) % len(next_grid)][j]
      s = next_grid[(i + 1) % len(next_grid)][j]
      if c == EMPTY and n == SOUTH:
        out_row.append(n)
      elif c == SOUTH and s == EMPTY:
        out_row.append(s)
      else:
        out_row.append(c)
    out.append(out_row)
  return out

print(f'Part 1: {part1()}')
