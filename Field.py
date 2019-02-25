import pygame

from Block import Block
import Helper


class Field():
    def __init__(self):
        self.wall_image = Helper.load_image('wall.png')
        self.block_image = Helper.load_image('block.png')
        self.exit_image = Helper.load_image('exit.png')
        self.enter_image = Helper.load_image('enter.png')

        self.block_mask = pygame.mask.from_surface(self.block_image)

        self.blocks = pygame.sprite.Group()
        self.exits = pygame.sprite.Group()
        self.enters = pygame.sprite.Group()

    def load(self, level):
        self.lines = []

        self.blocks.remove(self.blocks)
        self.exits.remove(self.exits)
        self.enters.remove(self.enters)

        with open('data/Level' + str(level) + '.txt') as f:
            for line in f.readlines():
                self.lines.append(line.strip())

        for i in range(len(self.lines)):
            for j in range(len(self.lines[i])):
                x, y = 63 * j, 83 * i
                if self.lines[i][j] == 'X':
                    block = Block(self.block_image, x, y)
                    block.mask = self.block_mask
                    block.portal = False
                    self.blocks.add(block)
                elif self.lines[i][j] == 'V':
                    block = Block(self.wall_image, x, y)
                    block.mask = self.block_mask
                    block.portal = True
                    self.blocks.add(block)
                elif self.lines[i][j] == 'E':
                    self.exit = Block(self.exit_image, x, y)
                    self.exits.add(self.exit)
                elif self.lines[i][j] == '0':
                    enter = Block(self.enter_image, x, y)
                    self.start_x = x
                    self.start_y = y
                    self.enters.add(enter)

    def draw(self, screen):
        self.blocks.draw(screen)
        self.exits.draw(screen)
        self.enters.draw(screen)
