from utils import prod, read_day

line = read_day(16)[0]
packet_hex = int(line, 16)
packet_bin = format(packet_hex, 'b').zfill(len(line) * 4)

def part1():
  return version_sum(packet_bin, 0)[0]

def version_sum(packet, p):
  version = int(packet[p:p+3], 2)
  type_id = int(packet[p+3:p+6], 2)
  p += 6
  if type_id == 4:
    n = ''
    while packet[p] == '1':
      n += packet[p+1:p+5]
      p += 5
    n += packet[p+1:p+5]
    value = int(n, 2)
    return version, p+5
  else:
    length_id = int(packet[p], 2)
    if length_id == 0:
      size = int(packet[p+1:p+16], 2)
      p += 16
      end = p+size
      while p < end:
        v, p = version_sum(packet, p)
        version += v
      return version, p
    else:
      num_packets = int(packet[p+1:p+12], 2)
      p += 12
      for _ in range(num_packets):
        v, p = version_sum(packet, p)
        version += v
      return version, p

print(f'Part 1: {part1()}')


def part2():
  return eval_packet(packet_bin, 0)[0]

def eval_packet(packet, p):
  version = int(packet[p:p+3], 2)
  type_id = int(packet[p+3:p+6], 2)
  p += 6
  if type_id == 4:
    return eval_literal(packet, p)

  values, p = eval_subpackets(packet, p)
  if type_id == 0:
    return sum(values), p
  if type_id == 1:
    return prod(values), p
  if type_id == 2:
    return min(values), p
  if type_id == 3:
    return max(values), p
  if type_id == 5:
    return 1 if values[0] > values[1] else 0, p
  if type_id == 6:
    return 1 if values[0] < values[1] else 0, p
  if type_id == 7:
    return 1 if values[0] == values[1] else 0, p

def eval_subpackets(packet, p):
  length_id = int(packet[p], 2)
  values = []
  if length_id == 0:
    size = int(packet[p+1:p+16], 2)
    p += 16
    end = p+size
    while p < end:
      v, p = eval_packet(packet, p)
      values.append(v)
  else:
    num_packets = int(packet[p+1:p+12], 2)
    p += 12
    for _ in range(num_packets):
      v, p = eval_packet(packet, p)
      values.append(v)
  return values, p

def eval_literal(packet, p):
  n = ''
  while packet[p] == '1':
    n += packet[p+1:p+5]
    p += 5
  n += packet[p+1:p+5]
  return int(n, 2), p+5

print(f'Part 2: {part2()}')
