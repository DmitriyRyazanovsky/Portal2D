import Helper
import pygame

NONE = 0
GO_RIGHT = 1
RUN_RIGHT = 2
GO_LEFT = 3
RUN_LEFT = 4


class Human(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.state = NONE

        walk_image = Helper.load_image('walk.png')
        run_image = Helper.load_image('run.png')

        self.walk_frames = Helper.get_frames(walk_image, 7)
        self.run_frames = Helper.get_frames(run_image, 7)

        left_image = pygame.transform.flip(walk_image, True, False)
        self.walk_frames_L = Helper.get_frames(left_image, 7)

        left_image = pygame.transform.flip(run_image, True, False)
        self.run_frames_L = Helper.get_frames(left_image, 7)

        self.cur_frame = 0
        self.image = self.walk_frames[0]

        self.rect = pygame.Rect(x, y, self.image.get_width(), self.image.get_height())

    def go_right(self):
        if self.state != GO_RIGHT:
            self.state = GO_RIGHT
            self.ticks = pygame.time.get_ticks()

    def run_right(self):
        if self.state != RUN_RIGHT:
            self.state = RUN_RIGHT
            self.ticks = pygame.time.get_ticks()

    def go_left(self):
        if self.state != GO_LEFT:
            self.state = GO_LEFT
            self.ticks = pygame.time.get_ticks()

    def run_left(self):
        if self.state != RUN_LEFT:
            self.state = RUN_LEFT
            self.ticks = pygame.time.get_ticks()

    def update(self):
        if self.state == RUN_LEFT:
            if pygame.time.get_ticks() > self.ticks + 40:
                self.cur_frame += 1

                if self.cur_frame == len(self.run_frames_L):
                    self.cur_frame = 0
                    self.state = NONE

                self.rect.x -= 9
                self.image = self.run_frames_L[self.cur_frame]
                self.ticks = pygame.time.get_ticks()

        if self.state == GO_LEFT:
            if pygame.time.get_ticks() > self.ticks + 60:
                self.cur_frame += 1

                if self.cur_frame == len(self.walk_frames_L):
                    self.cur_frame = 0
                    self.state = NONE

                self.rect.x -= 6
                self.image = self.walk_frames_L[self.cur_frame]
                self.ticks = pygame.time.get_ticks()

        if self.state == RUN_RIGHT:
            if pygame.time.get_ticks() > self.ticks + 40:
                self.cur_frame += 1

                if self.cur_frame == len(self.run_frames):
                    self.cur_frame = 0
                    self.state = NONE

                self.rect.x += 9
                self.image = self.run_frames[self.cur_frame]
                self.ticks = pygame.time.get_ticks()

        if self.state == GO_RIGHT:
            if pygame.time.get_ticks() > self.ticks + 60:
                self.cur_frame += 1

                if self.cur_frame == len(self.walk_frames):
                    self.cur_frame = 0
                    self.state = NONE

                self.rect.x += 6
                self.image = self.walk_frames[self.cur_frame]
                self.ticks = pygame.time.get_ticks()
