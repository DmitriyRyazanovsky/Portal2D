import pygame

from Block import Block
import Helper


class Field():
    def __init__(self):
        self.wall_image = Helper.load_image('wall.png')
        self.exit_image = Helper.load_image('exit.png')
        self.enter_image = Helper.load_image('enter.png')
        self.walls = pygame.sprite.Group()
        self.exits = pygame.sprite.Group()
        self.enters = pygame.sprite.Group()

    def load(self, level):
        self.level = level
        # self.sprites.clear()

        self.lines = []
        with open('data/Level' + str(self.level) + '.txt') as f:
            for line in f.readlines():
                self.lines.append(line.strip())

        for i in range(len(self.lines)):
            for j in range(len(self.lines[i])):
                x, y = 63 * j, 83 * i
                if self.lines[i][j] == 'X':
                    wall = Block(self.wall_image, x, y)
                    self.walls.add(wall)
                elif self.lines[i][j] == 'E':
                    exit = Block(self.exit_image, x, y)
                    self.exits.add(exit)
                elif self.lines[i][j] == '0':
                    enter = Block(self.enter_image, x, y)
                    self.start_x = x
                    self.start_y = y
                    self.enters.add(enter)

    def draw(self, screen):
        self.walls.draw(screen)
        self.exits.draw(screen)
        self.enters.draw(screen)