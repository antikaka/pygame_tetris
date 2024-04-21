
import pygame as pg
import sys
import random


def t_shape(count, x, y):
    match count:
        case 1:
            t_rect1 = pg.Rect(x, y, 60, 20)
            t_rect2 = pg.Rect(x, y, 20, 40)

            t_rect2[0], t_rect2[1] = t_rect1[0] + 20, t_rect1[1] - 20
            if t_rect1[0] < 240:
                t_rect1[0] = 240
                t_rect2[0] = 260

            if t_rect1[0] > 500:
                t_rect1[0] = 500
                t_rect2[0] = 520
            x_fix = 0


        case 2:
            t_rect1 = pg.Rect(x, y, 60, 20)
            t_rect2 = pg.Rect(x, y, 20, 40)
            t_rect1[0], t_rect1[1], t_rect1[2], t_rect1[3] = t_rect1[0], t_rect1[1] - 40,  t_rect1[3], t_rect1[2]
            t_rect2[0], t_rect2[1], t_rect2[2], t_rect2[3] = t_rect2[0], t_rect2[1] - 20, t_rect2[3], t_rect2[2]
            if t_rect1[0] < 240:
                t_rect1[0] = 240
                t_rect2[0] = 240

            if t_rect1[0] > 520:
                t_rect1[0] = 520
                t_rect2[0] = 520
            x_fix = 0
        case 3:
            t_rect1 = pg.Rect(x, y, 60, 20)
            t_rect2 = pg.Rect(x, y, 20, 40)
            t_rect2[0], t_rect2[1] = t_rect1[0] + 20, t_rect1[1] - 20
            t_rect1[1] = t_rect1[1] - 20
            if t_rect1[0] < 240:
                t_rect1[0] = 240
                t_rect2[0] = 260

            if t_rect1[0] > 500:
                t_rect1[0] = 500
                t_rect2[0] = 520

            x_fix = 0
        case 4:
            t_rect1 = pg.Rect(x, y, 60, 20)
            t_rect2 = pg.Rect(x, y, 20, 40)
            t_rect1[0], t_rect1[1], t_rect1[2], t_rect1[3] = t_rect1[0] + 40, t_rect1[1] - 40, t_rect1[3], t_rect1[2]
            t_rect2[0], t_rect2[1], t_rect2[2], t_rect2[3] = t_rect2[0] + 20, t_rect2[1] - 20, t_rect2[3], t_rect2[2]
            if t_rect2[0] < 240:
                t_rect2[0] = 240
                t_rect1[0] = 260

            if t_rect1[0] > 540:
                t_rect1[0] = 540
                t_rect2[0] = 520
            x_fix = -40
        case _:
            t_rect1 = pg.Rect(x, y, 60, 20)
            t_rect2 = pg.Rect(x, y, 20, 40)
            t_rect2[0], t_rect2[1] = t_rect1[0] + 20, t_rect1[1] - 20
            x_fix = 0


    return t_rect1, t_rect2, x_fix

def z_shape(count, x, y):
    match count:
        case 1:
            t_rect1 = pg.Rect(x + 20, y - 20, 20, 40)
            t_rect2 = pg.Rect(x + 20, y - 20, 20, 40)
            t_rect2[0], t_rect2[1] = t_rect1[0] - 20, t_rect1[1] - 20
            if t_rect2[0] < 240:
                t_rect2[0] = 240
                t_rect1[0] = 260
            if t_rect1[0] > 540:
                t_rect1[0] = 540
                t_rect2[0] = 520
            x_fix = -20
        case 2:
            t_rect1 = pg.Rect(x + 20, y - 20, 20, 40)
            t_rect2 = pg.Rect(x + 20, y - 20, 20, 40)
            t_rect1[0], t_rect1[1], t_rect1[2], t_rect1[3] = t_rect1[0], t_rect1[1], t_rect1[3], t_rect1[2]
            t_rect2[0], t_rect2[1], t_rect2[2], t_rect2[3] = t_rect2[0] - 20, t_rect2[1] + 20, t_rect2[3], t_rect2[2]
            if t_rect2[0] < 240:
                t_rect2[0] = 240
                t_rect1[0] = 260

            if t_rect2[0] > 500:
                t_rect1[0] = 520
                t_rect2[0] = 500
            x_fix = -20
        case 3:
            t_rect1 = pg.Rect(x + 20, y - 20, 20, 40)
            t_rect2 = pg.Rect(x + 20, y - 20, 20, 40)
            t_rect2[0], t_rect2[1] = t_rect1[0] - 20, t_rect1[1] - 20
            if t_rect2[0] < 240:
                t_rect2[0] = 240
                t_rect1[0] = 260
            if t_rect1[0] > 540:
                t_rect1[0] = 540
                t_rect2[0] = 520
            x_fix = -20
        case 4:
            t_rect1 = pg.Rect(x + 20, y - 20, 20, 40)
            t_rect2 = pg.Rect(x + 20, y - 20, 20, 40)
            t_rect1[0], t_rect1[1], t_rect1[2], t_rect1[3] = t_rect1[0], t_rect1[1], t_rect1[3], t_rect1[2]
            t_rect2[0], t_rect2[1], t_rect2[2], t_rect2[3] = t_rect2[0] - 20, t_rect2[1] + 20, t_rect2[3], t_rect2[2]
            if t_rect2[0] < 240:
                t_rect2[0] = 240
                t_rect1[0] = 260

            if t_rect2[0] > 500:
                t_rect1[0] = 520
                t_rect2[0] = 500
            x_fix = -20
        case _:
            t_rect1 = pg.Rect(x + 20, y - 20, 20, 40)
            t_rect2 = pg.Rect(x + 20, y - 20, 20, 40)
            t_rect2[0], t_rect2[1] = t_rect1[0] + 20, t_rect1[1] - 20
            x_fix = -20
    return t_rect1, t_rect2, x_fix
