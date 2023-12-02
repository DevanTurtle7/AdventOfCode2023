import re

tokens = {
  'one': 1,
  'two': 2,
  'three': 3,
  'four': 4,
  'five': 5,
  'six': 6,
  'seven': 7,
  'eight': 8,
  'nine': 9
}

def main():
  total = 0
  regex = '(?=(\d'

  for token in tokens:
    regex += f'|{token}'
  regex += '))'

  with open('./input.txt') as file:
    for line in file:
      match_iter = re.finditer(regex, line)
      matches = [match.group(1) for match in match_iter]
      num_str = ''

      for i in range(0, -2, -1):
        match = matches[i]
        if match in tokens:
          num_str += str(tokens[match])
        else:
          num_str += match
      
      total += int(num_str)
  
  print(total)


if __name__ == '__main__':
  main()