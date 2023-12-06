def str_to_nums(string):
  return [int(num) for num in string.strip().split()]

def main():
  total = 0

  with open ('./input.txt') as file:
    for line in file:
      numbers = line.split(':')[1]
      tokens = numbers.split('|')
      winning_numbers = set(str_to_nums(tokens[0]))
      my_numbers = str_to_nums(tokens[1])
      value = 0

      for number in my_numbers:
        if number in winning_numbers:
          if value == 0:
            value = 1
          else:
            value = value << 1 
      
      total += value

  print(total)

if __name__ == '__main__':
  main()

