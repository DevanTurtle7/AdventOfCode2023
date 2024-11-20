class Number:
  def __init__(self, number, x, y):
    self.number = number
    self.x = x
    self.y = y
  
  def __repr__(self):
    return f'Number ({self.number}, ({self.x}, {self.y}))'

def main():
  grid = []
  numbers = []
  total = 0

  with open('./input.txt') as file:
    line_num = 0

    for line in file:
      current_num = ''
      num_start = None
      row = []

      for i in range(0, len(line)):
        char = line[i]
        row.append(char)

        if char.isnumeric():
          int(char)
          current_num += char

          if num_start == None:
            num_start = i

        if not char.isnumeric() or i == len(line) - 1:
          if current_num != '' and num_start != None:
            numbers.append(Number(int(current_num), num_start, line_num))
            current_num = ''

          num_start = None

      grid.append(row)
      line_num += 1
  
  grid_height = len(grid)
  grid_width = len(grid[0])

  for number_obj in numbers:
    number = number_obj.number
    number_str = str(number)
    row = number_obj.y
    col = number_obj.x
    done = False

    for i in range(0, len(number_str)):
      check = [(1, 0), (-1, 0)]

      if done:
        break

      if i == 0:
        check.extend([(1, -1), (0, -1), (-1, -1)])

      if i == len(number_str) - 1:
        check.extend([(1, 1), (0, 1), (-1, 1)])

      for coords in check:
        current_row = row + coords[0]
        current_col = col + coords[1] + i

        if current_row >= 0 and current_row < grid_height and current_col >= 0 and current_col < grid_width - 1:
          current_char = grid[current_row][current_col]

          if current_char != '.' and not current_char.isnumeric():
            total += number
            done = True
            break;
  
  print(total)


if __name__ == '__main__':
  main()
