from vector import  *

class Cell(object):

    def __init__(self, is_wall = False):
        self.vector = Vector()
        self.distance = None
        self.wall = is_wall
        self.human = None

    def turn_wall(self):
        self.wall = True

    def is_wall(self):
        return self.wall

    def get_vector(self):
        return self.vector

    def get_dis(self):
        return self.distance

    def add_human(self, human):
        self.human = human

    def de_human(self):
        self.human = None

    def is_human(self):
        if not (self.human):
            return False
        else:
            return self.human

class Path():
    def __init__(self, simulation):
        self.s = simulation
        self.dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.checked = []
        self.neighbors = []
        self.walls = simulation.walls_co
        self.targets = simulation.targets

    def check_cell(self, x, y):
        if not (0 <= x < len(self.s.cells)) or not (0 <= y < len(self.s.cells[0])):
            return False
        else:
            return True

    def get_cell(self, x, y):
        if not (0 <= x < len(self.s.cells)) or not (0 <= y < len(self.s.cells[0])):
            return Cell(True)
        else:
            return self.s.cells[x][y]

    def set_neighbors(self, x, y):
        for (dx, dy) in self.dir:
            if not (self.check_cell(x + dx, y + dy)):
                continue
            new = (x + dx, y + dy)
            if new in (self.walls) or new in (self.checked) or new in (self.neighbors):
                continue
            self.neighbors.append(new)

    def set_targets(self):
        for (x, y) in self.targets:
            self.s.cells[x][y].distance = 0
            self.checked.append((x, y))
        for (x, y) in self.checked:
            self.set_neighbors(x, y)

    def get_distance(self, x, y):
        min = None
        for (dx, dy) in self.dir:
            dis = self.s.cells[x + dx][y + dy].get_dis()
            if (min == None):
                min = dis
            elif (dis < min) and (dis != None):
                min = dis
        return min

    def read_neighbors(self):
        while self.neighbors:
            x = self.neighbors[0][0]
            y = self.neighbors[0][1]
            self.checked.append((x, y))
            self.s.cells[x][y].distance = self.get_distance(x, y) + 1
            self.set_neighbors(x, y)
            self.neighbors.remove((x, y))

    def create_vector(self, x, y):
        curr_dis = self.get_cell(x, y).get_dis()
        left_cell_dis = self.get_cell(x - 1, y).get_dis()
        if not (left_cell_dis):
            left_cell_dis = curr_dis
        right_cell_dis = self.get_cell(x + 1, y).get_dis()
        if not (right_cell_dis):
            right_cell_dis = curr_dis
        up_cell_dis = self.get_cell(x, y - 1).get_dis()
        if not (up_cell_dis):
            up_cell_dis = curr_dis
        down_cell_dis = self.get_cell(x, y + 1).get_dis()
        if not (down_cell_dis):
            down_cell_dis = curr_dis
        self.s.cells[x][y].vector.x = left_cell_dis - right_cell_dis
        self.s.cells[x][y].vector.y = up_cell_dis - down_cell_dis

    def vectors(self):
        for x in range(len(self.s.cells)):
            for y in range(len(self.s.cells[0])):
                if (x, y) not in self.walls:
                    self.create_vector(x, y)

