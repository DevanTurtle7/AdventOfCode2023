import re

def main():
  total = 0
  constraint = {
    'red': 12,
    'green': 13,
    'blue': 14
  }
  total_constraint = 0

  for key in constraint:
    total_constraint += constraint[key]

  with open('./input.txt') as file:
    for line in file:
      tokens = line.strip().split(':')
      handfuls = tokens[1].split(';')
      current = {}

      for handful in handfuls:
        cubes = handful.split(',')

        for cube in cubes:
          match = re.match(r'(\d+) (.+)', cube.strip())
          num = int(match.group(1))
          color = match.group(2)

          if color not in current or current[color] < num:
            current[color] = num

      current_total = 1
      for color in current:
        current_total *= current[color]
      total += current_total
      
    print(total)

if __name__ == '__main__':
  main()