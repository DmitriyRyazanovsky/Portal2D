import pygame


# класс - простой спрайт с картинкой
class Block(pygame.sprite.Sprite):
    def __init__(self, image, x, y,up,down,left,right):
        super().__init__()
        self.image = image
        self.rect = image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.up = up
        self.down = down
        self.left = left
        self.right = right
