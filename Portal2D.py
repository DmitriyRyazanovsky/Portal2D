from Field import Field
from Human import Human
import pygame

pygame.init()
pygame.key.set_repeat(50, 50)

w = 63*19
h = 83*10
size = w, h
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

running = True
shift = False

human = Human(50, 50)
human_sprites = pygame.sprite.Group()
human_sprites.add(human)

field = Field()
field.load(1)

human.rect.x = field.start_x
human.rect.y = field.start_y

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if shift:
                    human.run_right()
                else:
                    human.go_right()
            elif event.key == pygame.K_LEFT:
                if shift:
                    human.run_left()
                else:
                    human.go_left()
            elif event.key == pygame.K_LSHIFT:
                shift = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                shift = False

    human.update()

    screen.fill(pygame.Color('white'))
    field.draw(screen)
    human_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
