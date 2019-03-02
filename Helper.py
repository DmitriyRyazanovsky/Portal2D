import os
import pygame
import math


# загрузка картинки из файла
def load_image(name):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
        image = image.convert_alpha()
        return image
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)


# получение фрэймов из спрайта
def get_frames(image, columns):
    w = image.get_width() // columns
    h = image.get_height()
    frames = []
    for i in range(columns):
        frame = image.subsurface(pygame.Rect(w * i, 0, w, h))
        frames.append(frame)
    return frames


# проверка, что маска спрайта пересеклась с группой спрайтов
def mask_collide_sprites(mask, sprites):
    for sprite in sprites:
        if pygame.sprite.collide_mask(mask, sprite):
            return sprite
    return False
