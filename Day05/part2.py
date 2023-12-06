import re

class Group:
  def __init__(self, start, end, offset):
    self.start = start
    self.end = end
    self.offset = offset
  
  def __repr__(self):
    return f'Group(start={self.start}, end={self.end}, offset={self.offset})'


def is_in_range(num, start, end):
  return num >= start and num <= end


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
  groups = []

  with open('./input.txt') as file:
    line = file.readline()
    first = True

    # TODO: Starting array needs rewritten. Will probably need to ue ranges like Group
    # Will probably need to check them after we define the groups

    while line != '':
      header_match = re.match(r'(.+)-to-(.*) map:', line)

      if first:
        first = False
        seed_tokens = line.split(':')[1].strip().split()

        for i in range(0, len(seed_tokens), 2):
          start = int(seed_tokens[i])
          length = int(seed_tokens[i+1])
          seeds.extend([num for num in range(start, start+length)])
      elif not header_match:
        while line.strip() != '':
          # Create a new group for this line
          current_map = [int(num) for num in line.split()]
          range_start = current_map[1]
          range_end = range_start + current_map[2] - 1
          offset = current_map[0]  - range_start
          new_group = Group(range_start, range_end, offset)

          # Create a list and put new_group into it. This group will likely get chopped up
          new_group_chunks = [new_group]
          to_remove = []
          to_add = []

          # Iterate over groups
          for group in groups:
            new_chunks = [chunk for chunk in new_group_chunks]
            print('new chunks:')
            print(new_chunks)

            for new_group_chunk in new_group_chunks:
              # Find all overlaps (we can assume that there are no overlaps within groups)
              if min(range_end, group.end) - max(range_start, group.start) + 1 > 0:
                # Subtract the two groups from each other
                sub_groups = get_group_intersections(group, new_group_chunk)
                intersection = sub_groups[0]
                group1_chunks = sub_groups[1]
                group2_chunks = sub_groups[2]
                print('overlap')
                print(group, new_group_chunk)
                print(sub_groups)
                print()

                # Replace the current group with the INTERSECTION
                # If the current group has a chopped section where there is no intersction, add that back too
                to_remove.append(group)
                to_add.extend(intersection)
                to_add.extend(group1_chunks)

                # Put the scraps of the new_group into the new_group list and continue
                new_chunks.remove(new_group_chunk)
                new_chunks.extend(group2_chunks)

            new_group_chunks = new_chunks
          
          for group in to_remove:
            groups.remove(group)

          groups.extend(to_add)
          groups.extend(new_group_chunks)
          to_remove = []
          to_add = []

          line = file.readline()
        
      line = file.readline()
  
  #print(min(seeds))
  print('Groups:')
  for group in groups:
    print(group)

if __name__ == '__main__':
  main()

