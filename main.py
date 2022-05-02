import pygame
import random
import time
from win32api import GetSystemMetrics
from pypresence import Presence
pygame.init()

dc = Presence('969947839704731758')
dc.connect()
dc.update(state='Solving a Wordle...', large_image='logo', start=int(time.time()))

run = True

t = pygame.time.Clock()

# colours
G0 = (57, 93, 36)
G1 = (74, 117, 44)
G2 = (87, 138, 52)
G3 = (162, 209, 73)
G4 = (190, 245, 105)
W = (255, 255, 255)
R = (221, 46, 67)
B0 = (0, 0, 0)
B1 = (7, 10, 15)
B2 = (18, 26, 37)
B3 = (35, 44, 56)
B4 = (61, 71, 84)
Y = (255, 203, 77)
BL1 = (27, 62, 161)
BL2 = (79, 118, 248)

# sounds
game_over = pygame.mixer.Sound('assets/sounds/game_over.wav')
green_let = pygame.mixer.Sound('assets/sounds/green_let.wav')
grey_let = pygame.mixer.Sound('assets/sounds/grey_let.wav')
hint = pygame.mixer.Sound('assets/sounds/hint.wav')
insert_let = pygame.mixer.Sound('assets/sounds/insert_let.wav')
music = pygame.mixer.Sound('assets/sounds/music.mp3')
no_enter = pygame.mixer.Sound('assets/sounds/no_enter.wav')
remove_let = pygame.mixer.Sound('assets/sounds/remove_let.wav')
round_start = pygame.mixer.Sound('assets/sounds/round_start.wav')
vanolex_jingle = pygame.mixer.Sound('assets/sounds/vanolex_jingle.wav')
yellow_let = pygame.mixer.Sound('assets/sounds/yellow_let.wav')

gs = 0
mx, my = 0, 0
sw, sh = 850, 950
s = 1
full_screen = False
anim_offset = [0, 0, 0, 0, 0]
hover_btn = 0
cursor_pos = 0
notfour = True
letreveal = False

pygame.display.set_caption('Wordle')
pygame.display.set_icon(pygame.image.load('assets/textures/logo.png'))
sc = pygame.display.set_mode((sw, sh), pygame.RESIZABLE)

ttl_fnt = pygame.font.Font('assets/fonts/Font1.otf', 50)
stl_fnt = pygame.font.Font('assets/fonts/Font1.otf', int(40*s))
let_fnt = pygame.font.Font('assets/fonts/Font1.otf', int(80*s))
ver_fnt = pygame.font.Font('assets/fonts/Font2.ttf', int(25*s))
vnx_fnt = pygame.font.Font('assets/fonts/Font3.ttf', int(80*s))
wordle_txt = ttl_fnt.render('WORDLE', True, W)

rcg = [random.randint(50, 125), random.randint(50, 125), random.randint(50, 125), random.randint(50, 125),
       random.randint(50, 125), random.randint(50, 125), random.randint(50, 125), random.randint(50, 125),
       random.randint(50, 125), random.randint(50, 125), random.randint(50, 125), random.randint(50, 125),
       random.randint(50, 125), random.randint(50, 125)]
