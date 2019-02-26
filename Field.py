import pygame

from Block import Block
import Helper


# класс - игровое поле
class Field:
    def __init__(self):
        self.wall_image = Helper.load_image('wall.png')
        self.block_image = Helper.load_image('block.png')
        self.exit_image = Helper.load_image('exit.png')
        self.enter_image = Helper.load_image('enter.png')
        self.back_image = Helper.load_image('back.png')

        self.block_mask = pygame.mask.from_surface(self.block_image)

        self.blocks = pygame.sprite.Group()
        self.exits = pygame.sprite.Group()
        self.enters = pygame.sprite.Group()
        self.backs = pygame.sprite.Group()

        self.level = 0

    # загрузка поля из файла
    def load(self, level):
        self.level = level
        self.lines = []

        # очистка поля
        self.blocks.remove(self.blocks)
        self.exits.remove(self.exits)
        self.enters.remove(self.enters)
        self.backs.remove(self.backs)

        with open('data/Level' + str(level) + '.txt') as f:
            for line in f.readlines():
                self.lines.append(line.strip())

        for i in range(len(self.lines)):
            for j in range(len(self.lines[i])):
                x, y = 64 * j, 84 * i
                if self.lines[i][j] == 'X':
                    # непробиваемый блок
                    block = Block(self.block_image, x, y)
                    block.mask = self.block_mask
                    block.portal = False
                    self.blocks.add(block)
                elif self.lines[i][j] == 'V':
                    # пробиваемый блок
                    block = Block(self.wall_image, x, y)
                    block.mask = self.block_mask
                    block.portal = True
                    self.blocks.add(block)
                elif self.lines[i][j] == 'E':
                    # выход
                    self.exit = Block(self.exit_image, x, y)
                    self.exits.add(self.exit)
                    back = Block(self.back_image, x, y)
                    self.backs.add(back)
                elif self.lines[i][j] == '0':
                    # старт
                    self.enter = Block(self.enter_image, x, y)
                    self.enters.add(self.enter)
                    back = Block(self.back_image, x, y)
                    self.backs.add(back)
                elif self.lines[i][j] == ' ':
                    # задний фон
                    back = Block(self.back_image, x, y)
                    self.backs.add(back)

    # рисование поля на экране
    def draw(self, screen):
        self.backs.draw(screen)
        self.blocks.draw(screen)
        self.exits.draw(screen)
        self.enters.draw(screen)
