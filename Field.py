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

        self.exit_image = Helper.load_image('exit.png')
        self.enter_image = Helper.load_image('enter.png')
        self.back_image = Helper.load_image('back.png')

        # self.block_mask = pygame.mask.from_surface(self.block_image)

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
                if self.lines[i][j] == '1':
                    # выход
                    self.exit = Block(self.exit_image, x, y, 0, 0, 0, 0)
                    self.exits.add(self.exit)
                    back = Block(self.back_image, x, y, 0, 0, 0, 0)
                    self.backs.add(back)
                elif self.lines[i][j] == '0':
                    # старт
                    self.enter = Block(self.enter_image, x, y, 0, 0, 0, 0)
                    self.enters.add(self.enter)
                    back = Block(self.back_image, x, y, 0, 0, 0, 0)
                    self.backs.add(back)
                elif self.lines[i][j] == ' ':
                    # задний фон
                    back = Block(self.back_image, x, y, 0, 0, 0, 0)
                    self.backs.add(back)

                elif self.lines[i][j] == 'A':
                    top = 0
                    bottom = 1
                    left = 0
                    right = 1
                    f = Block(self.A, x, y, top, bottom, left, right)
                    self.blocks.add(f)

                elif self.lines[i][j] == 'B':
                    top = 0
                    bottom = 1
                    left = 1
                    right = 1
                    f = Block(self.B, x, y, top, bottom, left, right)
                    self.blocks.add(f)

                elif self.lines[i][j] == 'C':
                    top = 0
                    bottom = 1
                    left = 0
                    right = 0
                    f = Block(self.C, x, y, top, bottom, left, right)
                    self.blocks.add(f)

                elif self.lines[i][j] == 'D':
                    top = 0
                    bottom = 1
                    left = 1
                    right = 0
                    f = Block(self.D, x, y, top, bottom, left, right)
                    self.blocks.add(f)

                elif self.lines[i][j] == 'E':
                    top = 0
                    bottom = 0
                    left = 0
                    right = 1
                    f = Block(self.E, x, y, top, bottom, left, right)
                    self.blocks.add(f)

                elif self.lines[i][j] == 'H':
                    top = 1
                    bottom = 1
                    left = 1
                    right = 0
                    f = Block(self.H, x, y, top, bottom, left, right)
                    self.blocks.add(f)

                elif self.lines[i][j] == 'I':
                    top = 1
                    bottom = 1
                    left = 0
                    right = 1
                    f = Block(self.I, x, y, top, bottom, left, right)
                    self.blocks.add(f)

                elif self.lines[i][j] == 'L':
                    top = 0
                    bottom = 0
                    left = 1
                    right = 0
                    f = Block(self.L, x, y, top, bottom, left, right)
                    self.blocks.add(f)

                elif self.lines[i][j] == 'M':
                    top = 1
                    bottom = 0
                    left = 0
                    right = 1
                    f = Block(self.M, x, y, top, bottom, left, right)
                    self.blocks.add(f)

                elif self.lines[i][j] == 'N':
                    top = 1
                    bottom = 0
                    left = 0
                    right = 0
                    f = Block(self.N, x, y, top, bottom, left, right)
                    self.blocks.add(f)

                elif self.lines[i][j] == 'O':
                    top = 1
                    bottom = 0
                    left = 1
                    right = 1
                    f = Block(self.O, x, y, top, bottom, left, right)
                    self.blocks.add(f)

                elif self.lines[i][j] == 'P':
                    top = 1
                    bottom = 0
                    left = 1
                    right = 0
                    f = Block(self.P, x, y, top, bottom, left, right)
                    self.blocks.add(f)

                elif self.lines[i][j] == 'Q':
                    top = 0
                    bottom = 0
                    left = 1
                    right = 1
                    f = Block(self.Q, x, y, top, bottom, left, right)
                    self.blocks.add(f)

                elif self.lines[i][j] == 'R':
                    top = 1
                    bottom = 1
                    left = 0
                    right = 0
                    f = Block(self.R, x, y, top, bottom, left, right)
                    self.blocks.add(f)

                elif self.lines[i][j] == 'S':
                    top = 1
                    bottom = 1
                    left = 1
                    right = 1
                    f = Block(self.S, x, y, top, bottom, left, right)
                    self.blocks.add(f)

    # рисование поля на экране
    def draw(self, screen):
        self.backs.draw(screen)
        self.blocks.draw(screen)
        self.exits.draw(screen)
        self.enters.draw(screen)
