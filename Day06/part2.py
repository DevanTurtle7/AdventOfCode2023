
def main():
  time = 0
  distance = 0

  with open('./input.txt') as file:
    first = True

    for line in file:
      nums = line.split(':')[1]
      number_str = ''.join(nums.strip().split())
      num = int(number_str)

      if first:
        time = num
        first = False
      else:
        distance = num
    
    count = 0

    for hold_time in range(1, time - 1):
      time_remaining = time - hold_time
      traveled = time_remaining * hold_time

      if traveled > distance:
        count += 1

  print(count)


if __name__ == '__main__':
  main()