def l_shape(count, x, y):
    match count:
        case 1:
            t_rect1 = pg.Rect(x + 20, y - 40, 20, 60)
            t_rect2 = pg.Rect(x + 20, y - 40, 40, 20)
            t_rect2[0], t_rect2[1] = t_rect1[0] - 20, t_rect1[1]
            if t_rect2[0] < 240:
                t_rect2[0] = 240
                t_rect1[0] = 260
            if t_rect1[0] > 540:
                t_rect1[0] = 540
                t_rect2[0] = 520
            x_fix = -20

        case 2:
            t_rect1 = pg.Rect(x + 20, y - 40, 20, 60)
            t_rect2 = pg.Rect(x + 20, y - 40, 40, 20)
            t_rect1[0], t_rect1[1], t_rect1[2], t_rect1[3] = t_rect1[0] - 20, t_rect1[1] + 40, t_rect1[3], t_rect1[2]
            t_rect2[0], t_rect2[1], t_rect2[2], t_rect2[3] = t_rect2[0] + 20, t_rect2[1] + 20, t_rect2[3], t_rect2[2]
            if t_rect1[0] < 240:
                t_rect1[0] = 240
                t_rect2[0] = 280
            if t_rect1[0] > 500:
                t_rect1[0] = 500
                t_rect2[0] = 540
            x_fix = 0
        case 3:
            t_rect1 = pg.Rect(x + 20, y - 40, 20, 60)
            t_rect2 = pg.Rect(x + 20, y - 40, 40, 20)
            t_rect1[0] = t_rect1[0] - 20
            t_rect2[0], t_rect2[1] = t_rect1[0], t_rect1[1] + 40
            if t_rect1[0] < 240:
                t_rect1[0] = 240
                t_rect2[0] = 240
            if t_rect2[0] > 520:
                t_rect2[0] = 520
                t_rect1[0] = 520
            x_fix = 0
        case 4:
            t_rect1 = pg.Rect(x + 20, y - 40, 20, 60)
            t_rect2 = pg.Rect(x + 20, y - 40, 40, 20)
            t_rect1[0], t_rect1[1], t_rect1[2], t_rect1[3] = t_rect1[0] - 20, t_rect1[1] + 20, t_rect1[3], t_rect1[2]
            t_rect2[0], t_rect2[1], t_rect2[2], t_rect2[3] = t_rect2[0] - 20, t_rect2[1] + 20, t_rect2[3], t_rect2[2]
            if t_rect1[0] < 240:
                t_rect1[0] = 240
                t_rect2[0] = 240
            if t_rect2[0] > 500:
                t_rect2[0] = 500
                t_rect1[0] = 500
            x_fix = 0
        case _:
            t_rect1 = pg.Rect(x + 20, y - 20, 20, 40)
            t_rect2 = pg.Rect(x + 20, y - 20, 20, 40)
            t_rect2[0], t_rect2[1] = t_rect1[0] + 20, t_rect1[1] - 20
            x_fix = 0
    return t_rect1, t_rect2, x_fix

