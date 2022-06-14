import pygame, sys

#1280 x 1024 screen BIG WINDOW
# MAIN_BOARD = [['.' for nod in range(139)] for row in range(105)]

# laptop screen SMALL WINDOW
MAIN_BOARD = [['.' for nod in range(85)] for row in range(64)]


class GameOfLife:
    def __init__(self, plansza):
        self.plansza = plansza

    def zmiana_pokolenia(self, plansza, liczba_symulacji=2):
        liczba_symulacji -= 1
        if liczba_symulacji == 0:
            return plansza

        # 1280 x 1024 screen BIG WINDOW
        # nowa_plansza = [['.' for nod in range(139)] for row in range(105)]

        # laptop screen SMALL WINDOW
        nowa_plansza = [['.' for nod in range(85)] for row in range(64)]

        for index_row, row in enumerate(plansza):
            for index_nod, nod in enumerate(row):
                zywa = True
                if nod == '.': zywa = False
                zywi_sasiedzi = self.zywi_sasiedzi(index_row, index_nod, plansza)
                if zywa and (zywi_sasiedzi == 2 or zywi_sasiedzi == 3):
                    nowa_plansza[index_row][index_nod] = 'X'
                elif not zywa and zywi_sasiedzi == 3:
                    nowa_plansza[index_row][index_nod] = 'X'
                else: nowa_plansza[index_row][index_nod] = '.'

        return self.zmiana_pokolenia(nowa_plansza, liczba_symulacji)

    def zywi_sasiedzi(self, index_row, index_nod, plansza=MAIN_BOARD):
        zywi = 0
        for i in range(-1, 2, 2):
            nowy_index_row = i + index_row
            nowy_index_nod = i + index_nod

            if nowy_index_nod == len(plansza[0]):
                nowy_index_nod = 0
            if nowy_index_row == len(plansza):
                nowy_index_row = 0

            if plansza[nowy_index_row][index_nod] == 'X':
                zywi += 1
            if plansza[index_row][nowy_index_nod] == 'X':
                zywi += 1

            for j in range(-1, 2, 2):
                nowy_index_nod = index_nod + j
                if nowy_index_nod == len(plansza[0]):
                    nowy_index_nod = 0

                if plansza[nowy_index_row][nowy_index_nod] == 'X':
                    zywi += 1
        return zywi

    def is_alive(self, board, index_row, index_nod):
        nod = board[index_row][index_nod]
        alive = True
        if nod == '.': alive = False
        zywi_sasiedzi = self.zywi_sasiedzi(index_row, index_nod, board)
        if alive and (zywi_sasiedzi == 2 or zywi_sasiedzi == 3):
            return alive
        elif not alive and zywi_sasiedzi == 3:
            return alive
        else:
            return not alive

    def mouse_handle(self):
        x, y = pygame.mouse.get_pos()

        mod_x, mod_y = x % 9, y % 9
        div_x, div_y = x // 9, y // 9

        if mod_x == 0:
            x = div_x
        else:
            x = (div_x * 9 + 9 - mod_x) // 9
        if mod_y == 0:
            y = div_y
        else:
            y = (div_y * 9 + 9 - mod_y) // 9

        return self.bug_handle(x, y)

    def clean(self, board):
        for i, row in enumerate(board):
            for j in range(len(row)):
                board[i][j] = '.'
        return board

    def board_drawing(self, board):
        for index_row, row in enumerate(MAIN_BOARD):
            for index_nod, nod_state in enumerate(row):
                if nod_state == 'X':
                    nod = pygame.Rect(index_nod * 9,index_row * 9, 10, 10)
                    pygame.draw.rect(screen, alive_color, nod)
                    continue
                nod = pygame.Rect(index_nod * 9, index_row * 9, NodSideLen, NodSideLen)
                pygame.draw.rect(screen, dead_color, nod, 1)

    def bug_handle(self, x, y):
        try:
            if MAIN_BOARD[y]: pass
        except:
            y = -1
        try:
            if MAIN_BOARD[y][x]: pass
        except:
            x = -1
        return x, y

main = GameOfLife(MAIN_BOARD)

pygame.init()
clock = pygame.time.Clock()

#BIG WINDOW
# screen_width = 1252
# screen_height = 946

#SMALL WINDOW
screen_width = 766
screen_height = 577

screen = pygame.display.set_mode((screen_width, screen_height))
generacja = 1
alive_color = pygame.Color(255, 255, 255)
dead_color = pygame.Color(18, 18, 18)
bg_color = pygame.Color(0,0,0)
NodSideLen = 10
run = False
pressed = False
if __name__ == "__main__":
    while True:
        # Handling input

        pygame.display.set_caption(f'Game of life   GENERACJA = {generacja}')
        screen.fill(bg_color)

        main.board_drawing(MAIN_BOARD)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if not run:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click = None
                    pressed = True

                    x, y = main.mouse_handle()

                    if event.button == 1:
                        click = 'LEFT'
                        if MAIN_BOARD[y][x] == '.':
                            MAIN_BOARD[y][x] = 'X'

                    if event.button == 3:
                        click = 'RIGHT'
                        if MAIN_BOARD[y][x] == 'X':
                            MAIN_BOARD[y][x] = '.'

                if event.type == pygame.MOUSEMOTION and pressed:
                    x, y = main.mouse_handle()
                    if click == 'LEFT':
                        if MAIN_BOARD[y][x] == '.':
                            MAIN_BOARD[y][x] = 'X'
                    if click == 'RIGHT':
                        if MAIN_BOARD[y][x] == 'X':
                            MAIN_BOARD[y][x] = '.'



                if event.type == pygame.MOUSEBUTTONUP:
                    pressed = False

            if event.type == pygame.KEYDOWN:
                if run:
                    if event.key == pygame.K_SPACE:
                        run = False
                else:
                    if event.key == pygame.K_SPACE:
                        run = True
                if event.key == pygame.K_ESCAPE:
                    generacja = 1
                    run = False
                    MAIN_BOARD = main.clean(MAIN_BOARD)

        if run:
            MAIN_BOARD = main.zmiana_pokolenia(MAIN_BOARD)
            generacja += 1

        pygame.display.flip()
        clock.tick(60)