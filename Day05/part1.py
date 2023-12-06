import re

def main():
  seeds = []

  with open('./input.txt') as file:
    line = file.readline()
    first = True

    while line != '':
      header_match = re.match(r'(.+)-to-(.*) map:', line)

      if first:
        first = False
        seeds = [int(num) for num in line.split(':')[1].strip().split()]
      elif not header_match:
        new_seeds = [seed for seed in seeds]

        while line.strip() != '':
          current_map = [int(num) for num in line.split()]
          range_start = current_map[1]
          range_end = range_start + current_map[2] - 1
          offset = current_map[0] - range_start

          for i in range(0, len(seeds)):
            seed = seeds[i]

            if seed >= range_start and seed <= range_end:
              new_seeds[i] = seed + offset

          line = file.readline()

        seeds = new_seeds
        
      line = file.readline()
  
  print(min(seeds))

if __name__ == '__main__':
  main()

