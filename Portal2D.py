import pygame, os

import Helper
from Human import Human
from Bullet import Bullet
from Field import Field
from Hand import Hand
from Label import Label
from Menu import Menu
from Portal import Portal

# окно по центру
os.environ['SDL_VIDEO_CENTERED'] = '1'

# запускаем окно
pygame.init()
pygame.display.set_caption('Portal 2D')

# запускаем работу со шрифтами
pygame.font.init()

# ширина окна, 19 блоков по 64 пикселя
w = 64 * 19
# высота окна, 10 блоков по 84 пикселя
h = 84 * 10
size = w, h
screen = pygame.display.set_mode(size)
# запускаем таймер 60 fps
clock = pygame.time.Clock()
fps = 60

running = True
shift = False

# создаем человека
human = Human()
# создаем пулю
bullet = Bullet()
# создаем пулю
field = Field()

# создаем красный портал
red_portal = Portal('red_vert.png', 'red_horz.png')
# создаем синий портал
blue_portal = Portal('blue_vert.png', 'blue_horz.png')

# создаем надпись на экране с картинкой
label = Label(w, h)
# создаем меню
menu = Menu(w, h)

# подгружаем звук завершения уровня
win_sound = pygame.mixer.Sound('data/tada.wav')


# загрузка уровня
def load_level(level):
    # загружаем поле
    field.load(level)
    # человека ставим где вход
    human.set_pos(field.enter.rect.x, field.enter.rect.y)
    # убираем порталы и пулю
    red_portal.visible = False
    blue_portal.visible = False
    bullet.visible = False
    # показываем какой сейчас уровень
    label.visible = True
    label.text = "Уровень " + str(level)
    # прячем меню
    menu.visible = False
    # переключаемся в игровое меню
    menu.start = False
    # сперва стреляем красной пулей
    human.hand.red = True
    # в заголовке окна показываем номер уровня
    pygame.display.set_caption('Portal 2D - уровень ' + str(level))


# сохранение игры
def save_game():
    # сохраняе под именем текущего пользователя в каталоге saves
    user = os.environ.get("USERNAME")
    file = 'saves/' + user + ".save"

    # сохраняем текущее состояние
    with open(file, "wt") as f:
        f.write(str(field.level) + "\n")
        f.write(str(human.rect.x) + "\n")
        f.write(str(human.rect.y) + "\n")
        f.write(str(human.hand.red) + "\n")

        red_portal.save(f)
        blue_portal.save(f)

    # после сохранения прячем меню
    menu.visible = False


# загружаем игру
def load_game():
    # загружаем под именем текущего пользователя из каталога saves
    user = os.environ.get("USERNAME")
    file = 'saves/' + user + ".save"

    # считываем файл
    try:
        with open(file, "rt") as f:
            lines = f.readlines()
    except Exception:
        # если файла нет, то ничего не делаем
        return

    # загружаем текущее состояние
    lines = [s.strip() for s in lines]

    level = int(lines[0])
    load_level(level)

    human.set_pos(int(lines[1]), int(lines[2]))
    human.hand.red = lines[3] == "True"

    red_portal.load(lines, 4)
    if red_portal.visible:
        blue_portal.load(lines, 8)
    else:
        blue_portal.load(lines, 5)


# обработка щелчка в меню
def click_menu():
    # если новая игра, то загружаем уровень 1
    if menu.button == Menu.NEW_GAME:
        load_level(1)
    # если выход, то завершаем программу
    elif menu.button == Menu.EXIT:
        global running
        running = False
    # если продолжить, то прячем меню
    elif menu.button == Menu.CONTINUE:
        menu.visible = False
    # если перезапуск уровня, то загружаем уровень заново
    elif menu.button == Menu.RESTART:
        load_level(field.level)
    # сохранение игры
    elif menu.button == Menu.SAVE:
        save_game()
    # загрузка игры
    elif menu.button == Menu.LOAD:
        load_game()


# открытие портала
def open_portal(block):
    # центр пули
    cx = bullet.rect.x + bullet.rect.w / 2
    cy = bullet.rect.y + bullet.rect.h / 2

    if human.hand.red:
        portal = red_portal
    else:
        portal = blue_portal

    # вычисляем с какой стороны портал
    if block.rect.x <= cx <= block.rect.x + block.rect.w:
        if cy < block.rect.y and block.up:
            portal.top(block.rect)
        elif cy > block.rect.y and block.down:
            portal.bottom(block.rect)
        else:
            return
    elif block.rect.y <= cy <= block.rect.y + block.rect.h:
        if cx < block.rect.x and block.left:
            portal.left(block.rect)
        elif cx > block.rect.x and block.right:
            portal.right(block.rect)
        else:
            return
    else:
        return

    # меняем цвет следующей пули
    if human.hand.red:
        human.hand.red = False
    else:
        human.hand.red = True


