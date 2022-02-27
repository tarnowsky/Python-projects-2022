import pygame, sys
MAIN_BOARD = [['.' for nod in range(51)] for row in range(38)]
class GameOfLife:
    def __init__(self, plansza):
        self.plansza = plansza

    def zmiana_pokolenia(self, plansza, liczba_symulacji=2):
        liczba_symulacji -= 1
        if liczba_symulacji == 0:
            return plansza
        nowa_plansza = [['.' for nod in range(51)] for row in range(38)]

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
        a = False
        x, y = pygame.mouse.get_pos()
        for i in range(51):
            if 5+15*i <= x <= 15+15*i:
                a = True
        if a:
            for i in range(38):
                if 5 + 15 * i <= y <= 15 + 15 * i:
                    # pom_x, pom_y = x, y
                    mod = x % 15
                    if not mod == 0:
                        div = x // 15
                        x = (div * 15 + 15 - mod) // 15
                    else: x = x // 15 - 1
                    mod = y % 15
                    if not mod == 0:
                        div = y // 15
                        y = (div * 15 + 15 - mod) // 15
                    else: y = y // 15 - 1
                    return x, y
        return False

    def clean(self, board):
        for i, row in enumerate(board):
            for j in range(len(row)):
                board[i][j] = '.'
        return board



main = GameOfLife(MAIN_BOARD)

pygame.init()
clock = pygame.time.Clock()

screen_width = 768
screen_height = 576
screen = pygame.display.set_mode((screen_width, screen_height))
generacja = 1
alive_color = pygame.Color(219, 24, 31)
dead_color = pygame.Color(255, 255, 255)
bg_color = pygame.Color(0,0,0)
run = False
if __name__ == "__main__":
    while True:
        # Handling input

        pygame.display.set_caption(f'Game of life {generacja = }')
        screen.fill(bg_color)

        for index_row, row in enumerate(MAIN_BOARD):
            for index_nod, nod_state in enumerate(row):
                nod = pygame.Rect(5 + index_nod * 15, 5 + index_row * 15, 10, 10)
                if nod_state == 'X':
                    pygame.draw.rect(screen, alive_color, nod, 1)
                    continue
                pygame.draw.rect(screen, dead_color, nod, 1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if not run:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x_y = main.mouse_handle()
                        if x_y:
                            x, y = x_y[0], x_y[1]
                            if MAIN_BOARD[y][x] == 'X':
                                MAIN_BOARD[y][x] = '.'
                            else: MAIN_BOARD[y][x] = 'X'

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
        clock.tick(30)