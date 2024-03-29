# This is a MESS!

import re

class Group:
  def __init__(self, start, end, offset):
    self.start = start
    self.end = end
    self.offset = offset
  
  def __repr__(self):
    return f'Group(start={self.start}, end={self.end}, offset={self.offset})'


def get_group_intersections(group1, group2):
  """
  Return: A tuple where index 0 is the intersection of the 2 groups.
  Index 1 is group1 only. Index 2 is group2 only.
  """
  combined_offset = group1.offset + group2.offset

  if group1.start == group2.start and group1.end == group2.end:
    return ([Group(group1.start, group1.end, combined_offset)], [], [])

  if group1.start <= group2.start and group1.end >= group2.end:
    # Group 1 consumes group 2
    if group1.start == group2.start:
      # Starts match
      group1_chunk = Group(group2.end + 1, group1.end, group1.offset)
      combined_chunk = Group(group2.start, group2.end, combined_offset)

      return ([combined_chunk], [group1_chunk], [])
    elif group1.end == group2.end:
      # Ends match
      group1_chunk = Group(group1.start, group2.start - 1, group1.offset)
      combined_chunk = Group(group2.start, group2.end, combined_offset)

      return ([combined_chunk], [group1_chunk], [])
    else:
      # No start/end match
      group1_chunk1 = Group(group1.start, group2.start - 1, group1.offset)
      group1_chunk2 = Group(group2.end + 1, group1.end, group1.offset)
      combined_chunk = Group(group2.start, group2.end, combined_offset)
      group1_chunks = [group1_chunk1, group1_chunk2]

      return ([combined_chunk], group1_chunks, [])
  elif group2.start <= group1.start and group2.end >= group1.end:
    # Group 2 consumes group 1
    result = get_group_intersections(group2, group1)
    return (result[0], result[2], result[1])
  elif group1.start <= group2.start and group1.end <= group2.end:
    # Group 1 starts before group 2, but ends before group 2
    # Any start/end match should be caught by the previous if statement, since technically
    # one of the groups would be being consumed by the other.
    group1_chunk = Group(group1.start, group2.start - 1, group1.offset)
    group2_chunk = Group(group1.end + 1, group2.end, group2.offset)
    combined_chunk = Group(group2.start, group1.end, combined_offset)

    return ([combined_chunk], [group1_chunk], [group2_chunk])
  elif group2.start <= group1.start and group2.end <= group1.end:
    # Group 2 starts before group 1, but ends before group 1
    result = get_group_intersections(group2, group1)
    return (result[0], result[2], result[1])
  else:
    return None
  

def main():
  seeds = []
  layers = []

  with open('./input.txt') as file:
    line = file.readline()
    first = True

    while line != '':
      header_match = re.match(r'(.+)-to-(.*) map:', line)

      if first:
        first = False
        seed_tokens = line.split(':')[1].strip().split()
        min_seed = None
        max_seed = None

        for i in range(0, len(seed_tokens), 2):
          start = int(seed_tokens[i])
          length = int(seed_tokens[i+1])
          end = start + length - 1
          seeds.append(Group(start, end, 0))

          if min_seed == None or start < min_seed:
            min_seed = start
          if max_seed == None or end > max_seed:
            max_seed = end

      elif not header_match:
        layer = []

        while line.strip() != '':
          # Create a new group for this line
          current_map = [int(num) for num in line.split()]
          range_start = current_map[1]
          range_end = range_start + current_map[2] - 1
          offset = current_map[0]  - range_start
          new_group = Group(range_start, range_end, offset)
          layer.append(new_group)

          line = file.readline()

        if len(layer) > 0:
          layers.append(layer)

      line = file.readline()

  for layer in layers:
    transformed_seeds = []
    leftover_seeds = [seed for seed in seeds] 

    for group in layer:
      new_leftover_seeds = []
      added = set()

      for i in range(0, len(leftover_seeds)):
        seed = leftover_seeds[i]

        if min(group.end, seed.end) - max(group.start, seed.start) + 1 > 0:
          added.add(i)
          intersections = get_group_intersections(seed, group)
          new_leftover_seeds.extend(intersections[1])

          for item in intersections[0]:
            item.start += item.offset
            item.end += item.offset
            item.offset = 0
            transformed_seeds.append(item)
        
      for i in range(0, len(leftover_seeds)):
        if i not in added:
          new_leftover_seeds.append(leftover_seeds[i])
      leftover_seeds = new_leftover_seeds

    seeds = [seed for seed in transformed_seeds]
    seeds.extend([seed for seed in leftover_seeds])

  smallest = None

  for seed in seeds:
    if smallest == None or seed.start < smallest:
      smallest = seed.start
  
  print(smallest)


if __name__ == '__main__':
  main()

