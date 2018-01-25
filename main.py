import sys
from sprites import *
from cells import *
from menu import *

class Simulation:
    def __init__(self, human_count, doors_count):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.walls_co = []
        self.targets = set()
        self.human_count = human_count
        self.doors_count = doors_count
        self.cells = [None] * GRIDWIDTH
        for x in range(GRIDWIDTH):
            self.cells[x] = [None] * GRIDHEIGHT
            for y in range(GRIDHEIGHT):
                self.cells[x][y] = Cell()


    def load_data(self):
        self.map_data = []
        if self.doors_count == 1:
            file = DOOR1
        elif self.doors_count == 2:
            file = DOOR2
        elif self.doors_count == 3:
            file = DOOR3
        with open(file, 'r') as f:
            for line in f:
                self.map_data.append(line)

    def create_humans(self):
        humans = []
        count = 0
        while count < self.human_count:
            x = random.randint(1, 61)
            y = random.randint(4, 45)
            if (x, y) not in (self.targets or humans):
                if not self.cells[x][y].is_wall():
                    Human(self, x, y)
                    count += 1
                    humans.append((x, y))

    def new(self):
        self.load_data()
        self.sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.humans = pygame.sprite.Group()
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '#':
                    Wall(self, col, row)
                    cell = self.cells[col][row]
                    cell.turn_wall()
                    self.walls_co.append((col, row))
                if tile == '0':
                    self.targets.add((col, row))
        self.create_humans()

    def loop(self):
        self.running = True
        while self.running:
            self.clock.tick_busy_loop(FPS)
            self.events()
            self.update()
            self.draw()
            self.clock.tick(100)

    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        self.sprites.update()

    def draw_grid(self):
        for x in range(0, WIDTH, SIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, SIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BLACK)
        self.draw_grid()
        self.sprites.draw(self.screen)
        font = pygame.font.Font('freesansbold.ttf', 16)
        text = font.render('PRESS M FOR MENU OR ESC TO EXIT', True, WHITE)
        rect = text.get_rect()
        rect.center = (WIDTH / 2, 8)
        self.screen.blit(text, rect)
        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
                if event.key == pygame.K_m:
                    menu = Menu(self)
                    menu.view_menu()
                    self.new_human_count = menu.get_humans()
                    self.new_door_count = menu.get_doors()
                    self.running = False

    def get_cell(self, x, y):
        if not 0 < x < len(self.cells) or not 0 < y < len(self.cells[0]):
            return Cell(True)
        else:
            return self.cells[x][y]

def main():


    humans = 20
    doors = 1
    while True:
        s = Simulation(humans, doors)
        p = Path(s)
        s.new()
        p.set_targets()
        p.read_neighbors()
        p.vectors()
        s.loop()
        humans = s.new_human_count
        doors = s.new_door_count

if __name__ == "__main__":
    main()