def sq_shape(count, x, y):
    match count:
        case 1:
            t_rect1 = pg.Rect(x, y - 20, 40, 40)
            if t_rect1[0] < 240:
                t_rect1[0] = 240
            if t_rect1[0] > 520:
                t_rect1[0] = 520
            x_fix = 0
        case 2:
            t_rect1 = pg.Rect(x, y - 20, 40, 40)
            if t_rect1[0] < 240:
                t_rect1[0] = 240
            if t_rect1[0] > 520:
                t_rect1[0] = 520
            x_fix = 0
        case 3:
            t_rect1 = pg.Rect(x, y - 20, 40, 40)
            if t_rect1[0] < 240:
                t_rect1[0] = 240
            if t_rect1[0] > 520:
                t_rect1[0] = 520
            x_fix = 0
        case 4:
            t_rect1 = pg.Rect(x, y - 20, 40, 40)
            if t_rect1[0] < 240:
                t_rect1[0] = 240
            if t_rect1[0] > 520:
                t_rect1[0] = 520
            x_fix = 0
        case _:
            t_rect1 = pg.Rect(x, y - 20, 40, 40)
            x_fix = 0
    t_rect2 = pg.Rect(0, 0, 0, 0)
    return t_rect1, t_rect2, x_fix


def i_shape(count, x, y):
    match count:
        case 1:
            t_rect1 = pg.Rect(x + 20, y - 40, 20, 80)
            if t_rect1[0] < 240:
                t_rect1[0] = 240
            if t_rect1[0] > 540:
                t_rect1[0] = 540
            x_fix = -20
        case 2:
            t_rect1 = pg.Rect(x + 20, y - 40, 20, 80)
            t_rect1[0], t_rect1[1], t_rect1[2], t_rect1[3] = t_rect1[0] - 20, t_rect1[1] + 20, t_rect1[3], t_rect1[2]
            if t_rect1[0] < 240:
                t_rect1[0] = 240
            if t_rect1[0] > 480:
                t_rect1[0] = 480
            x_fix = 0
        case 3:
            t_rect1 = pg.Rect(x + 20, y - 40, 20, 80)

            if t_rect1[0] < 240:
                t_rect1[0] = 240
            if t_rect1[0] > 540:
                t_rect1[0] = 540
            x_fix = -20
        case 4:
            t_rect1 = pg.Rect(x + 20, y - 40, 20, 80)
            t_rect1[0], t_rect1[1], t_rect1[2], t_rect1[3] = t_rect1[0] - 20, t_rect1[1] + 20, t_rect1[3], t_rect1[2]
            if t_rect1[0] < 240:
                t_rect1[0] = 240
            if t_rect1[0] > 480:
                t_rect1[0] = 480
            x_fix = 0
        case _:
            t_rect1 = pg.Rect(x + 20, y - 40, 20, 80)
            x_fix = 0
    t_rect2 = pg.Rect(0, 0, 0, 0)
    return t_rect1, t_rect2, x_fix


