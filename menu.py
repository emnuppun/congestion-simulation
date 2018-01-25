import pygame
from settings import *


class Menu:
    def __init__(self, simulation):
        self.s = simulation
        self.screen = simulation.screen
        self.humans = 20
        self.doors = 1

    def get_humans(self):
        return self.humans

    def get_doors(self):
        return self.doors

    def view_menu(self):
        title = pygame.Rect(((WIDTH / 16) + 1, (HEIGHT / 8) + 1, 7 * WIDTH / 8, HEIGHT / 4))
        menu1 = pygame.Rect(((WIDTH / 4) + 1, (HEIGHT / 2) + 1, 2 * WIDTH / 4, HEIGHT / 10))
        menu2 = pygame.Rect(((WIDTH / 4) + 1, (HEIGHT / 2) + 1 + (3 * HEIGHT / 20), 2 * WIDTH / 4, HEIGHT / 10))
        menu3 = pygame.Rect(((WIDTH / 4) + 1, (HEIGHT / 2) + 1 + (6 * HEIGHT / 20), 2 * WIDTH / 4, HEIGHT / 10))
        font_title = pygame.font.Font('freesansbold.ttf', 64)
        font_menu = pygame.font.Font('freesansbold.ttf', 32)

        self.screen.fill(BLACK)
        pygame.draw.rect(self.screen, LIGHTGREY, menu1)
        pygame.draw.rect(self.screen, LIGHTGREY, menu2)
        pygame.draw.rect(self.screen, LIGHTGREY, menu3)
        pygame.draw.ellipse(self.screen, LIGHTGREY, title)

        title_text = font_title.render('SIMULATION MENU', True, BLUE)
        title_rect = title_text.get_rect()
        title_rect.center = (WIDTH/2,(HEIGHT/4)+3)

        text_simu = font_menu.render('START SIMULATION', True, RED)
        simu_rect = text_simu.get_rect()
        simu_rect.center = (WIDTH/2,(HEIGHT/2)+(HEIGHT/20)+3)

        text_settings = font_menu.render('SETTINGS', True, RED)
        settings_rect = text_settings.get_rect()
        settings_rect.center = (WIDTH/2,(HEIGHT/2)+(4*HEIGHT/20)+3)

        text_exit = font_menu.render('EXIT', True, RED)
        exit_rect = text_exit.get_rect()
        exit_rect.center = (WIDTH/2,(HEIGHT/2)+(7*HEIGHT/20)+3)

        self.screen.blit(title_text, title_rect)
        self.screen.blit(text_simu, simu_rect)
        self.screen.blit(text_settings, settings_rect)
        self.screen.blit(text_exit, exit_rect)

        self.running = True
        while self.running:
            self.screen.fill(BLACK)
            pygame.draw.rect(self.screen, LIGHTGREY, menu1)
            pygame.draw.rect(self.screen, LIGHTGREY, menu2)
            pygame.draw.rect(self.screen, LIGHTGREY, menu3)
            pygame.draw.ellipse(self.screen, LIGHTGREY, title)

            self.screen.blit(title_text, title_rect)
            self.screen.blit(text_simu, simu_rect)
            self.screen.blit(text_settings, settings_rect)
            self.screen.blit(text_exit, exit_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.s.quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if (menu1.left < event.pos[0] < menu1.right) and (menu1.top < event.pos[1] < menu1.bottom):
                            self.running = False
                        if (menu2.left < event.pos[0] < menu2.right) and (menu2.top < event.pos[1] < menu2.bottom):
                            self.view_settings()
                        if (menu3.left < event.pos[0] < menu3.right) and (menu3.top < event.pos[1] < menu3.bottom):
                            self.s.quit()

            pygame.display.flip()

    def view_settings(self):
        title = pygame.Rect(((WIDTH / 16) + 1, (HEIGHT / 8) + 1, 7 * WIDTH / 8, HEIGHT / 4))

        menu1 = pygame.Rect(((WIDTH / 4) + 1), (HEIGHT / 2) + 1, 2 * HEIGHT / 10, HEIGHT / 10)
        door1 = pygame.Rect(((WIDTH / 4) + 1) + 2 * HEIGHT / 10 + 30, (HEIGHT / 2) + 1, HEIGHT / 10, HEIGHT / 10)
        door2 = pygame.Rect(((WIDTH / 4) + 1) + 3 * HEIGHT / 10 + 2 * 30, (HEIGHT / 2) + 1, HEIGHT / 10, HEIGHT / 10)
        door3 = pygame.Rect(((WIDTH / 4) + 1) + 4 * HEIGHT / 10 + 3 * 30, (HEIGHT / 2) + 1, HEIGHT / 10, HEIGHT / 10)

        menu2 = pygame.Rect(((WIDTH / 4) + 1), (HEIGHT / 2) + 1 + (3 * HEIGHT / 20), 2 * HEIGHT / 10, HEIGHT / 10)
        hum1 = pygame.Rect(((WIDTH / 4) + 1) + 2 * HEIGHT / 10 + 30, (HEIGHT / 2) + 1  + (3 * HEIGHT / 20), HEIGHT / 10, HEIGHT / 10)
        hum2 = pygame.Rect(((WIDTH / 4) + 1) + 3 * HEIGHT / 10 + 2 * 30, (HEIGHT / 2) + 1  + (3 * HEIGHT / 20), HEIGHT / 10, HEIGHT / 10)
        hum3 = pygame.Rect(((WIDTH / 4) + 1) + 4 * HEIGHT / 10 + 3 * 30, (HEIGHT / 2) + 1 + (3 * HEIGHT / 20), HEIGHT / 10, HEIGHT / 10)

        menu3 = pygame.Rect(((WIDTH / 4) + 1, (HEIGHT / 2) + 1 + (6 * HEIGHT / 20), 2 * WIDTH / 4, HEIGHT / 10))


        font_title = pygame.font.Font('freesansbold.ttf', 64)
        font_menu = pygame.font.Font('freesansbold.ttf', 32)

        self.screen.fill(BLACK)
        pygame.draw.ellipse(self.screen, LIGHTGREY, title)
        pygame.draw.rect(self.screen, LIGHTGREY, menu1)
        pygame.draw.rect(self.screen, LIGHTGREY, door1)
        pygame.draw.rect(self.screen, LIGHTGREY, door2)
        pygame.draw.rect(self.screen, LIGHTGREY, door3)

        pygame.draw.rect(self.screen, LIGHTGREY, menu2)
        pygame.draw.rect(self.screen, LIGHTGREY, hum1)
        pygame.draw.rect(self.screen, LIGHTGREY, hum2)
        pygame.draw.rect(self.screen, LIGHTGREY, hum3)

        pygame.draw.rect(self.screen, LIGHTGREY, menu3)

        title_text = font_title.render('SIMULATION SETTINGS', True, BLUE)
        title_rect = title_text.get_rect()
        title_rect.center = (WIDTH / 2, (HEIGHT / 4) + 3)


        text_door = font_menu.render('DOORS:', True, RED)
        door_rect = text_door.get_rect()
        door_rect.center = (WIDTH / 4 + HEIGHT / 10, (HEIGHT/2)+(HEIGHT/20)+3)

        text_dop1 = font_menu.render('1', True, RED)
        dop1_rect = text_dop1.get_rect()
        dop1_rect.center = (WIDTH / 4 + 2 * HEIGHT / 10 + 30 + HEIGHT/20, (HEIGHT/2)+(HEIGHT/20)+3)

        text_dop2 = font_menu.render('2', True, RED)
        dop2_rect = text_dop1.get_rect()
        dop2_rect.center = (WIDTH / 4 + 3 * HEIGHT / 10 + 2 * 30 + HEIGHT / 20, (HEIGHT / 2) + (HEIGHT / 20) + 3)

        text_dop3 = font_menu.render('3', True, RED)
        dop3_rect = text_dop1.get_rect()
        dop3_rect.center = (WIDTH / 4 + 4 * HEIGHT / 10 + 3 * 30 + HEIGHT / 20, (HEIGHT / 2) + (HEIGHT / 20) + 3)



        text_hum = font_menu.render('HUMANS:', True, RED)
        hum_rect = text_door.get_rect()
        hum_rect.center = (WIDTH / 4 + HEIGHT / 10 - 12, (HEIGHT / 2) + (4*HEIGHT / 20) + 3)

        text_hum1 = font_menu.render('20', True, RED)
        hum1_rect = text_dop1.get_rect()
        hum1_rect.center = (WIDTH / 4 + 2 * HEIGHT / 10 + 30 + HEIGHT / 20 - 8, (HEIGHT / 2) + (4*HEIGHT / 20) + 3)

        text_hum2 = font_menu.render('50', True, RED)
        hum2_rect = text_dop1.get_rect()
        hum2_rect.center = (WIDTH / 4 + 3 * HEIGHT / 10 + 2 * 30 + HEIGHT / 20 - 8, (HEIGHT / 2) + (4*HEIGHT / 20) + 3)

        text_hum3 = font_menu.render('80', True, RED)
        hum3_rect = text_dop1.get_rect()
        hum3_rect.center = (WIDTH / 4 + 4 * HEIGHT / 10 + 3 * 30 + HEIGHT / 20 - 8,(HEIGHT/2)+(4*HEIGHT/20)+3)

        text_exit = font_menu.render('BACK', True, RED)
        exit_rect = text_exit.get_rect()
        exit_rect.center = (WIDTH / 2, (HEIGHT / 2) + (7 * HEIGHT / 20) + 3)

        self.screen.blit(title_text, title_rect)
        self.screen.blit(text_exit, exit_rect)
        self.screen.blit(text_door, door_rect)
        self.screen.blit(text_dop1, dop1_rect)
        self.screen.blit(text_dop2, dop2_rect)
        self.screen.blit(text_dop3, dop3_rect)
        self.screen.blit(text_hum, hum_rect)
        self.screen.blit(text_hum1, hum1_rect)
        self.screen.blit(text_hum2, hum2_rect)
        self.screen.blit(text_hum3, hum3_rect)


        view_run = True
        while view_run:
            self.screen.fill(BLACK)
            pygame.draw.ellipse(self.screen, LIGHTGREY, title)
            pygame.draw.rect(self.screen, LIGHTGREY, menu1)
            pygame.draw.rect(self.screen, LIGHTGREY, door1)
            pygame.draw.rect(self.screen, LIGHTGREY, door2)
            pygame.draw.rect(self.screen, LIGHTGREY, door3)

            pygame.draw.rect(self.screen, LIGHTGREY, menu2)
            pygame.draw.rect(self.screen, LIGHTGREY, hum1)
            pygame.draw.rect(self.screen, LIGHTGREY, hum2)
            pygame.draw.rect(self.screen, LIGHTGREY, hum3)

            pygame.draw.rect(self.screen, LIGHTGREY, menu3)

            self.screen.blit(title_text, title_rect)
            self.screen.blit(text_exit, exit_rect)
            self.screen.blit(text_door, door_rect)
            self.screen.blit(text_dop1, dop1_rect)
            self.screen.blit(text_dop2, dop2_rect)
            self.screen.blit(text_dop3, dop3_rect)
            self.screen.blit(text_hum, hum_rect)
            self.screen.blit(text_hum1, hum1_rect)
            self.screen.blit(text_hum2, hum2_rect)
            self.screen.blit(text_hum3, hum3_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.s.quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if (menu3.left < event.pos[0] < menu3.right) and (menu3.top < event.pos[1] < menu3.bottom):
                            view_run = False
                        if (door1.left < event.pos[0] < door1.right) and (door1.top < event.pos[1] < door1.bottom):
                            text_dop1 = font_menu.render('1', True, YELLOW)
                            text_dop2 = font_menu.render('2', True, RED)
                            text_dop3 = font_menu.render('3', True, RED)
                            self.doors = 1
                        if (door2.left < event.pos[0] < door2.right) and (door2.top < event.pos[1] < door2.bottom):
                            text_dop1 = font_menu.render('1', True, RED)
                            text_dop2 = font_menu.render('2', True, YELLOW)
                            text_dop3 = font_menu.render('3', True, RED)
                            self.doors = 2
                        if (door3.left < event.pos[0] < door3.right) and (door3.top < event.pos[1] < door3.bottom):
                            text_dop1 = font_menu.render('1', True, RED)
                            text_dop2 = font_menu.render('2', True, RED)
                            text_dop3 = font_menu.render('3', True, YELLOW)
                            self.doors = 3
                        if (hum1.left < event.pos[0] < hum1.right) and (hum1.top < event.pos[1] < hum1.bottom):
                            text_hum1 = font_menu.render('20', True, YELLOW)
                            text_hum2 = font_menu.render('50', True, RED)
                            text_hum3 = font_menu.render('80', True, RED)
                            self.humans = 20
                        if (hum2.left < event.pos[0] < hum2.right) and (hum2.top < event.pos[1] < hum2.bottom):
                            text_hum1 = font_menu.render('20', True, RED)
                            text_hum2 = font_menu.render('50', True, YELLOW)
                            text_hum3 = font_menu.render('80', True, RED)
                            self.humans = 50
                        if (hum3.left < event.pos[0] < hum3.right) and (hum3.top < event.pos[1] < hum3.bottom):
                            text_hum1 = font_menu.render('20', True, RED)
                            text_hum2 = font_menu.render('50', True, RED)
                            text_hum3 = font_menu.render('80', True, YELLOW)
                            self.humans = 80


            pygame.display.flip()



