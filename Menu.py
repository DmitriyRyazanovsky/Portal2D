import pygame
import Helper


# класс - меню на экране
class Menu(pygame.sprite.Sprite):
    # константы с кнопками
    NEW_GAME = 1
    RESTART = 2
    LOAD = 3
    SAVE = 4
    CONTINUE = 5
    EXIT = 6

    def __init__(self, w, h):
        super().__init__()
        self.image = Helper.load_image('menu.png')
        self.rect = self.image.get_rect()
        self.rect.x = int(w // 2 - self.rect.w // 2)
        self.rect.y = int(h // 2 - self.rect.h // 2)

        self.group = pygame.sprite.Group()
        self.group.add(self)

        # шрифт кнопок
        self.font = pygame.font.SysFont("Arial", 18)
        self.font.set_bold(True)

        self.visible = True
        self.start = True

        # координаты мыши
        self.mouse_x = 0
        self.mouse_y = 0
        # текущая кнопка
        self.button = None

    # рисование меню
    def draw(self, screen):
        # рисуем фоновую картинку
        self.group.draw(screen)
        self.button = None

        # рисуем кнопки
        buttons = []
        buttons.append(('НОВАЯ ИГРА', Menu.NEW_GAME))
        if not self.start:
            buttons.append(('УРОВЕНЬ СНАЧАЛА', Menu.RESTART))
        buttons.append(('ЗАГРУЗИТЬ', Menu.LOAD))
        if not self.start:
            buttons.append(('СОХРАНИТЬ', Menu.SAVE))
        if not self.start:
            buttons.append(('ПРОДОЛЖИТЬ', Menu.CONTINUE))
        buttons.append(('ВЫХОД', Menu.EXIT))

        x = 950
        y = 200
        for button in buttons:
            rect = pygame.Rect(900, y, 200, 50)
            # если мышка над кнопкой
            if rect.collidepoint(self.mouse_x, self.mouse_y):
                button_color = pygame.Color(255, 106, 0)
                self.button = button[1]
            else:
                button_color = (172, 172, 172)

            pygame.draw.rect(screen, button_color, rect)

            bevel_color = (64, 128, 255)
            pygame.draw.rect(screen, bevel_color, rect, 5)

            text_color = pygame.Color(255, 255, 255)
            text = self.font.render(button[0], True, text_color)
            screen.blit(text, (x - text.get_width() // 2 + 50, y + 15))

            if self.start:
                y += 100
            else:
                y += 75

    # запоминаем координаты мыши
    def set_mouse(self, x, y):
        self.mouse_x = x
        self.mouse_y = y
