import pygame as pg

pg.init()

CELL = 60
GRID = 9
BLOCK = 3
SIZE = CELL * GRID

BG = (245, 245, 245)
LINE = (20, 20, 20)
SELECTION = (189, 255, 252)
INVALID_BG = (255, 120, 120)

screen = pg.display.set_mode((SIZE, SIZE))
pg.display.set_caption("Sudoku")

font = pg.font.SysFont(None, 40)

board = [[0] * GRID for _ in range(GRID)]
invalid = [[False] * GRID for _ in range(GRID)]
selected = None  # (r, c)


def cell_rect(r, c):
    return pg.Rect(c * CELL, r * CELL, CELL, CELL)


def draw_grid():
    for i in range(GRID + 1):
        w = 4 if i % BLOCK == 0 else 1
        p = i * CELL
        pg.draw.line(screen, LINE, (p, 0), (p, SIZE), w)
        pg.draw.line(screen, LINE, (0, p), (SIZE, p), w)


def draw_numbers():
    for r in range(GRID):
        for c in range(GRID):
            v = board[r][c]
            if v == 0:
                continue
            surf = font.render(str(v), True, (10, 10, 10))
            rect = surf.get_rect(center=cell_rect(r, c).center)
            screen.blit(surf, rect)


def is_move_valid(board, r, c, value) -> bool:
    # TODO
    breakpoint()
    return True


clock = pg.time.Clock()
running = True

while running:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            running = False

        elif e.type == pg.MOUSEBUTTONDOWN and e.button == 1:
            mx, my = e.pos
            c = mx // CELL
            r = my // CELL
            if 0 <= r < GRID and 0 <= c < GRID:
                selected = (r, c)

        elif e.type == pg.KEYDOWN and selected is not None:
            r, c = selected

            # digits 1-9
            if pg.K_1 <= e.key <= pg.K_9:
                value = e.key - pg.K_0
                board[r][c] = value
                invalid[r][c] = not is_move_valid(board, r, c, value)

            # clear cell button
            elif e.key in (pg.K_0, pg.K_BACKSPACE, pg.K_DELETE):
                board[r][c] = 0
                invalid[r][c] = False

    screen.fill(BG)

    # invalid cells first
    for r in range(GRID):
        for c in range(GRID):
            if invalid[r][c]:
                pg.draw.rect(screen, INVALID_BG, cell_rect(r, c))

    # selected cell highlight on top of invalid highlight
    if selected is not None:
        pg.draw.rect(screen, SELECTION, cell_rect(*selected))

    draw_grid()
    draw_numbers()

    pg.display.flip()
    clock.tick(60)

pg.quit()
