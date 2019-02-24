import Helper
import pygame


class Human(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

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
        self.last_time = 0
        self.right = True

        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())

    def go_right(self):
        self.right = True
        self.rect.x += 2

        if pygame.time.get_ticks() > self.last_time + 45:
            self.cur_frame += 1
            if self.cur_frame == len(self.walk_frames_right):
                self.cur_frame = 0
            self.image = self.walk_frames_right[self.cur_frame]
            self.last_time = pygame.time.get_ticks()

    def go_left(self):
        self.right = False
        self.rect.x -= 2

        if pygame.time.get_ticks() > self.last_time + 45:
            self.cur_frame += 1
            if self.cur_frame == len(self.walk_frames_left):
                self.cur_frame = 0
            self.image = self.walk_frames_left[self.cur_frame]
            self.last_time = pygame.time.get_ticks()

    def run_right(self):
        self.right = True
        self.rect.x += 4

        if pygame.time.get_ticks() > self.last_time + 45:
            self.cur_frame += 1
            if self.cur_frame == len(self.run_frames_right):
                self.cur_frame = 0
            self.image = self.run_frames_right[self.cur_frame]
            self.last_time = pygame.time.get_ticks()

    def run_left(self):
        self.right = False
        self.rect.x -= 4

        if pygame.time.get_ticks() > self.last_time + 45:
            self.cur_frame += 1
            if self.cur_frame == len(self.run_frames_left):
                self.cur_frame = 0
            self.image = self.run_frames_left[self.cur_frame]
            self.last_time = pygame.time.get_ticks()

    def stop(self):
        self.cur_frame = 0
        if self.right:
            self.image = self.walk_frames_right[self.cur_frame]
        else:
            self.image = self.walk_frames_left[self.cur_frame]
