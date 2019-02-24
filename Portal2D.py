from Field import Field
from Human import Human
from Bullet import Bullet
from Helper import load_image
import pygame, os

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

a = 1
w = 63 * 19
h = 83 * 10
size = w, h
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

running = True
shift = False

human = Human(50, 50)
human_sprites = pygame.sprite.Group()
human_sprites.add(human)

bullet_image = load_image('red_bullet.png')
bullet = Bullet(bullet_image, 100, 100)
bullet_sprites = pygame.sprite.Group()
bullet_sprites.add(bullet)

field = Field()
field.load(1)

human.rect.x = field.start_x
human.rect.y = field.start_y

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LSHIFT:
            shift = True
        if event.type == pygame.KEYUP and event.key == pygame.K_LSHIFT:
            shift = False

    x = human.rect.x

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        if shift:
            human.run_right()
        else:
            human.go_right()
    elif keys[pygame.K_LEFT]:
        if shift:
            human.run_left()
        else:
            human.go_left()
    else:
        human.stop()

    if pygame.sprite.spritecollideany(human, field.walls):
        human.rect.x = x

    human.rect.y += a
    if pygame.sprite.spritecollideany(human, field.walls):
        human.rect.y -= a
        a = 2
    # else:
    #    a += 0.1


    screen.fill(pygame.Color('white'))
    field.draw(screen)
    human_sprites.draw(screen)
    bullet_sprites.draw(screen)



    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
