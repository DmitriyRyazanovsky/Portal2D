import pygame

from Block import Block
import Helper


# класс - игровое поле
class Field:
    def __init__(self):
        self.wall_image = Helper.load_image('wall.png')
        self.A = Helper.load_image('A.png')
        self.B = Helper.load_image('B.png')
        self.C = Helper.load_image('C.png')
        self.D = Helper.load_image('D.png')
        self.E = Helper.load_image('E.png')
        self.H = Helper.load_image('H.png')
        self.I = Helper.load_image('I.png')
        self.L = Helper.load_image('L.png')
        self.M = Helper.load_image('M.png')
        self.N = Helper.load_image('N.png')
        self.O = Helper.load_image('O.png')
        self.P = Helper.load_image('P.png')
        self.Q = Helper.load_image('Q.png')
        self.R = Helper.load_image('R.png')
        self.S = Helper.load_image('S.png')
        self.T = Helper.load_image('T.png')

        self.exit_image = Helper.load_image('exit.png')
        self.enter_image = Helper.load_image('enter.png')
        self.back_image = Helper.load_image('back.png')

        self.block_mask = pygame.mask.from_surface(self.wall_image)

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

        # загружаем строки из файла
        with open('data/Level' + str(level) + '.txt') as f:
            for line in f.readlines():
                self.lines.append(line.strip())

        # загружаем блоки
        for i in range(len(self.lines)):
            for j in range(len(self.lines[i])):
                x, y = 64 * j, 84 * i
                if self.lines[i][j] == '1':
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
                elif self.lines[i][j] == 'A':
                    block = Block(self.A, x, y)
                    block.left = False
                    block.up = False
                    self.blocks.add(block)
                elif self.lines[i][j] == 'B':
                    block = Block(self.B, x, y)
                    block.up = False
                    self.blocks.add(block)
                elif self.lines[i][j] == 'C':
                    block = Block(self.C, x, y)
                    block.left = False
                    block.up = False
                    block.right = False
                    self.blocks.add(block)
                elif self.lines[i][j] == 'D':
                    block = Block(self.D, x, y)
                    block.up = False
                    block.right = False
                    self.blocks.add(block)
                elif self.lines[i][j] == 'E':
                    block = Block(self.E, x, y)
                    block.left = False
                    block.up = False
                    block.down = False
                    self.blocks.add(block)
                elif self.lines[i][j] == 'H':
                    block = Block(self.H, x, y)
                    block.right = False
                    self.blocks.add(block)
                elif self.lines[i][j] == 'I':
                    block = Block(self.I, x, y)
                    block.left = False
                    self.blocks.add(block)
                elif self.lines[i][j] == 'L':
                    block = Block(self.L, x, y)
                    block.up = False
                    block.right = False
                    block.down = False
                    self.blocks.add(block)
                elif self.lines[i][j] == 'M':
                    block = Block(self.M, x, y)
                    block.left = False
                    block.down = False
                    self.blocks.add(block)
                elif self.lines[i][j] == 'N':
                    block = Block(self.N, x, y)
                    block.left = False
                    block.right = False
                    block.down = False
                    self.blocks.add(block)
                elif self.lines[i][j] == 'O':
                    block = Block(self.O, x, y)
                    block.down = False
                    self.blocks.add(block)
                elif self.lines[i][j] == 'P':
                    block = Block(self.P, x, y)
                    block.right = False
                    block.down = False
                    self.blocks.add(block)
                elif self.lines[i][j] == 'Q':
                    block = Block(self.Q, x, y)
                    block.up = False
                    block.down = False
                    self.blocks.add(block)
                elif self.lines[i][j] == 'R':
                    block = Block(self.R, x, y)
                    block.left = False
                    block.right = False
                    self.blocks.add(block)
                elif self.lines[i][j] == 'S':
                    block = Block(self.S, x, y)
                    self.blocks.add(block)
                elif self.lines[i][j] == 'T':
                    block = Block(self.T, x, y)
                    block.down = False
                    self.blocks.add(block)

        # задаем маску каждому блоку для ускорения
        for block in self.blocks:
            block.mask = self.block_mask

    # рисование поля на экране
    def draw(self, screen):
        self.backs.draw(screen)
        self.blocks.draw(screen)
        self.exits.draw(screen)
        self.enters.draw(screen)
