import re

def main():
  total = 0

  with open('./input.txt') as file:
    for line in file:
      matches = re.findall(r'(\d)', line)
      num_str = f'{matches[0]}{matches[-1]}'
      total += int(num_str)
  
  print(total)


if __name__ == '__main__':
  main()