import math
from settings import *

class Vector():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def multiple(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def add(self, vector):
        return Vector(self.x + vector.x, self.y + vector.y)

    def subtraction(self, vector):
        return Vector(self.x - vector.x, self.y - vector.y)

    def scale(self):
        l = self.length()
        if (l == 0):
            l = 1
        return Vector(self.x/l, self.y/l)

    def length(self):
        return (math.sqrt(pow(self.x, 2) + pow(self.y, 2)))

    def distance(self, vector):
        return (math.sqrt(pow(self.x - vector.x, 2) + pow(self.y - vector.y, 2)))

    def print_vec(self):
        print (self.x, self.y)


class Direction():

    def __init__(self, simulation, x_co, y_co, x, y):
        self.vector = Vector()
        self.avoid_vec = Vector(0,0)
        self.sep_vec = Vector(0,0)
        self.seek_vec = Vector(0,0)
        self.braking = 1
        self.s = simulation
        self.x_co = x_co
        self.y_co = y_co
        self.center = Vector(x, y)

    def set_vector(self):

        self.get_avoidance()
        self.vector = self.vector.add(self.avoid_vec)

        self.get_seeking()
        self.vector = self.vector.add(self.seek_vec)

        self.get_separation()
        '''
        print "Whole", self.vector.x, self.vector.y
        print "Avoid", self.avoid_vec.x, self.avoid_vec.y
        print "Seek", self.seek_vec.x, self.seek_vec.y
        print "Separat", self.sep_vec.x, self.sep_vec.y
        print "Braking", self.braking
        '''
        self.vector = self.vector.multiple(self.braking)

        check = False
        if (self.vector.x == 0):
            for (x, y) in self.s.targets:
                if (self.x_co == x):
                    check = True
                    break
            if not check:
                self.vector.x = -1
        check = False
        if (self.vector.y == 0):
            for (x, y) in self.s.targets:
                if (self.y_co == y):
                    check = True
                    break
            if not check:
                self.vector.y = -1

        if self.avoid_vec.length() == 0 and self.sep_vec.length() == 0:
            self.vector.multiple(10)

    def get_vector(self):
        return self.vector

#Avoidance
    def get_avoidance(self):
        vector_list = []
        for wall in self.s.walls:
            wall_vec = wall.center
            if self.center.distance(wall_vec) < 25:
                vector_list.append(wall_vec)
                self.avoid_vec = self.avoid_vec.add(self.center.subtraction(wall_vec))

        self.avoid_vec = self.avoid_vec.scale()

        #Little fix if human is stuck at a walls corner
        if (round(abs(self.avoid_vec.x),6) - round(abs(self.avoid_vec.y),6)) == 0:
            self.avoid_vec.x = 0
            self.avoid_vec.y *= 80

        self.avoid_vec = self.avoid_vec.multiple(0.525)

#Separation
    def get_separation(self):
        vector_list = []
        for human in self.s.humans:
            human_vec = Vector(human.x, human.y)
            if self.center.distance(human_vec) < 20:
                self.sep_vec = self.sep_vec.add(self.center.subtraction(human_vec))
                vector_list.append(human)

        self.sep_vec = self.sep_vec.scale()
        self.sep_vec = self.sep_vec.multiple(0.475)

        self.vector = self.vector.add(self.sep_vec)

        self.get_braking(vector_list)

#Seeking
    def get_seeking(self):
        cell = self.s.get_cell(self.x_co, self.y_co)
        cell_center = Vector(self.x_co * SIZE + SIZE/2, self.y_co * SIZE + SIZE/2)
        self.seek_vec = cell.get_vector()


        #Little fix when human is stuck between two cells
        if (self.seek_vec.x == 0 or self.seek_vec.y == 0) and self.center.distance(cell_center) > 0.2:
            temp_vec = self.center.subtraction(cell_center)
            self.seek_vec = self.seek_vec.add(temp_vec.multiple(0.05))


        self.seek_vec = self.seek_vec.multiple(0.08)


#Braking
    def get_braking(self, humans):

        if (self.vector.x < 0):
            dx = -1
        else:
            dx = 1
        if (self.vector.y < 0):
            dy = -1
        else:
            dy = 1

        x_limit = self.center.x + dx * 20
        y_limit = self.center.y + dy * 20

        check = False
        for human in humans:
            min_x = min(x_limit, self.center.x)
            max_x = max(x_limit, self.center.x)
            min_y = min(y_limit, self.center.y)
            max_y = max(y_limit, self.center.y)
            if min_x <= human.x <= max_x and min_y <= human.y <= max_y and human.vector.length() < self.vector.length():
                self.braking = 0.5
                check = True
                break

        if not check:
            self.braking = 1
