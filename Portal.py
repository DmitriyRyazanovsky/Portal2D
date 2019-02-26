import pygame

import Helper


# класс - портал
class Portal(pygame.sprite.Sprite):
    # константы - направление выхода из портала
    TOP = 0
    BOTTOM = 1
    LEFT = 2
    RIGHT = 3

    def __init__(self, vert_image, horz_image):
        super().__init__()

        # картинки портала
        self.vert_image = Helper.load_image(vert_image)
        self.horz_image = Helper.load_image(horz_image)

        self.visible = False

        # создаем группу спрайтов и добавляем в нее этот спрайт
        self.group = pygame.sprite.Group()
        self.group.add(self)

    # открываем портал сверху
    def top(self, rect):
        self.image = self.horz_image
        self.rect = self.horz_image.get_rect()
        self.rect.x = rect.x
        self.rect.y = rect.y - self.rect.h // 2
        self.visible = True
        self.orientation = Portal.TOP

    # открываем портал снизу
    def bottom(self, rect):
        self.image = self.horz_image
        self.rect = self.horz_image.get_rect()
        self.rect.x = rect.x
        self.rect.y = rect.y + rect.h - self.rect.h // 2
        self.visible = True
        self.orientation = Portal.BOTTOM

    # открываем портал слева
    def left(self, rect):
        self.image = self.vert_image
        self.rect = self.vert_image.get_rect()
        self.rect.x = rect.x - self.rect.w // 2
        self.rect.y = rect.y
        self.visible = True
        self.orientation = Portal.LEFT

    # открываем портал справа
    def right(self, rect):
        self.image = self.vert_image
        self.rect = self.vert_image.get_rect()
        self.rect.x = rect.x + rect.w - self.rect.w // 2
        self.rect.y = rect.y
        self.visible = True
        self.orientation = Portal.RIGHT

    # телепортируем человека
    def teleport(self, human):
        if self.orientation == Portal.TOP:
            human.rect.x = self.rect.x
            human.rect.y = self.rect.y - human.rect.h
        elif self.orientation == Portal.BOTTOM:
            human.rect.x = self.rect.x
            human.rect.y = self.rect.y + self.rect.h
        elif self.orientation == Portal.LEFT:
            human.rect.x = self.rect.x - human.rect.w
            human.rect.y = self.rect.y
        elif self.orientation == Portal.RIGHT:
            human.rect.x = self.rect.x + self.rect.w
            human.rect.y = self.rect.y

    # рисуем портал на экране
    def draw(self, screen):
        self.group.draw(screen)

    # сохраняем состояние портала в файл
    def save(self, f):
        f.write(str(self.visible) + "\n")
        if self.visible:
            f.write(str(self.orientation) + "\n")
            f.write(str(self.rect.x) + "\n")
            f.write(str(self.rect.y) + "\n")

    # загружаем состояние портала из файла
    def load(self, lines, i):
        self.visible = lines[i] == "True"
        if self.visible:
            self.orientation = int(lines[i + 1])

            if self.orientation == Portal.LEFT or self.orientation == Portal.RIGHT:
                self.image = self.vert_image
            else:
                self.image = self.horz_image

            self.rect = self.image.get_rect()
            self.rect.x = int(lines[i + 2])
            self.rect.y = int(lines[i + 3])