vanolex_jingle.play()
for k in range(90):
    sc.fill(B1)
    vnx_fnt = pygame.font.Font('assets/fonts/Font3.ttf', int(80 * s * (k / 180 + 1)))
    sc.blit(vnx_fnt.render('VANOLEX', True, W), vnx_fnt.render('VANOLEX', True, W).get_rect(
        center=(sw // 2, sh // 2-25*s-k/10*s)))
    sc.blit(stl_fnt.render('PRESENTS', True, W), stl_fnt.render('PRESENTS', True, W).get_rect(
        center=(sw // 2, sh // 2+50*s)))
    logo_overlay = pygame.Surface((sw, sh))
    if k < 20:
        logo_overlay.set_alpha(int(255 - k*12.75))
        logo_overlay.fill(B1)
        sc.blit(logo_overlay, (0, 0))
    elif k > 50:
        logo_overlay.set_alpha(int((k - 50)*12.75))
        logo_overlay.fill(B1)
        sc.blit(logo_overlay, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.VIDEORESIZE:
            sw, sh = sc.get_width(), sc.get_height()
            s = (sh - 80) / 870
            if sw < 850 * s:
                sw = 850 * s
            if sw < 300:
                sw = 300
            if sh < 300:
                sh = 300
            s = (sh - 80) / 870
            stl_fnt = pygame.font.Font('assets/fonts/Font1.otf', int(40 * s))
            let_fnt = pygame.font.Font('assets/fonts/Font1.otf', int(80 * s))
            ver_fnt = pygame.font.Font('assets/fonts/Font2.ttf', int(20 * s))
            sw, sh = sw // 1, sh // 1
            fh, fw = sw - 20, sh - 70
            sc = pygame.display.set_mode((sw, sh), pygame.RESIZABLE)
        if event.type == pygame.KEYDOWN:
            if event.key == 1073741892:
                if full_screen:
                    sw, sh = 550, 950
                    s = 1
                    stl_fnt = pygame.font.Font('assets/fonts/Font1.otf', int(40 * s))
                    let_fnt = pygame.font.Font('assets/font1.otf', int(80 * s))
                    ver_fnt = pygame.font.Font('assets/font2.ttf', int(20 * s))
                    fh, fw = sw - 20, sh - 70
                    sc = pygame.display.set_mode((sw, sh), pygame.RESIZABLE)
                    full_screen = False
                else:
                    sw, sh = GetSystemMetrics(0), GetSystemMetrics(1)
                    s = (sh - 80) / 870
                    stl_fnt = pygame.font.Font('assets/fonts/Font1.otf', int(40 * s))
                    let_fnt = pygame.font.Font('assets/fonts/Font1.otf', int(80 * s))
                    ver_fnt = pygame.font.Font('assets/fonts/Font2.ttf', int(20 * s))
                    sw, sh = sw // 1, sh // 1
                    fh, fw = sw - 20, sh - 70
                    sc = pygame.display.set_mode((sw, sh), pygame.FULLSCREEN)
                    full_screen = True
    pygame.display.update()
    t.tick(30)
del logo_overlay
let_fnt = pygame.font.Font('assets/fonts/Font1.otf', int(80*s))


for k in range(110):
    sc.fill(G2)
    pygame.draw.rect(sc, G1, (0, sh//2 + 80 * s - k*2*s, sw, sh//2 + 200 * s))
    for k1 in range(int(sw//20)):
        pygame.draw.circle(sc, G1, (50*s + 80*k1*s, sh//2 + 60*s - k*2*s), rcg[k1 % len(rcg)])
        pygame.draw.circle(sc, G1, (-25 * s + 60 * k1 * s - rcg[k1 % len(rcg)]*s,
                           sh // 2 - rcg[k1 % len(rcg)] * s * 3 - k*s),
                           rcg[k1 % len(rcg)]//4)
    if k < 40:
        if 5 <= k < 10:
            sc.blit(let_fnt.render('W', True, W),
                    let_fnt.render('W', True, W).get_rect(center=(sw // 2 - 134.5 * s, sh // 2 + 90 * s - (k-4) * 20 * s)))
        elif 10 <= k < 15:
            sc.blit(let_fnt.render('W', True, W),
                    let_fnt.render('W', True, W).get_rect(center=(sw // 2 - 134.5 * s, sh // 2)))
            sc.blit(let_fnt.render('O', True, W),
                    let_fnt.render('O', True, W).get_rect(center=(sw // 2 - 62.5 * s, sh // 2 + 90 * s - (k-9) * 20 * s)))
        elif 15 <= k < 20:
            sc.blit(let_fnt.render('W', True, W),
                    let_fnt.render('W', True, W).get_rect(center=(sw // 2 - 134.5 * s, sh // 2)))
            sc.blit(let_fnt.render('O', True, W),
                    let_fnt.render('O', True, W).get_rect(center=(sw // 2 - 62.5 * s, sh // 2)))
            sc.blit(let_fnt.render('R', True, W),
                    let_fnt.render('R', True, W).get_rect(center=(sw // 2 - 2 * s, sh // 2 + 90 * s - (k-14) * 20 * s)))
        elif 20 <= k < 25:
            sc.blit(let_fnt.render('W', True, W),
                    let_fnt.render('W', True, W).get_rect(center=(sw // 2 - 134.5 * s, sh // 2)))
            sc.blit(let_fnt.render('O', True, W),
                    let_fnt.render('O', True, W).get_rect(center=(sw // 2 - 62.5 * s, sh // 2)))
            sc.blit(let_fnt.render('R', True, W),
                    let_fnt.render('R', True, W).get_rect(center=(sw // 2 - 2 * s, sh // 2)))
            sc.blit(let_fnt.render('D', True, W),
                    let_fnt.render('D', True, W).get_rect(center=(sw // 2 + 56.5 * s, sh // 2 + 90 * s-(k-19) * 20 * s)))
        elif 25 <= k < 30:
            sc.blit(let_fnt.render('W', True, W),
                    let_fnt.render('W', True, W).get_rect(center=(sw // 2 - 134.5 * s, sh // 2)))
            sc.blit(let_fnt.render('O', True, W),
                    let_fnt.render('O', True, W).get_rect(center=(sw // 2 - 62.5 * s, sh // 2)))
            sc.blit(let_fnt.render('R', True, W),
                    let_fnt.render('R', True, W).get_rect(center=(sw // 2 - 2 * s, sh // 2)))
            sc.blit(let_fnt.render('D', True, W),
                    let_fnt.render('D', True, W).get_rect(center=(sw // 2 + 56.5 * s, sh // 2)))
            sc.blit(let_fnt.render('L', True, W),
                    let_fnt.render('L', True, W).get_rect(center=(sw // 2 + 107 * s, sh // 2 + 90 * s-(k-24) * 20 * s)))
        elif 30 <= k < 35:
            sc.blit(let_fnt.render('W', True, W),
                    let_fnt.render('W', True, W).get_rect(center=(sw // 2 - 134.5 * s, sh // 2)))
            sc.blit(let_fnt.render('O', True, W),
                    let_fnt.render('O', True, W).get_rect(center=(sw // 2 - 62.5 * s, sh // 2)))
            sc.blit(let_fnt.render('R', True, W),
                    let_fnt.render('R', True, W).get_rect(center=(sw // 2 - 2 * s, sh // 2)))
            sc.blit(let_fnt.render('D', True, W),
                    let_fnt.render('D', True, W).get_rect(center=(sw // 2 + 56.5 * s, sh // 2)))
            sc.blit(let_fnt.render('L', True, W),
                    let_fnt.render('L', True, W).get_rect(center=(sw // 2 + 107 * s, sh // 2)))
            sc.blit(let_fnt.render('E', True, W),
                    let_fnt.render('E', True, W).get_rect(center=(sw // 2 + 151.5 * s, sh // 2 + 90*s-(k-29) * 20 * s)))
        pygame.draw.rect(sc, G1, (sw // 2 - 200 * s, sh // 2 + 40 * s, 400, sh // 2))
    if k < 90:
        pygame.draw.rect(sc, W, (sw // 2 - 90 * s, sh - 90 * s, k*2*s, 10 * s), border_radius=int(5 * s))
    else:
        pygame.draw.rect(sc, W, (sw // 2 - 90 * s, sh - 90 * s, 180*s, 10 * s), border_radius=int(5 * s))
    pygame.draw.rect(sc, W, (sw//2 - 100*s, sh - 100*s, 200*s, 30*s), 5, border_radius=int(15*s))
    if 35 <= k:
        if 40 <= k <= 50:
            let_fnt = pygame.font.Font('assets/fonts/Font1.otf', int(80 * s + 4*(k-40)*s))
        sc.blit(let_fnt.render('WORDLE', True, W), let_fnt.render('WORDLE', True, W).get_rect(
            center=(sw//2, sh//2)))
    if k < 90:
        sc.blit(ver_fnt.render('Loading...' + str(k) + '%', True, W), ver_fnt.render('Loading...' + str(k) + '%',
            True, W).get_rect(center=(sw // 2, sh - int(120 * s))))
    else:
        sc.blit(ver_fnt.render('Loading... 100%', True, W),
            ver_fnt.render('Loading... 100%', True, W).get_rect(
                center=(sw // 2, sh - int(120 * s))))
    sc.blit(ver_fnt.render('Version 1.5r-02', True, G0),
            ver_fnt.render('Version 1.5r-02', True, G0).get_rect(center=(sw // 2, sh - int(25 * s))))
    pygame.display.update()

    if 5 <= k <= 30 and k % 5 == 0:
        insert_let.play()

    if k == 40:
        green_let.play()

    for event in pygame.event.get():
        if event.type == pygame.VIDEORESIZE:
            sw, sh = sc.get_width(), sc.get_height()
            s = (sh - 80) / 870
            if sw < 850 * s:
                sw = 850 * s
            if sw < 300:
                sw = 300
            if sh < 300:
                sh = 300
            s = (sh - 80) / 870
            stl_fnt = pygame.font.Font('assets/fonts/Font1.otf', int(40 * s))
            if k < 40:
                let_fnt = pygame.font.Font('assets/fonts/Font1.otf', int(80*s))
            elif k > 60:
                let_fnt = pygame.font.Font('assets/fonts/Font1.otf', int(120 * s))
            ver_fnt = pygame.font.Font('assets/fonts/Font2.ttf', int(20 * s))
            sw, sh = sw // 1, sh // 1
            fh, fw = sw - 20, sh - 70
            sc = pygame.display.set_mode((sw, sh), pygame.RESIZABLE)
        if event.type == pygame.KEYDOWN:
            if event.key == 1073741892:
                if full_screen:
                    sw, sh = 550, 950
                    s = 1
                    stl_fnt = pygame.font.Font('assets/fonts/Font1.otf', int(40 * s))
                    if k < 40:
                        let_fnt = pygame.font.Font('assets/fonts/Font1.otf', int(80 * s))
                    elif k > 60:
                        let_fnt = pygame.font.Font('assets/fonts/Font1.otf', int(160 * s))
                    ver_fnt = pygame.font.Font('assets/font2.ttf', int(20 * s))
                    fh, fw = sw - 20, sh - 70
                    sc = pygame.display.set_mode((sw, sh), pygame.RESIZABLE)
                    full_screen = False
                else:
                    sw, sh = GetSystemMetrics(0), GetSystemMetrics(1)
                    s = (sh - 80) / 870
                    stl_fnt = pygame.font.Font('assets/fonts/Font1.otf', int(40 * s))
                    if k < 40:
                        let_fnt = pygame.font.Font('assets/fonts/Font1.otf', int(80 * s))
                    elif k > 60:
                        let_fnt = pygame.font.Font('assets/fonts/Font1.otf', int(160 * s))
                    ver_fnt = pygame.font.Font('assets/fonts/Font2.ttf', int(20 * s))
                    sw, sh = sw // 1, sh // 1
                    fh, fw = sw - 20, sh - 70
                    sc = pygame.display.set_mode((sw, sh), pygame.FULLSCREEN)
                    full_screen = True
    pygame.display.update()
    t.tick(30)

wordlist = open('assets/words/5eng.txt').read()
word = list(random.choice(list(open('assets/words/5eng.txt'))))
word.pop()

cline = ['null'] * 5
let = []
cc = [W]*5 + [G4]*25
pcc = []
ccc = []

let_fnt = pygame.font.Font('assets/fonts/Font1.otf', int(80*s))


def draw_field(x, y, n):
    pygame.draw.rect(sc, cc[n], (x, y, 90 * s, 110 * s), border_radius=int(10*s))

    if cc[n] == W:
        if cursor_pos == n % 5 and not letreveal:
            pygame.draw.rect(sc, G3, (x, y, 90 * s, 110 * s), width=int(5*s), border_radius=int(10 * s))
            pygame.draw.rect(sc, cc[n], (x-5*s, y-5*s, 100 * s, 120 * s), width=int(5 * s), border_radius=int(15 * s))
        if cline[n % 5] != 'null':
            sc.blit(let_fnt.render(cline[n % 5], True, B1),
                    let_fnt.render(cline[n % 5], True, B1).get_rect(center=(x+45*s, y + 55*s)))
    if len(let) <= n < len(let) + 5 and cc[n] != W:
        sc.blit(let_fnt.render(cline[n % 5], True, W),
                let_fnt.render(cline[n % 5], True, W).get_rect(center=(x + 45 * s, y + 55 * s)))

    if len(let) > n:
        sc.blit(let_fnt.render(let[n], True, W), let_fnt.render(let[n], True, W).get_rect(
            center=(x + 45*s, y + 55*s)))


def sc_draw_game():
    sc.fill(G2)
    pygame.draw.rect(sc, G1, (0, 0, sw, 60))

    if 1 <= gs <= 3:
        pygame.draw.rect(sc, B2, (sw//2 - 265*s, 70, 530*s, sh-80), border_radius=int(20*s))

        if gs == 1:
            pygame.draw.rect(sc, G2, (sw // 2 - 245 * s, 70 + 20 * s, 490 * s, 110 * s), border_radius=int(10*s))

            sc.blit(let_fnt.render('YOU WON!', True, W), let_fnt.render('YOU WON!', True, W).get_rect(
                center=(sw//2, 70 + 75*s)))
            sc.blit(stl_fnt.render('CONGRATULATIONS!', True, W), stl_fnt.render('CONGRATULATIONS', True, W).get_rect(
                center=(sw // 2, 70 + 200 * s)))
        elif gs == 2:
            pygame.draw.rect(sc, R, (sw // 2 - 245 * s, 70 + 20 * s, 490 * s, 110 * s), border_radius=int(10*s))

            sc.blit(let_fnt.render('YOU LOST!', True, W), let_fnt.render('YOU LOST!', True, W).get_rect(
                center=(sw//2, 70 + 75*s)))
            sc.blit(stl_fnt.render('THE WORD WAS:', True, W), stl_fnt.render('THE WORD WAS:', True, W).get_rect(
                center=(sw // 2, 70 + 200 * s)))
        elif gs == 3:
            pygame.draw.rect(sc, BL1, (sw // 2 - 245 * s, 70 + 20 * s, 490 * s, 110 * s), border_radius=int(10*s))

            sc.blit(let_fnt.render('GAVE UP!', True, W), let_fnt.render('GAVE UP!', True, W).get_rect(
                center=(sw//2, 70 + 75*s)))
            sc.blit(stl_fnt.render('THE WORD WAS:', True, W), stl_fnt.render('THE WORD WAS:', True, W).get_rect(
                center=(sw // 2, 70 + 200 * s)))

        for k in range(5):
            pygame.draw.rect(sc, G1, (sw // 2 - 245*s + 100*k*s, 70 + 260 * s, 90 * s, 110 * s),
                             border_radius=int(10*s))
            sc.blit(let_fnt.render(word[k], True, W),
                    let_fnt.render(word[k], True, W).get_rect(center=(sw // 2 - 245*s + 100*k*s + 45*s, 70 + 315 * s)))

        for k in range(len(let)):
            if cc[k] == B2:
                sc.blit(stl_fnt.render(let[k], True, W), stl_fnt.render(let[k], True, W).get_rect(
                            center=(sw // 2 - 60 * s + 30 * (k % 5) * s, 70 + 425 * s + k//5 * 45 * s)))
            else:
                sc.blit(stl_fnt.render(let[k], True, cc[k]), stl_fnt.render(let[k], True, W).get_rect(
                    center=(sw // 2 - 60 * s + 30 * (k % 5) * s, 70 + 425 * s + k // 5 * 45 * s)))

    else:
        pygame.draw.rect(sc, G3, (sw//2 - 265*s, 70, 530*s, sh-80), border_radius=int(20*s))

        for k in range(6):
            if anim_offset == [0, 0, 0, 0, 0] or len(let)//5 != k:
                draw_field(sw // 2 - 245*s, 70 + 20*s + k*120*s, 0 + k*5)
                draw_field(sw // 2 - 145*s, 70 + 20*s + k*120*s, 1 + k*5)
                draw_field(sw // 2 - 45*s, 70 + 20*s + k*120*s, 2 + k*5)
                draw_field(sw // 2 + 55*s, 70 + 20*s + k*120*s, 3 + k*5)
                draw_field(sw // 2 + 155*s, 70 + 20*s + k*120*s, 4 + k*5)
            else:
                draw_field(sw // 2 - 245 * s, 70 + 20 * s + k * 120 * s - anim_offset[0]*s, 0 + k * 5)
                draw_field(sw // 2 - 145 * s, 70 + 20 * s + k * 120 * s - anim_offset[1]*s, 1 + k * 5)
                draw_field(sw // 2 - 45 * s, 70 + 20 * s + k * 120 * s - anim_offset[2]*s, 2 + k * 5)
                draw_field(sw // 2 + 55 * s, 70 + 20 * s + k * 120 * s - anim_offset[3]*s, 3 + k * 5)
                draw_field(sw // 2 + 155 * s, 70 + 20 * s + k * 120 * s - anim_offset[4]*s, 4 + k * 5)

    pygame.draw.rect(sc, B3, (sw // 2 - 245 * s, 70 + 740 * s, 490 * s, 110 * s), border_radius=int(15 * s))
    if hover_btn == 1:
        pygame.draw.rect(sc, G1, (sw // 2 - 235 * s, 70 + 750 * s, 230 * s, 90 * s), border_radius=int(20 * s))
    else:
        pygame.draw.rect(sc, G2, (sw // 2 - 235 * s, 70 + 750 * s, 230 * s, 90 * s), border_radius=int(20 * s))

    if hover_btn == 2:
        pygame.draw.rect(sc, G1, (sw // 2 + 5 * s, 70 + 750 * s, 230 * s, 90 * s), border_radius=int(20 * s))
    else:
        pygame.draw.rect(sc, G2, (sw // 2 + 5 * s, 70 + 750 * s, 230 * s, 90 * s), border_radius=int(20 * s))

    if gs == 0:
        sc.blit(stl_fnt.render('GIVE UP', True, W), stl_fnt.render('GIVE UP', True, W).get_rect(
            center=(sw // 2 - 120*s, 70 + 795*s)))
    else:
        sc.blit(stl_fnt.render('RETRY', True, W), stl_fnt.render('RETRY', True, W).get_rect(
            center=(sw // 2 - 120*s, 70 + 795*s)))
    sc.blit(stl_fnt.render('QUIT', True, W), stl_fnt.render('QUIT', True, W).get_rect(
        center=(sw // 2 + 120 * s, 70 + 795 * s)))

    sc.blit(wordle_txt, wordle_txt.get_rect(center=(sw//2, 30)))
    pygame.display.update()


sc_draw_game()
round_start.play()


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.VIDEORESIZE:
            sw, sh = sc.get_width(), sc.get_height()
            s = (sh-80)/870
            if sw < 850*s:
                sw = 850*s
            if sw < 300:
                sw = 300
            if sh < 300:
                sh = 300
            s = (sh-80) / 870
            stl_fnt = pygame.font.Font('assets/fonts/Font1.otf', int(40 * s))
            let_fnt = pygame.font.Font('assets/fonts/Font1.otf', int(80 * s))
            ver_fnt = pygame.font.Font('assets/fonts/Font2.ttf', int(20 * s))
            sw, sh = sw//1, sh//1
            fh, fw = sw - 20, sh - 70
            sc = pygame.display.set_mode((sw, sh), pygame.RESIZABLE)
            sc_draw_game()

        if event.type == pygame.KEYDOWN:
            if event.key == 1073741892:
                if full_screen:
                    sw, sh = 550, 950
                    s = 1
                    stl_fnt = pygame.font.Font('assets/fonts/Font1.otf', int(40 * s))
                    let_fnt = pygame.font.Font('assets/fonts/Font1.otf', int(80 * s))
                    ver_fnt = pygame.font.Font('assets/fonts/Font2.ttf', int(20 * s))
                    fh, fw = sw - 20, sh - 70
                    sc = pygame.display.set_mode((sw, sh), pygame.RESIZABLE)
                    sc_draw_game()
                    full_screen = False
                else:
                    sw, sh = GetSystemMetrics(0), GetSystemMetrics(1)
                    s = (sh - 80) / 870
                    stl_fnt = pygame.font.Font('assets/fonts/Font1.otf', int(40 * s))
                    let_fnt = pygame.font.Font('assets/fonts/Font1.otf', int(80 * s))
                    ver_fnt = pygame.font.Font('assets/fonts/Font2.ttf', int(20 * s))
                    sw, sh = sw // 1, sh // 1
                    fh, fw = sw - 20, sh - 70
                    sc = pygame.display.set_mode((sw, sh), pygame.FULLSCREEN | pygame.NOFRAME)
                    sc_draw_game()
                    full_screen = True
            if 97 <= event.key <= 122 and cursor_pos < 5 and (gs == 0 or gs == 4):  # a-z
                cline[cursor_pos] = chr(event.key)
                if cursor_pos != 4:
                    notfour = True
                    cursor_pos += 1
                else:
                    notfour = False
                insert_let.play()
                for k in range(5):
                    if notfour:
                        anim_offset = [0] * (cursor_pos-1) + [k*2 + 1] + [0] * (5 - cursor_pos)
                    else:
                        anim_offset = [0] * cursor_pos + [k * 2 + 1] + [0] * (4 - cursor_pos)
                    sc_draw_game()
                    t.tick(60)
                for k in range(5):
                    if notfour:
                        anim_offset = [0] * (cursor_pos-1) + [9 - k*2] + [0] * (5 - cursor_pos)
                    else:
                        anim_offset = [0] * cursor_pos + [9 - k * 2] + [0] * (4 - cursor_pos)
                    sc_draw_game()
                    t.tick(60)
                anim_offset = [0] * 5
            if event.key == 8 and (gs == 0 or gs == 4):  # delete
                remove_let.play()
                if cline[cursor_pos] == 'null':
                    if cursor_pos != 0:
                        cursor_pos -= 1
                        cline[cursor_pos] = 'null'
                else:
                    cline[cursor_pos] = 'null'
                    if cursor_pos != 0 and cursor_pos != 4:
                        cursor_pos -= 1
                for k in range(5):
                    anim_offset = [0] * cursor_pos + [-k*2 - 1] + [0] * (4 - cursor_pos)
                    sc_draw_game()
                    t.tick(60)
                for k in range(5):
                    anim_offset = [0] * cursor_pos + [k*2-9] + [0] * (4 - cursor_pos)
                    sc_draw_game()
                    t.tick(60)
                anim_offset = [0] * 5
            if event.key == 13 and (gs == 0 or gs == 4):  # enter
                if cline == word:
                    letreveal = True
                    for k1 in range(5):
                        cc = pcc + [G1] * (k1+1) + [W] * (4-k1) + [G4] * (30 - len(pcc))
                        green_let.play()
                        for k in range(5):
                            anim_offset = [0]*k1 + [k*2+1] + [0]*(4-k1)
                            sc_draw_game()
                            t.tick(45)
                        for k in range(5):
                            anim_offset = [0] * k1 + [9 - k*2] + [0] * (4 - k1)
                            sc_draw_game()
                            t.tick(45)
                    anim_offset = [0]*5
                    pygame.time.delay(500)
                    ccc = []
                    let += cline
                    cline = ['null'] * 5
                    cursor_pos = 0
                    letreveal = False
                    gs = 1
                    sc_draw_game()
                    game_over.play()
                elif ''.join(map(str, cline)) in wordlist:
                    ccc = []
                    for k1 in range(5):
                        if cline[k1] == word[k1]:
                            ccc.append(G1)
                            green_let.play()
                        elif cline[k1] in word:
                            ccc.append(Y)
                            yellow_let.play()
                        else:
                            ccc.append(B2)
                            grey_let.play()
                        cc = pcc + ccc + [W] * (4-k1) + [G4] * (30 - len(pcc))
                        letreveal = True
                        for k in range(5):
                            anim_offset = [0]*k1 + [k*2+1] + [0]*(4-k1)
                            sc_draw_game()
                            t.tick(45)
                        for k in range(5):
                            anim_offset = [0] * k1 + [9 - k*2] + [0] * (4 - k1)
                            sc_draw_game()
                            t.tick(45)
                    anim_offset = [0] * 5
                    pcc += ccc
                    cc = pcc + [W]*5 + [G4]*(30-len(pcc)-5)
                    ccc = []
                    cursor_pos = 0
                    let += cline
                    cline = ['null'] * 5
                    letreveal = False
                    if len(let) == 30:
                        gs = 2
                        game_over.play()
                    sc_draw_game()
                else:
                    no_enter.play()
                    for k in range(5):
                        anim_offset = [k*2+1] + [-1-k*2] + [k*2+1] + [-1-k*2] + [k*2+1]
                        sc_draw_game()
                        t.tick(90)
                    for k in range(5):
                        anim_offset = [9 - k*2] + [k*2-9] + [9 - k*2] + [k*2-9] + [9 - k*2]
                        sc_draw_game()
                        t.tick(90)
                    anim_offset = [0]*5
                    sc_draw_game()
            if event.key == 1073741903:
                if cursor_pos < 4:
                    cursor_pos += 1
                insert_let.play()
                for k in range(5):
                    anim_offset = [0] * cursor_pos + [k * 2 + 1] + [0] * (4 - cursor_pos)
                    sc_draw_game()
                    t.tick(60)
                for k in range(5):
                    anim_offset = [0] * cursor_pos + [9 - k * 2] + [0] * (4 - cursor_pos)
                    sc_draw_game()
                    t.tick(60)
                anim_offset = [0] * 5
            if event.key == 1073741904:
                if cursor_pos > 0:
                    cursor_pos -= 1
                remove_let.play()
                for k in range(5):
                    anim_offset = [0] * cursor_pos + [k * 2 + 1] + [0] * (4 - cursor_pos)
                    sc_draw_game()
                    t.tick(60)
                for k in range(5):
                    anim_offset = [0] * cursor_pos + [9 - k * 2] + [0] * (4 - cursor_pos)
                    sc_draw_game()
                    t.tick(60)
                anim_offset = [0] * 5

        if event.type == pygame.MOUSEMOTION:
            [mx, my] = event.pos
            if 70 + int(750*s) <= my <= 70 + int(840*s):
                if sw//2 - int(235*s) <= mx <= sw//2 - 5*s:
                    if hover_btn != 1:
                        hover_btn = 1
                        sc_draw_game()
                elif sw//2 + int(235*s) >= mx >= sw//2 + 5*s:
                    if hover_btn != 2:
                        hover_btn = 2
                        sc_draw_game()
                elif hover_btn != 0:
                    hover_btn = 0
                    sc_draw_game()
            elif hover_btn != 0:
                hover_btn = 0
                sc_draw_game()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if hover_btn == 1:
                    if gs > 0:
                        wordlist = open('assets/words/5eng.txt').read()
                        word = list(random.choice(list(open('assets/words/5eng.txt'))))
                        word.pop()

                        cline = ['null'] * 5
                        let = []
                        cc = [W] * 5 + [G4] * 25
                        pcc = []
                        ccc = []
                        gs = 0
                        sc_draw_game()
                        round_start.play()
                    else:
                        gs = 3
                        sc_draw_game()
                        game_over.play()
                elif hover_btn == 2:
                    run = False
        if event.type == pygame.WINDOWFOCUSLOST:
            focuslost = True
            while focuslost:
                for ev1 in pygame.event.get():
                    if ev1.type == pygame.WINDOWFOCUSGAINED:
                        focuslost = False
                    t.tick(15)

    t.tick(30)

dc.close()
