
def main():
  data = []

  with open('./input.txt') as file:
    for line in file:
      nums = line.split(':')[1]
      data.append([int(num) for num in nums.strip().split()])

    total = 1
    
    for i in range(0, len(data[0])):
      time = data[0][i]
      distance = data[1][i]
      count = 0

      for hold_time in range(1, time - 1):
        time_remaining = time - hold_time
        traveled = time_remaining * hold_time

        if traveled > distance:
          count += 1

      total *= count
  
  print(total)


if __name__ == '__main__':
  main()

