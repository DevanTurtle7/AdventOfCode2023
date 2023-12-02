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
      game_id = int(re.match(r'Game (\d+)', tokens[0]).group(1))
      handfuls = tokens[1].split(';')
      valid = True

      for handful in handfuls:
        cubes = handful.split(',')
        current_total = 0

        for cube in cubes:
          match = re.match(r'(\d+) (.+)', cube.strip())
          num = int(match.group(1))
          color = match.group(2)
          current_total += num

          if num > constraint[color]:
            valid = False

        if current_total > total_constraint:
          valid = False
        
        if not valid:
          break

      if valid:
        total += game_id
        
    print(total)

if __name__ == '__main__':
  main()