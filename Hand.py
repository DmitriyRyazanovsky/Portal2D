import Helper
import pygame
import math


# класс - рука человека
class Hand(pygame.sprite.Sprite):
    # координаты плеча - центра вращения руки
    SHOULDER_X = 27
    SHOULDER_Y = 30

    def __init__(self):
        super().__init__()

        self.red_hand_image = Helper.load_image('red_hand.png')
        self.blue_hand_image = Helper.load_image('blue_hand.png')
        self.image = self.red_hand_image
        self.rect = self.image.get_rect()
        self.angle = 0
        self.red = True

    # установить руку с пушкой
    # x1, y1 - координаты человека
    # x2, y2 - координаты мышки
    def set_pos(self, x1, y1, x2, y2):
        # цетр вращения руки человека
        x1 += Hand.SHOULDER_X
        y1 += Hand.SHOULDER_Y
        # угол поворота пушки
        angle = math.atan2(y1 - y2, x2 - x1) * 180 / math.pi
        # если угол поменялся, то поворачиваем картинку с рукой
        if angle != self.angle:
            if self.red:
                self.image = pygame.transform.rotate(self.red_hand_image, angle)
            else:
                self.image = pygame.transform.rotate(self.blue_hand_image, angle)
            self.angle = angle
        # задаем новые координаты руки
        self.rect = self.image.get_rect()
        self.rect.x = x1 - self.rect.w // 2
        self.rect.y = y1 - self.rect.h // 2
