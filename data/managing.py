from data.fight import fight
from data.player import Player
from data.enemy import Enemy

from pygame import locals
import pygame
import random
import time


pygame.init()


class LevelsButton:
    def __init__(self, screen, enemy, draw, background, shown, pos):
        self.enemy = enemy
        self.draw = draw
        self.shown = shown
        self.pos = pos
        self.screen = screen
        self.background = background

        # images
        if self.shown:
            self.image_draw = self.screen.blit(draw, self.pos)


class Manager:
    def __init__(self):
        # screen stuff
        self.screen_size = (1000, 800)
        self.screen = pygame.display.set_mode(self.screen_size)
        self.screen.fill((255, 132, 0))

        # run
        self.page = 1
        self.last_page = 2
        self.run = True

        # IMAGES
        # si son cosas ya dibujadas en pantalla entonces va en pages esto es solo pa imagenes madre mia willy


        # Quit and back
        self.back = pygame.image.load('/Users/xinxiang/Desktop/Ping/Python/CheeseGame/static/back_image_button.png')
        self.quit = pygame.image.load('/Users/xinxiang/Desktop/Ping/Python/CheeseGame/static/quit_image_button.png')

        # page 1
        self.cheese_image_load = pygame.image.load('/Users/xinxiang/Desktop/Ping/Python/CheeseGame/static/cheese_full_icon.png')
        self.cheese_sword_image_load = pygame.image.load('/Users/xinxiang/Desktop/Ping/Python/CheeseGame/static/sword_and_cheese.png')
        self.play_button = pygame.image.load('/Users/xinxiang/Desktop/Ping/Python/CheeseGame/static/play_button.png')

        # page 2
        self.levels_button_image = pygame.image.load('/Users/xinxiang/Desktop/Ping/Python/CheeseGame/static/levels_button.png')
        self.shop_button = pygame.image.load('/Users/xinxiang/Desktop/Ping/Python/CheeseGame/static/shop_button.png')
        self.player_button = pygame.image.load('/Users/xinxiang/Desktop/Ping/Python/CheeseGame/static/player_button.png')

        # page 3
        self.bd_image = pygame.image.load('/Users/xinxiang/Desktop/Ping/Python/CheeseGame/static/bd_levels.png')

        self.level_1 = pygame.image.load('/Users/xinxiang/Desktop/Ping/Python/CheeseGame/static/level_1_button.png')
        self.level_2 = pygame.image.load('/Users/xinxiang/Desktop/Ping/Python/CheeseGame/static/level_2_button.png')
        self.level_3 = pygame.image.load('/Users/xinxiang/Desktop/Ping/Python/CheeseGame/static/level_3_button.png')
        self.level_4 = pygame.image.load('/Users/xinxiang/Desktop/Ping/Python/CheeseGame/static/level_4_button.png')
        self.level_5 = pygame.image.load('/Users/xinxiang/Desktop/Ping/Python/CheeseGame/static/level_5_button.png')
        self.button_list = None
        # in levels.py

        # page_4
        self.wa_button = pygame.image.load('/Users/xinxiang/Desktop/Ping/Python/CheeseGame/static/weapons_and_armor_button.png')
        self.sp_button = pygame.image.load('/Users/xinxiang/Desktop/Ping/Python/CheeseGame/static/spells_and_potions_button.png')

        # page_8
        # player and enemy line is between 35 & 54
        self.background_1 = pygame.image.load('/Users/xinxiang/Desktop/Ping/Python/CheeseGame/static/background_1.png')

        self.level_1_enemy = Enemy(100, 20, 100, 100)
        self.level_2_enemy = Enemy(200, 30, 200, 150)
        self.level_3_enemy = Enemy(300, 40, 300, 300)
        self.level_4_enemy = Enemy(500, 50, 500, 600)
        self.level_5_enemy = Enemy(1000, 200, 1000, 1200)
        self.player = Player()
        self.enemy = None
        self.background = None

    def pages(self, page):
        # menu
        if page == 1:
            self.screen.blit(self.cheese_image_load, (150, 150))  # 600, 250
            self.screen.blit(self.cheese_sword_image_load, (750, 150))  # 100, 250
            self.screen.blit(self.play_button, (375, 500))

        # place where you choose what do you want to do
        if page == 2:
            self.screen.blit(self.levels_button_image, (150, 75))  # levels
            self.screen.blit(self.shop_button, (250, 300))  # store
            self.screen.blit(self.player_button, (150, 525))  # player_stats
            self.screen.blit(self.quit, (845, 15))  # quit

        # levels
        if page == 3:
            self.screen.blit(self.bd_image, (0, 0))
            self.button_list = {
                LevelsButton(self.screen, self.level_1_enemy, self.level_1, self.background_1, True, (150, 150)),
                LevelsButton(self.screen, self.level_2_enemy, self.level_2, self.background_1, True, (100, 425)),
                LevelsButton(self.screen, self.level_3_enemy, self.level_3, self.background_1, True, (475, 600)),
                LevelsButton(self.screen, self.level_4_enemy, self.level_4, self.background_1, True, (650, 250)),
                LevelsButton(self.screen, self.level_5_enemy, self.level_5, self.background_1, True, (730, 50))
            }
            self.screen.blit(self.back, (15, 15))

        # shop
        if page == 4:
            self.screen.fill((100, 50, 25))
            self.screen.blit(self.wa_button, (75, 100))
            self.screen.blit(self.sp_button, (500, 100))
            self.screen.blit(self.back, (15, 15))

        # player stats
        if page == 5:
            self.screen.blit(self.back, (15, 15))

        # weapons and armor shop
        if page == 6:
            pygame.draw.rect(self.screen, (200, 200, 200), (600, 5, 395, 790))
            pygame.draw.rect(self.screen, (200, 200, 200), (15, 15, 140, 70))

        # potions and abilities
        if page == 7:
            pygame.draw.rect(self.screen, (200, 200, 200), (600, 5, 395, 790))
            pygame.draw.rect(self.screen, (200, 200, 200), (15, 15, 140, 70))

        # fight
        if page == 8:
            self.green_bar_player = pygame.draw.rect(self.screen, (0, 255, 0), (20, 20, self.player.bar, 60))
            pygame.draw.rect(self.screen, (200, 200, 200), (20, 20, 375, 60), 3)
            self.rect_ = pygame.draw.rect(self.screen, (200, 200, 200), (300, 300, 300, 300))
            self.screen.blit(self.background, (0, 0))

    def event_run(self):
        while self.run:
            self.pages(self.page)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

                if event.type == pygame.MOUSEBUTTONUP:
                    # menu play button
                    if self.page == 1:
                        if self.play_button.get_rect(topleft=(375, 500)).collidepoint(event.pos):
                            self.page = 2

                    # choose
                    elif self.page == 2:
                        if self.levels_button_image.get_rect(topleft=(150, 75)).collidepoint(event.pos):
                            self.page = 3

                        elif self.shop_button.get_rect(topleft=(250, 300)).collidepoint(event.pos):
                            self.page = 4

                        elif self.player_button.get_rect(topleft=(150, 525)).collidepoint(event.pos):
                            self.page = 5

                        elif self.quit.get_rect(topleft=(845, 15)).collidepoint(event.pos):
                            self.run = False

                        self.last_page = 2

                    # levels
                    elif self.page == 3:
                        for button in self.button_list:
                            if button.draw.get_rect(topleft=button.pos).collidepoint(pygame.mouse.get_pos()):
                                self.page = 8
                                self.enemy = button.enemy
                                self.background = button.background

                        if self.back.get_rect(topleft=(15, 15)).collidepoint(event.pos):
                            self.page = self.last_page

                    # shop
                    elif self.page == 4:
                        if self.wa_button.get_rect(topleft=(75, 80)).collidepoint(event.pos):
                            self.page = 6
                            self.last_page = 4

                        elif self.back.get_rect(topleft=(15, 15)).collidepoint(event.pos):
                            self.page = self.last_page

                    # fight thing
                    elif self.page == 8:
                        if self.rect_.collidepoint(event.pos):
                            winner = fight(self.screen, event, self.enemy, self.player)
                            if winner == 'player':
                                self.player.cheese += self.enemy.cheese_drop
                                print(self.player.cheese)

                                self.page = 3

                    self.screen.fill((255, 132, 0))
                    pygame.display.flip()

            pygame.display.update()


manager = Manager()
manager.event_run()