# перемещение пули
def move_bullet():
    # двигаем по 1 пикселю
    for i in range(15):
        bullet.move()
        # если пуля попала в красный портал
        if red_portal.visible and pygame.sprite.collide_mask(bullet, red_portal):
            bullet.visible = False
            break

        # если пуля попала в синий потал
        if blue_portal.visible and pygame.sprite.collide_mask(bullet, blue_portal):
            bullet.visible = False
            break

        # если пуля попала в блок
        block = Helper.mask_collide_sprites(bullet, field.blocks)
        if block:
            bullet.visible = False
            open_portal(block)
            break


# пробуем опустить человека вниз
def try_down():
    for i in range(int(human.acceleration)):
        # опускаем по 1 пикселю
        human.move(0, 1)
        if Helper.mask_collide_sprites(human, field.blocks):
            # если там блок, то возвращаем обратно
            human.move(0, -1)
            human.acceleration = 2
            break
        else:
            # увеличиваем ускорение падения
            human.acceleration += 0.05
            # делаем картинку - человек падает
            human.fly()


while running:
    # обработка событий
    for event in pygame.event.get():
        # закрытие окна
        if event.type == pygame.QUIT:
            running = False
        # нажали Shift
        if event.type == pygame.KEYDOWN and (event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT):
            shift = True
        # отпустили Shift
        if event.type == pygame.KEYUP and (event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT):
            shift = False
        # нажали кнопку мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            # если на экране надпись, то прячем ее
            if label.visible:
                label.visible = False
            # если на экране меню
            elif menu.visible:
                click_menu()
            # если на экране нет пули, то стреляем
            elif not bullet.visible:
                x1 = human.rect.x + Hand.SHOULDER_X
                y1 = human.rect.y + Hand.SHOULDER_Y
                x2 = event.pos[0]
                y2 = event.pos[1]
                bullet.red = human.hand.red
                bullet.start(x1, y1, x2, y2)
        # если на экране надпись и нажали пробел, то убираем надпись
        if label.visible and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            label.visible = False
        # ESC - заходим в меню
        if not menu.visible and not label.visible and event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            menu.visible = True
        # перемещение мышки в меню - раскрашиваем кнопки
        if event.type == pygame.MOUSEMOTION:
            menu.set_mouse(event.pos[0], event.pos[1])
            human.set_mouse(event.pos[0], event.pos[1])

    # рисуем надпись на экране
    if label.visible:
        screen.fill(pygame.Color('black'))
        label.draw(screen)
        pygame.display.flip()
        clock.tick(fps)
        continue

    # рисуем меню
    if menu.visible:
        screen.fill(pygame.Color('black'))
        menu.draw(screen)
        pygame.display.flip()
        clock.tick(fps)
        continue

    # запоминаем где был человек
    x = human.rect.x

    # смотрим нажатые клавиши
    keys = pygame.key.get_pressed()

    # перемещение человека
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

    # если вошел в стену, то возвращаем человека обратно
    if Helper.mask_collide_sprites(human, field.blocks):
        human.set_pos(x, human.rect.y)

    # пропуем опустить человека вниз
    try_down()

    # перемещаем пулю
    if bullet.visible:
        move_bullet()

    # телепортируем человека
    if red_portal.visible and blue_portal.visible:
        if Helper.mask_collide_sprites(human, red_portal.group):
            blue_portal.teleport(human)

    # если человек зашел в выход
    if field.exit.rect.contains(human.rect):
        if field.level == 4:
            load_level(1)
            label.text = "Поздравляю! Игра пройдена!"
            menu.visible = True
            menu.start = True
        else:
            load_level(field.level + 1)
        label.visible = True
        win_sound.play()

    # если упал, то начинаем уровень заново
    if human.rect.y > h:
        load_level(field.level)

    # рисуем поле, человека, порталы, пулю
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

# если начали игру, то автосохранение
if field.level > 0:
    save_game()

# выходим из PyGame
pygame.quit()
