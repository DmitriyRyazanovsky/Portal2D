import pygame

import Helper


class Label(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = Helper.load_image('label.png')
        self.rect = self.image.get_rect()
        self.group = pygame.sprite.Group()
        self.group.add(self)

        self.text = ""
        self.font1 = pygame.font.SysFont("Arial", 32)
        self.font2 = pygame.font.SysFont("Arial", 18)
        self.color = pygame.Color(162, 162, 162)

        self.visible = False

    def draw(self, screen):
        self.group.draw(screen)

        text = self.font1.render(self.text, True, self.color)
        x = self.rect.x + self.rect.w // 2 - text.get_width() // 2
        y = self.rect.y + 300
        screen.blit(text, (x, y))

        text = self.font2.render("нажмите пробел для продолжения", True, self.color)
        x = self.rect.x + self.rect.w // 2 - text.get_width() // 2
        y = self.rect.y + 350
        screen.blit(text, (x, y))
