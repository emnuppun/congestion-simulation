import pygame
import random
from vector import *

class Human(pygame.sprite.Sprite):
    def __init__(self, simulation, x, y):
        self.groups = simulation.sprites, simulation.humans
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.simulation = simulation
        self.image = pygame.Surface((SIZE, SIZE), pygame.SRCALPHA, 32) #background transparent
        color_index = random.randint(0, 5)
        pygame.draw.circle(self.image, COLOR_LIST[color_index], (SIZE/2, SIZE/2), HUMAN_RAD)
        self.rect = self.image.get_rect()
        self.vector = Vector(0, 0)
        self.x = x * SIZE + SIZE/2
        self.y = y * SIZE + SIZE/2
        self.x_co = x
        self.y_co = y

    def get_direction(self):
        dir = Direction(self.simulation, self.x_co, self.y_co, self.x , self.y)
        dir.set_vector()
        vector = dir.get_vector()
        self.vector = vector.multiple(SPEED)
        if self.vector.length() > 5:
            self.vector = self.vector.multiple(5/self.vector.length())


    def update(self):
        self.get_direction()
        cell = self.simulation.get_cell(self.x_co, self.y_co)
        cell.de_human()
        self.x += self.vector.x
        self.y += self.vector.y
        self.x_co = int((self.x) / SIZE)
        self.y_co = int((self.y) / SIZE)
        cell = self.simulation.get_cell(self.x_co, self.y_co)
        cell.add_human(self)
        self.rect.x = self.x - SIZE/2
        self.rect.y = self.y - SIZE/2
        if ((self.x_co, self.y_co) in self.simulation.targets):
            cell.de_human()
            self.kill()


class Wall(pygame.sprite.Sprite):
    def __init__(self, simulation, x, y):
        self.groups = simulation.sprites, simulation.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.simulation = simulation
        self.image = pygame.Surface((SIZE, SIZE))
        self.image.fill(LIGHTGREY)
        self.rect = self.image.get_rect()
        self.x_co = x
        self.y_co = y
        self.center = Vector(self.x_co * SIZE + SIZE/2, self.y_co * SIZE + SIZE/2)
        self.rect.x = x * SIZE
        self.rect.y = y * SIZE

