from Human import Human
import Helper
import pygame

pygame.init()
w = 600
h = 300
size = w, h
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 30

running = True

# создадим группу, содержащую все спрайты
all_sprites = pygame.sprite.Group()

# загружаем картинку
human = Human(Helper.load_image("walk.png"), 7, 50, 50)
all_sprites.add(human)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    human.update()

    screen.fill(pygame.Color('white'))
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
