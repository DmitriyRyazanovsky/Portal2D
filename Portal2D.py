import os

import pygame

pygame.init()
w = 600
h = 300
size = w, h
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 30

running = True


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
        image = image.convert_alpha()
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        return image
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)


# создадим группу, содержащую все спрайты
all_sprites = pygame.sprite.Group()


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, x, y):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect.x = x
        self.rect.y = y

    def cut_sheet(self, sheet, columns):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns, sheet.get_height())
        for i in range(columns):
            frame_location = (self.rect.w * i, 0)
            self.frames.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


# загружаем картинку
dragon = AnimatedSprite(load_image("walk.png"), 7, 50, 50)
all_sprites.add(dragon)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dragon.update()

    screen.fill(pygame.Color('white'))
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
