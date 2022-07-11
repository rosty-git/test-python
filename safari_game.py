from random import randint

from animal import Lion, Wolf, Tiger, Deer


class Safari:
    def __init__(self, safari_map, starting_cell):
        self._visited = set()
        self._safari_map = safari_map
        self._starting_cell = starting_cell

    def play(self):
        valid_cells = self.get_valid_cells(self._starting_cell)
        self.get_animal_from_cell(self._starting_cell)._conquered = True
        print("start")
        self.print_map()
        self.conquer_neighbours(self._starting_cell, valid_cells)

    def get_valid_cells(self, cell):
        max_x = len(self._safari_map[0]) - 1
        max_y = len(self._safari_map) - 1
        neighbors = lambda x, y: [(x2, y2) for x2 in range(x - 1, x + 2)
                                  for y2 in range(y - 1, y + 2)
                                  if (-1 < x <= max_x and
                                      -1 < y <= max_y and
                                      (x != x2 or y != y2) and
                                      (0 <= x2 <= max_x) and
                                      (0 <= y2 <= max_y))]

        valid_cells = [c for c in neighbors(cell[0], cell[1]) if c not in self._visited]
        return valid_cells

    def conquer_and_replace(self, cell, neighbour_cell):
        current_animal = self.get_animal_from_cell(cell)
        next_animal = self.get_animal_from_cell(neighbour_cell)
        result = current_animal.conquer(next_animal)
        if result:
            self._safari_map[neighbour_cell[0]][neighbour_cell[1]] = current_animal.clone_conquered()
        return result

    def get_animal_from_cell(self, cell):
        return self._safari_map[cell[0]][cell[1]]

    def conquer_neighbours(self, cell, valid_cells):
        for neighbour_cell in valid_cells:
            conquered = self.conquer_and_replace(cell, neighbour_cell)
            self._visited.add(neighbour_cell)
            if conquered:
                valid_cells = self.get_valid_cells(neighbour_cell)
                self.conquer_neighbours(neighbour_cell, valid_cells)

    def print_map(self):
        rep = ('\n'.join([''.join(['{:4}'.format(item.__str__()) for item in row])
                          for row in self._safari_map]))
        print(rep)
        return rep

    def print_start(self):
        animal_letter = self.get_animal_from_cell(self._starting_cell).__str__()
        start_cell_str = str(self._starting_cell[0] + 1) + " - " + str(self._starting_cell[1] + 1)
        print(start_cell_str + " -> " + animal_letter)


def get_random_animal():
    animals = [Lion(), Tiger(), Wolf(), Deer()]
    return animals[randint(0, 3)]


def create_random_map(size):
    return [[get_random_animal() for x in range(size)] for y in range(size)]


def get_random_cell(safari_map):
    return randint(0, len(safari_map[0]) - 1), randint(0, len(safari_map) - 1)


def main():
    # 1 2 create map and chose random cell
    safari_map = create_random_map(10)
    start_cell = get_random_cell(safari_map)

    # 3 Output of the board to the screen
    safari = Safari(safari_map, start_cell)
    safari.print_map()

    # 4
    safari.print_start()

    safari.play()

    # 5 print the board again
    print("end")
    safari.print_map()


if __name__ == "__main__":
    main()