def left_right(t_rect1, t_rect2):
    obj_l = []
    obj_r = []
    solo_rect = False
    rect1_h = t_rect1[3]
    rect2_h = t_rect2[3]
    if rect2_h < 10:
        solo_rect = True

    x = t_rect1[0]
    y = t_rect1[1] + 20

    for num in range(rect1_h // 20):
        obj_l.append(pg.Rect(x - 20, y + (20 * num), 20, 20))
        obj_r.append(pg.Rect(x + t_rect1[2], y + (20 * num), 20, 20))

    x = t_rect2[0]
    y = t_rect2[1] + 20

    if not solo_rect:
        for num in range(rect2_h // 20):
            obj_l.append(pg.Rect(x - 20, y + (20 * num), 20, 20))
            obj_r.append(pg.Rect(x + t_rect2[2], y + (20 * num), 20, 20))

    return obj_l, obj_r


def drop(x, y):
    y += 20
    return x, y



pg.init()

width, height = 800, 600
screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()
def_font = pg.font.get_default_font()
font = pg.font.Font(def_font, 10)

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
magenta = (255, 0, 255)
cyan = (0, 255, 255)

colors = [red, blue, green, yellow, magenta, cyan]

random_color = random.choice(colors)


started = False

start_pos = (380, 20)

piece_list = []

piece_x, piece_y = start_pos[0], start_pos[1]

count = 1
piece_count = 0

line1 = pg.Rect(240, 0, 2, 580)
left = pg.Rect(0, 0, 240, 580)
line2 = pg.Rect(559, 0, 2, 580)
right = pg.Rect(560, 0, 240, 580)
line3 = pg.Rect(240, 580, 320, 2)
bottom = pg.Rect(240, 579, 320, 40)

shape_list = [sq_shape, t_shape, z_shape, i_shape, l_shape]
random_shape = random.choice(shape_list)

go_left = True
go_right = True
new_piece = False

speed = 3
pg.key.set_repeat(500, 50)

playfield_closed = []
while True:
    clock.tick(speed)

    r_x_orig, r_y, r_width, r_height = 240, 0, 20, 20
    playfield_list = []

    screen.fill((255, 255, 255))

    for num in range(29):
        r_x = r_x_orig
        for num in range(16):
            rect = pg.Rect(r_x, r_y, r_width, r_height)
            playfield_list.append(rect)
            pg.draw.rect(screen, (120, 120, 120), rect, 1)
            r_x += 20
        r_y += 20

    pg.draw.rect(screen, (0, 0, 0), line1)
    pg.draw.rect(screen, (0, 0, 0), line2)
    pg.draw.rect(screen, (0, 0, 0), line3)

    start_button = pg.Rect(0, 10, 20, 20)
    pg.draw.rect(screen, (255, 0, 0), start_button)



    playfield_active = []
    for sq_c in playfield_closed:
        for sq in playfield_list:
            if sq not in playfield_closed and sq_c[2][0] == sq[0] and sq_c[2][1] - 20 == sq[1]:
                playfield_active.append(sq)


    playfield_active_bottoms = []
    for sq in playfield_active:
        active_bottom = pg.Rect(sq[0], sq.bottom - 1, 20, 2)
        playfield_active_bottoms.append(active_bottom)

    go_right = True
    go_left = True
    if len(playfield_closed) > 1:
        obj_l, obj_r = left_right(t_rect1, t_rect2)

        for sq in obj_l:
            pg.draw.rect(screen, (255, 0, 0), sq, 1)
        for sq in obj_r:
            pg.draw.rect(screen, (255, 0, 0), sq, 1)


        for sq in obj_l:
            for sq_c in playfield_closed:
                if sq == sq_c[2]:
                    go_left = False
                    break


        for sq in obj_r:
            for sq_c in playfield_closed:
                if sq == sq_c[2]:
                    go_right = False
                    break

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT and go_left:
                piece_x -= 20
                go_left = False
            if event.key == pg.K_RIGHT and go_right:
                piece_x += 20
                go_right = False
            if event.key == pg.K_DOWN:
                speed = 30
        if event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                print("SPACE")
                count += 1
            if event.key == pg.K_DOWN:
                while speed > 3:
                    speed -= 1



    if count > 4:
        count = 1
    elif count < 1:
        count = 4


    if new_piece:
        for sq in playfield_list:
            for piece in piece_list:
                if sq.colliderect(piece[2]):
                    playfield_closed.append((screen, piece[1], sq))
        piece_list.clear()
        print(piece_list)
        random_color = random.choice(colors)

        new_piece = False

    if piece_y > 40:
        if (bottom.colliderect(t_rect1) or bottom.colliderect(t_rect2)):
            print("collide")
            piece_count += 1
            new_piece = True
            piece_list.append((screen, random_color, t_rect1))
            piece_list.append((screen, random_color, t_rect2))
            random_shape = random.choice(shape_list)
            piece_x, piece_y = start_pos[0], start_pos[1]
            t_rect1, t_rect2, x_fix = random_shape(count, piece_x, piece_y)





    for bottom_act in playfield_active_bottoms:
        if bottom_act.colliderect(t_rect1) or bottom_act.colliderect(t_rect2):
            print("collide2")
            piece_count += 1
            new_piece = True
            piece_list.append((screen, random_color, t_rect1))
            piece_list.append((screen, random_color, t_rect2))
            random_shape = random.choice(shape_list)
            piece_x, piece_y = start_pos[0], start_pos[1]
            t_rect1, t_rect2, x_fix = random_shape(count, piece_x, piece_y)

    t_rect1, t_rect2, x_fix = random_shape(count, piece_x, piece_y)



    pg.draw.rect(screen, random_color, t_rect1)
    if t_rect2[2] > 1:
        pg.draw.rect(screen, random_color, t_rect2)

    for sq in playfield_closed:
        pg.draw.rect(*sq)
        pg.draw.rect(screen, (0, 0, 0), sq[2], 1)

    piece_x = t_rect1[0] + x_fix
    piece_x, piece_y = drop(piece_x, piece_y)


    pg.display.flip()

