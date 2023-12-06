import re

def str_to_nums(string):
  return [int(num) for num in string.strip().split()]

def main():
  num_cards = 0
  matches = {}
  counts = {}

  with open ('./input.txt') as file:
    for line in file:
      num_cards += 1

      card_tokens = line.split(':')
      card_number = int(re.match(r'Card\s+(\d+)', card_tokens[0]).group(1))
      tokens = card_tokens[1].split('|')
      winning_numbers = set(str_to_nums(tokens[0]))
      my_numbers = str_to_nums(tokens[1])
      value = 0

      for number in my_numbers:
        if number in winning_numbers:
          value += 1

      matches[card_number] = value
  
  for i in range(1, num_cards + 1):
    counts[i] = 1
  
  for match in matches:
    for _ in range(0, counts[match]):
      for i in range(match + 1, match + matches[match] + 1):
        counts[i] += 1
  
  total_num_cards = 0

  for card_num in counts:
    total_num_cards += counts[card_num]

  print(total_num_cards)

if __name__ == '__main__':
  main()

