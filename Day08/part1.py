import re

def main():
  nodes = {}
  steps = ''

  with open('./input.txt') as file:
    steps = file.readline().strip()

    for line in file:
      line = line.strip()
      
      if line == '':
        continue

      matches = re.match(r'(.*)\s+=\s+[(](.*)[,]\s+(.*)[)]', line)
      node = matches.group(1)
      left = matches.group(2)
      right = matches.group(3)
      nodes[node] = (left, right)
  
  current = 'AAA'
  num_steps = 0
  i = 0

  while current != 'ZZZ':
    step = steps[i]

    if step == 'L':
      current = nodes[current][0]
    elif step == 'R':
      current = nodes[current][1]

    num_steps += 1
    i += 1

    if i >= len(steps):
      i = 0

  print(num_steps)

if __name__ == '__main__':
  main()

