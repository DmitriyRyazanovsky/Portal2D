import os
import pygame


def load_image(name):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
        image = image.convert_alpha()
        return image
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)


def get_frames(image, columns):
    w = image.get_width() // columns
    h = image.get_height()
    frames = []
    for i in range(columns):
        frame = image.subsurface(pygame.Rect(w * i, 0, w, h))
        frames.append(frame)
    return frames


def mask_collide_sprites(mask, sprites):
    for sprite in sprites:
        if pygame.sprite.collide_mask(mask, sprite):
            return True
    return False