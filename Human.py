import pygame
from AnimatedSprite import AnimatedSprite


class Human(AnimatedSprite):
    def __init__(self, sheet, columns, x, y):
        super().__init__(sheet, columns, x, y)
