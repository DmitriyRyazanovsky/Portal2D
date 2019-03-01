import pygame


# класс - простой спрайт с картинкой
class Block(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.up = True
        self.down = True
        self.left = True
        self.right = True
