import re

class Trip:
  def __init__(self, current_node):
    self.current_node = current_node
    self.loop_size = None
    self.counter = 0
  
  def take_step(self, new_node):
    self.current_node = new_node
    self.counter += 1

    if new_node[-1] == 'Z':
      self.loop_size = self.counter
      self.counter = 0
  
  def __repr__(self):
    return f'Trip(current_node={self.current_node}, loop_size={self.loop_size}, counter={self.counter})'


def lcm(a, b):
  x = a
  y = b

  while x != y:
    if x > y:
      y += b
    else:
      x += a
  
  return x


def main():
  nodes = {}
  steps = ''

  with open('./input.txt') as file:
    steps = file.readline().strip()

    for line in file:
      line = line.strip()
      
      if line == '':
        continue

      matches = re.match(r'(.*)\s+=\s+[(](.*)[,]\s+(.*)[)]', line)
      node = matches.group(1)
      left = matches.group(2)
      right = matches.group(3)
      nodes[node] = (left, right)
  
  trips = []
  trips_complete = False
  i = 0

  for node in nodes:
    if node[-1] == 'A':
      trips.append(Trip(node))

  while not trips_complete:
    step = steps[i]

    for trip in trips:
      if trip.loop_size != None:
        continue
       
      paths = nodes[trip.current_node]
      new_node = ''

      if step == 'L':
        new_node = paths[0]
      elif step == 'R':
        new_node = paths[1]
      
      trip.take_step(new_node)

    trips_complete = True

    for trip in trips:
      if trip.loop_size == None:
        trips_complete = False
        break

    i = (i + 1) % len(steps)

  result = 0

  for i in range(1, len(trips)):
    if i == 1:
      result = lcm(trips[i].loop_size, trips[i - 1].loop_size)
    else:
      result = lcm(trips[i].loop_size, result)
  
  print(result)


if __name__ == '__main__':
  main()

