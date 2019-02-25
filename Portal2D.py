import Helper
from Human import Human
from Bullet import Bullet
from Field import Field
import pygame, os

from Label import Label
from Menu import Menu
from Portal import Portal

os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()
pygame.display.set_caption('Portal 2D')
pygame.font.init()

w = 63 * 19
h = 83 * 10
size = w, h
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

running = True
shift = False
a = 2

human = Human()
bullet = Bullet()
field = Field()

red_portal = Portal('red_vert.png', 'red_horz.png')
blue_portal = Portal('blue_vert.png', 'blue_horz.png')

label = Label(w, h)
menu = Menu(w, h)


def load_level(level):
    field.load(level)
    human.rect.x = field.start_x
    human.rect.y = field.start_y
    red_portal.visible = False
    blue_portal.visible = False
    bullet.visible = False
    label.visible = True
    label.text = "Уровень " + str(level)
    menu.visible = False
    menu.start = False
    bullet.red = True


def click_menu():
    if menu.button == Menu.NEW_GAME:
        load_level(1)
    elif menu.button == Menu.EXIT:
        global running
        running = False
    elif menu.button == Menu.CONTINUE:
        menu.visible = False
    elif menu.button == Menu.RESTART:
        load_level(field.level)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT):
            shift = True
        if event.type == pygame.KEYUP and (event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT):
            shift = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if label.visible:
                label.visible = False
            elif menu.visible:
                click_menu()
            elif not bullet.visible:
                x1 = human.rect.x + human.rect.w / 2
                y1 = human.rect.y + human.rect.h / 2
                x2 = event.pos[0]
                y2 = event.pos[1]
                bullet.start(x1, y1, x2, y2)
        if label.visible and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            label.visible = False
        if not menu.visible and not label.visible and event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            menu.visible = True
        if menu.visible and event.type == pygame.MOUSEMOTION:
            menu.set_mouse(event.pos[0], event.pos[1])

    if label.visible:
        screen.fill(pygame.Color('black'))
        label.draw(screen)
        pygame.display.flip()
        clock.tick(fps)
        continue

    if menu.visible:
        screen.fill(pygame.Color('black'))
        menu.draw(screen)
        pygame.display.flip()
        clock.tick(fps)
        continue

    x = human.rect.x

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        if shift:
            human.run_right()
        else:
            human.go_right()
    elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
        if shift:
            human.run_left()
        else:
            human.go_left()
    else:
        human.stop()

    if Helper.mask_collide_sprites(human, field.blocks):
        human.rect.x = x

    for i in range(int(a)):
        human.rect.y += 1
        if Helper.mask_collide_sprites(human, field.blocks):
            human.rect.y -= 1
            a = 2
            break
        else:
            a += 0.05
            human.fly()

    if bullet.visible:
        for i in range(15):
            bullet.move()

            if red_portal.visible and pygame.sprite.spritecollideany(bullet, red_portal.group):
                bullet.visible = False
                break

            if blue_portal.visible and pygame.sprite.spritecollideany(bullet, blue_portal.group):
                bullet.visible = False
                break

            block = pygame.sprite.spritecollideany(bullet, field.blocks)
            if block:
                bullet.visible = False

                if block.portal:
                    cx = bullet.rect.x + bullet.rect.w / 2
                    cy = bullet.rect.y + bullet.rect.h / 2

                    if bullet.red:
                        portal = red_portal
                    else:
                        portal = blue_portal

                    if block.rect.x <= cx <= block.rect.x + block.rect.w:
                        if cy < block.rect.y:
                            portal.top(block.rect)
                        else:
                            portal.bottom(block.rect)
                    elif block.rect.y <= cy <= block.rect.y + block.rect.h:
                        if cx < block.rect.x:
                            portal.left(block.rect)
                        else:
                            portal.right(block.rect)
                    else:
                        break

                    if bullet.red:
                        bullet.red = False
                    else:
                        bullet.red = True
                break

    if red_portal.visible and blue_portal.visible:
        if Helper.mask_collide_sprites(human, red_portal.group):
            blue_portal.teleport(human)

    if field.exit.rect.contains(human.rect):
        if field.level == 4:
            load_level(1)
            label.text = "Поздравляю! Игра пройдена!"
            menu.visible = True
            menu.start = True
        else:
            load_level(field.level + 1)
        label.visible = True

    if human.rect.y > h:
        load_level(field.level)

    screen.fill(pygame.Color('white'))
    field.draw(screen)
    human.draw(screen)
    if red_portal.visible:
        red_portal.draw(screen)
    if blue_portal.visible:
        blue_portal.draw(screen)
    if bullet.visible:
        bullet.draw(screen)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
