from utils import bits_to_dec, int_list, read_day

def parse_boards(lines):
  boards = []
  i = 0
  while i < len(lines):
    board = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    for j in range(SIZE):
      board[j] = [int(x) for x in lines[i + j].split() if x != '']
    boards.append(board)
    i += SIZE + 1  # includes blank line
  return boards

SIZE = 5
MARK = -1
lines = read_day(4)
nums = int_list(lines[0])
boards = parse_boards(lines[2:])

def mark_number(n, boards):
  for board in boards:
    for i, row in enumerate(board):
      for j, x in enumerate(row):
        if x == n:
          board[i][j] = MARK

def check_bingo(board):
  for i in range(SIZE):
    bingo = True
    for j in range(SIZE):
      if board[i][j] != MARK:
        bingo = False
    if bingo:
      return True
  for i in range(SIZE):
    bingo = True
    for j in range(SIZE):
      if board[j][i] != MARK:
        bingo = False
    if bingo:
      return True
  return False

def score(board):
  return sum(sum(x for x in r if x != MARK) for r in board)

def part1():
  for n in nums:
    mark_number(n, boards)
    for board in boards:
      if check_bingo(board):
        return n * score(board)
  return -1

print(f'Part 1: {part1()}')

def part2():
  for n in nums:
    mark_number(n, boards)
    for board in boards:
      if check_bingo(board):
        if len(boards) == 1:
          return n * score(board)
        else:
          boards.remove(board)
  return -1

print(f'Part 2: {part2()}')
