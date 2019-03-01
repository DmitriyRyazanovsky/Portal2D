import Helper
import pygame

from Hand import Hand


class Human(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # загрузка фрэймов
        walk_image = Helper.load_image('walk.png')
        run_image = Helper.load_image('run.png')

        self.walk_frames_right = Helper.get_frames(walk_image, 7)
        self.run_frames_right = Helper.get_frames(run_image, 7)

        left_image = pygame.transform.flip(walk_image, True, False)
        self.walk_frames_left = Helper.get_frames(left_image, 7)
        self.walk_frames_left.reverse()

        left_image = pygame.transform.flip(run_image, True, False)
        self.run_frames_left = Helper.get_frames(left_image, 7)
        self.run_frames_left.reverse()

        self.cur_frame = 0
        self.image = self.walk_frames_right[0]
        self.mask = pygame.mask.from_surface(self.image)

        self.last_time = 0
        self.right = True

        self.rect = self.image.get_rect()

        # создам группу спрайтов и добавляем в нее этот спрайт
        self.group = pygame.sprite.Group()
        self.group.add(self)

        self.hand = Hand()
        self.group.add(self.hand)

        # ускорение падения
        self.acceleration = 2

        self.mouse_x = 0
        self.mouse_y = 0

    # переместить человека в координаты x,y
    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.hand.set_pos(x, y, self.mouse_x, self.mouse_y)

    # сместить человека на dx,dy
    def move(self, dx, dy):
        self.set_pos(self.rect.x + dx, self.rect.y + dy)

    def set_mouse(self, x, y):
        self.mouse_x = x
        self.mouse_y = y

    # перемещение вправо
    def go_right(self):
        self.right = True
        self.move(2, 0)

        # меняем кадр через 45 мс
        if pygame.time.get_ticks() > self.last_time + 45:
            self.cur_frame += 1
            if self.cur_frame == len(self.walk_frames_right):
                self.cur_frame = 0
            self.image = self.walk_frames_right[self.cur_frame]
            self.last_time = pygame.time.get_ticks()

    # перемещение влево
    def go_left(self):
        self.right = False
        self.move(-2, 0)

        if pygame.time.get_ticks() > self.last_time + 45:
            self.cur_frame += 1
            if self.cur_frame == len(self.walk_frames_left):
                self.cur_frame = 0
            self.image = self.walk_frames_left[self.cur_frame]
            self.last_time = pygame.time.get_ticks()

    # бег вправо
    def run_right(self):
        self.right = True
        self.move(4, 0)

        if pygame.time.get_ticks() > self.last_time + 45:
            self.cur_frame += 1
            if self.cur_frame == len(self.run_frames_right):
                self.cur_frame = 0
            self.image = self.run_frames_right[self.cur_frame]
            self.last_time = pygame.time.get_ticks()

    # бег влево
    def run_left(self):
        self.right = False
        self.move(-4, 0)

        if pygame.time.get_ticks() > self.last_time + 45:
            self.cur_frame += 1
            if self.cur_frame == len(self.run_frames_left):
                self.cur_frame = 0
            self.image = self.run_frames_left[self.cur_frame]
            self.last_time = pygame.time.get_ticks()

    # остановка
    def stop(self):
        self.cur_frame = 0
        if self.right:
            self.image = self.walk_frames_right[self.cur_frame]
        else:
            self.image = self.walk_frames_left[self.cur_frame]

    # полет, меняем кадр на 4-й
    def fly(self):
        self.cur_frame = 4
        if self.right:
            self.image = self.walk_frames_right[self.cur_frame]
        else:
            self.image = self.walk_frames_left[self.cur_frame]

    # рисование человека
    def draw(self, screen):
        self.group.draw(screen)
