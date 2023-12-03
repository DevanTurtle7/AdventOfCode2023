class Coord:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def __repr__(self):
    return f'Coord ({self.x}, {self.y})'

def main():
  grid = []
  gears = []
  total = 0

  with open('./input.txt') as file:
    line_num = 0

    for line in file:
      row = []

      for i in range(0, len(line)):
        char = line[i]
        row.append(char)
        if char == '*':
          gears.append(Coord(i, line_num))

      grid.append(row)
      line_num += 1

  grid_height = len(grid)
  grid_width = len(grid[0])

  for gear in gears:
    numbers = {}

    for x in range(-1, 2):
      for y in range(-1, 2):
        if x == 0 and y == 0:
          continue
        current_x = gear.x + x
        current_y = gear.y + y
        
        if current_y >= 0 and current_y < grid_height and current_x >= 0 and current_x < grid_width - 1:
          char = grid[current_y][current_x]

          if char.isnumeric():
            start_x = current_x

            while start_x - 1 >= 0 and grid[current_y][start_x - 1].isnumeric():
              start_x -= 1

            number_str = ''
            i = start_x

            while i < grid_width and grid[current_y][i].isnumeric():
              number_str += grid[current_y][i]
              i += 1
              
            number = int(number_str)

            if start_x not in numbers:
              numbers[start_x] = {}
            
            if current_y not in numbers[start_x]:
              numbers[start_x][current_y] = number

    num_numbers = 0
    gear_ratio = 1

    for start_x in numbers:
      for y in numbers[start_x]:
        num_numbers += 1
        gear_ratio *= numbers[start_x][y]

    if num_numbers == 2:
      total += gear_ratio 

  print(total)

if __name__ == '__main__':
  main()