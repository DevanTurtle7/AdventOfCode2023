
class Node:
    def __init__(self, symbol, x, y):
        self.neighbors = set()
        self.symbol = symbol
        self.x = x
        self.y = y
        self.connections = []

        if self.symbol == '|':
            self.connections.append((0, 1))
            self.connections.append((0, -1))
        elif self.symbol == '-':
            self.connections.append((1, 0))
            self.connections.append((-1, 0))
        elif self.symbol == 'L':
            # NE
            self.connections.append((1, 0))
            self.connections.append((0, -1))
        elif self.symbol == 'J':
            # NW
            self.connections.append((0, -1))
            self.connections.append((-1, 0))
        elif self.symbol == '7':
            # SW
            self.connections.append((0, 1))
            self.connections.append((-1, 0))
        elif self.symbol == 'F':
            # SE
            self.connections.append((1, 0))
            self.connections.append((0, 1))

    def add_neighbor(self, neighbor):
        self.neighbors.add(neighbor)

    def is_compatible(self, other):
        if other.symbol == "S":
            return True

        for connection in self.connections:
            x, y = connection
            inverse_connection = (x * -1, y * -1)

            if inverse_connection in other.connections:
                if other.x == self.x + x and other.y == self.y + y:
                    return True

        return False

    def __hash__(self):
        return hash(f'{self.x},{self.y}')
    
    def __repr__(self):
        neighbor_coords = [f'({node.x}, {node.y})' for node in self.neighbors]
        return f'Node ({self.x}, {self.y}), neighbors: {neighbor_coords}'

def main():
    with open('./input.txt') as file:
        line_num = 0
        rows = []
        start_node = None

        # Create unconnected nodes
        for line in file:
            line = line.strip()
            row = []

            for char_num in range(0, len(line)):
                char = line[char_num]
                row.append(Node(char, char_num, line_num))
            
            rows.append(row)
            line_num += 1

        # Connect nodes
        num_rows = len(rows)

        for y in range(0, num_rows):
            row = rows[y]
            num_nodes = len(row)

            for x in range(0, num_nodes):
                node = row[x]

                if node.symbol == 'S':
                    start_node = node

                for connection in node.connections:
                    dir_x, dir_y = connection
                    neighbor_x = x + dir_x
                    neighbor_y = y + dir_y

                    if neighbor_x < 0 or neighbor_x >= num_nodes \
                    or neighbor_y < 0 or neighbor_y >= num_rows:
                        continue

                    neighbor = rows[neighbor_y][neighbor_x]

                    if not node.is_compatible(neighbor):
                        continue

                    node.neighbors.add(neighbor)
                    neighbor.neighbors.add(node)

        # BFS
        visited = set()
        queue = [start_node]
        distances = {start_node: 0}
        max_distance = 0

        while len(queue) > 0:
            current = queue.pop(0)

            for neighbor in current.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    distances[neighbor] = distances[current] + 1

                    if distances[neighbor] > max_distance:
                        max_distance = distances[neighbor]
                elif distances[neighbor] > distances[current] + 1:
                    queue.append(neighbor)
                    distances[neighbor] = distances[current] + 1


        print(max_distance)


if __name__ == '__main__':
    main()

