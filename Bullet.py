import pygame

import Helper
import math


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.red_image = Helper.load_image('red_bullet.png')
        self.blue_image = Helper.load_image('blue_bullet.png')
        self.image = self.blue_image
        self.rect = self.blue_image.get_rect()
        self.visible = False
        self.red = True

        self.group = pygame.sprite.Group()
        self.group.add(self)

    def start(self, x1, y1, x2, y2):
        if self.red:
            self.image = self.red_image
        else:
            self.image = self.blue_image
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x = x1
        self.y = y1
        self.visible = True

    def move(self):
        d = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        dx = (self.x2 - self.x1) / d
        dy = (self.y2 - self.y1) / d
        self.x += dx
        self.y += dy
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def draw(self, screen):
        self.group.draw(screen)