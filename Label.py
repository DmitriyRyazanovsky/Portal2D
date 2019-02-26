import pygame

import Helper


# класс - надпись на экране с картинкой
class Label(pygame.sprite.Sprite):
    def __init__(self, w, h):
        super().__init__()
        self.image = Helper.load_image('label.png')
        self.rect = self.image.get_rect()
        self.rect.x = int(w // 2 - self.rect.w // 2)
        self.rect.y = int(h // 2 - self.rect.h // 2)

        self.group = pygame.sprite.Group()
        self.group.add(self)

        self.text = ""
        # крупный шрифт
        self.font1 = pygame.font.SysFont("Arial", 32)
        # мелкий шрифт
        self.font2 = pygame.font.SysFont("Arial", 18)
        self.color = pygame.Color(162, 162, 162)

        self.visible = False

    def draw(self, screen):
        self.group.draw(screen)

        # выводим основную надпись по центру экрана
        text = self.font1.render(self.text, True, self.color)
        x = self.rect.x + self.rect.w // 2 - text.get_width() // 2
        y = self.rect.y + 300
        screen.blit(text, (x, y))

        # выводим вторую надпись
        text = self.font2.render("щелкните мышкой или нажмите пробел для продолжения", True, self.color)
        x = self.rect.x + self.rect.w // 2 - text.get_width() // 2
        y = self.rect.y + 350
        screen.blit(text, (x, y))
