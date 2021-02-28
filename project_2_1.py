import pygame
import os


def haracteristica_geroev(screen, price, hp, strength_of_close_attack, strength_of_far_attack, board, x, y, l, a, b):
    global flag_move
    global current_x
    global current_y
    global current_length
    global previous_cell
    global current_a
    global current_b
    current_b = b
    current_a = a
    previous_cell = (x - 10, y - 10)
    current_x = x
    current_y = y
    current_length = l
    flag_move = 1
    board.render(screen)
    pygame.draw.rect(screen, (0, 0, 0), (650, 0, 870 - 650, 650))
    fontObj = pygame.font.Font('freesansbold.ttf', 10)
    textSurfaceObj = fontObj.render(f"PRICE: {price}", True, (255, 0, 0), (0, 0, 0))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (750, 50)
    screen.blit(textSurfaceObj, textRectObj)

    fontObj = pygame.font.Font('freesansbold.ttf', 10)
    textSurfaceObj = fontObj.render(f"HP: {hp}", True, (255, 0, 0), (0, 0, 0))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (750, 100)
    screen.blit(textSurfaceObj, textRectObj)

    fontObj = pygame.font.Font('freesansbold.ttf', 10)
    textSurfaceObj = fontObj.render(f"STRENGTH OF CLOSE ATTACK: {strength_of_close_attack}", True, (255, 0, 0), (0, 0, 0))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (750, 150)
    screen.blit(textSurfaceObj, textRectObj)

    fontObj = pygame.font.Font('freesansbold.ttf', 10)
    textSurfaceObj = fontObj.render(f"STRENGTH OF FAR ATTACK: {strength_of_far_attack}", True, (255, 0, 0), (0, 0, 0))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (750, 200)
    screen.blit(textSurfaceObj, textRectObj)

    fontObj = pygame.font.Font('freesansbold.ttf', 15)
    textSurfaceObj = fontObj.render("MOVE", True, (255, 0, 0), (0, 0, 255))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (750, 250)
    screen.blit(textSurfaceObj, textRectObj)


def haracteristica_tekstur(screen, name, board):
    global flag_move
    flag_move = 0
    board.render(screen)
    pygame.draw.rect(screen, (0, 0, 0), (650, 0, 870 - 650, 650))
    fontObj = pygame.font.Font('freesansbold.ttf', 10)
    textSurfaceObj = fontObj.render(f"TYPE: {name}", True, (255, 0, 0), (0, 0, 0))
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (750, 50)
    screen.blit(textSurfaceObj, textRectObj)


def load_image(name, color_key=None):
    fullname = os.path.join('data_for_the_project', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


def load_image2(name, color_key=None):
    fullname = os.path.join('текстуры, проект', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


class Board:
    def __init__(self, wi, he):
        self.wi = wi
        self.he = he
        self.board = [[0] * wi for _ in range(he)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def make_rect(self, screen, color, x, y, len_x, len_y):
        pygame.draw.rect(screen, pygame.Color(color), (x * self.cell_size + self.left,
                                                                 y * self.cell_size + self.top, len_x * self.cell_size,
                                                                 len_y * self.cell_size))

    def render(self, screen):
        self.make_rect(screen, (92, 92, 92), 0, 0, 64, 64)
        for y in range(self.he):
            for x in range(self.wi):
                pygame.draw.rect(screen, pygame.Color('white'), (x * self.cell_size + self.left,
                                                                 y * self.cell_size + self.top, self.cell_size,
                                                                 self.cell_size), 1)

        # self.make_rect(screen, 'dark blue', 1, 58, 4, 1)  # барак
        #self.make_rect(screen, 'red', 1, 55, 4, 2)  # медпункт
        # self.make_rect(screen, 'dark blue', 1, 53, 4, 1)  # барак
        pygame.draw.rect(screen, pygame.Color('dark blue'), (6 * self.cell_size + self.left,
                                                        53 * self.cell_size + self.top, self.cell_size,
                                                        4 * self.cell_size))  # барак
        pygame.draw.rect(screen, pygame.Color('dark blue'), (8 * self.cell_size + self.left,
                                                        53 * self.cell_size + self.top, self.cell_size,
                                                        4 * self.cell_size))  # барак
        pygame.draw.rect(screen, pygame.Color('blue'), (11 * self.cell_size + self.left,
                                                        61 * self.cell_size + self.top, self.cell_size,
                                                        3 * self.cell_size))  # казармы
        #pygame.draw.rect(screen, pygame.Color('purple'), (10 * self.cell_size + self.left,
          #                                              52 * self.cell_size + self.top, self.cell_size * 2,
         #                                               2 * self.cell_size))  # вышка
        pygame.draw.rect(screen, pygame.Color('orange'), (4 * self.cell_size + self.left,
                                                        47 * self.cell_size + self.top, 2 * self.cell_size,
                                                        2 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (3 * self.cell_size + self.left,
                                                          44 * self.cell_size + self.top, 4 * self.cell_size,
                                                          self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (8 * self.cell_size + self.left,
                                                          44 * self.cell_size + self.top, 4 * self.cell_size,
                                                          self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (11 * self.cell_size + self.left,
                                                          41 * self.cell_size + self.top, 1 * self.cell_size,
                                                          3 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (0 * self.cell_size + self.left,
                                                          44 * self.cell_size + self.top, 2 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (0 * self.cell_size + self.left,
                                                          40 * self.cell_size + self.top, 1 * self.cell_size,
                                                          4 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (0 * self.cell_size + self.left,
                                                          37 * self.cell_size + self.top, 1 * self.cell_size,
                                                          2 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (0 * self.cell_size + self.left,
                                                          36 * self.cell_size + self.top, 10 * self.cell_size,
                                                          self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('brown'), (2 * self.cell_size + self.left,
                                                          36 * self.cell_size + self.top, 1 * self.cell_size,
                                                          self.cell_size))  # арка
        pygame.draw.rect(screen, pygame.Color('brown'), (7 * self.cell_size + self.left,
                                                         36 * self.cell_size + self.top, 1 * self.cell_size,
                                                         self.cell_size))  # арка
        pygame.draw.rect(screen, pygame.Color('orange'), (4 * self.cell_size + self.left,
                                                          40 * self.cell_size + self.top, 2 * self.cell_size,
                                                          3 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (4 * self.cell_size + self.left,
                                                          38 * self.cell_size + self.top, 2 * self.cell_size,
                                                          self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (9 * self.cell_size + self.left,
                                                          38 * self.cell_size + self.top, 1 * self.cell_size,
                                                          5 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (11 * self.cell_size + self.left,
                                                          35 * self.cell_size + self.top, 1 * self.cell_size,
                                                          5 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (0 * self.cell_size + self.left,
                                                          34 * self.cell_size + self.top, 12 * self.cell_size,
                                                          self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('brown'), (2 * self.cell_size + self.left,
                                                         34 * self.cell_size + self.top, 1 * self.cell_size,
                                                         self.cell_size))  # арка
        pygame.draw.rect(screen, pygame.Color('brown'), (7 * self.cell_size + self.left,
                                                         34 * self.cell_size + self.top, 1 * self.cell_size,
                                                         self.cell_size))  # арка
        pygame.draw.rect(screen, pygame.Color('orange'), (14 * self.cell_size + self.left,
                                                          60 * self.cell_size + self.top, 1 * self.cell_size,
                                                          4 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (15 * self.cell_size + self.left,
                                                          60 * self.cell_size + self.top, 3 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (19 * self.cell_size + self.left,
                                                          60 * self.cell_size + self.top, 4 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (24 * self.cell_size + self.left,
                                                          60 * self.cell_size + self.top, 3 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (26 * self.cell_size + self.left,
                                                          61 * self.cell_size + self.top, 1 * self.cell_size,
                                                          3 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (17 * self.cell_size + self.left,
                                                          62 * self.cell_size + self.top, 1 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (19 * self.cell_size + self.left,
                                                          62 * self.cell_size + self.top, 1 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (17 * self.cell_size + self.left,
                                                          63 * self.cell_size + self.top, 3 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (22 * self.cell_size + self.left,
                                                          62 * self.cell_size + self.top, 1 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (24 * self.cell_size + self.left,
                                                          62 * self.cell_size + self.top, 1 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (22 * self.cell_size + self.left,
                                                          63 * self.cell_size + self.top, 3 * self.cell_size,
                                                          1 * self.cell_size))  # здания

        pygame.draw.rect(screen, pygame.Color('orange'), (36 * self.cell_size + self.left,
                                                          60 * self.cell_size + self.top, 1 * self.cell_size,
                                                          4 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (37 * self.cell_size + self.left,
                                                          60 * self.cell_size + self.top, 3 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (41 * self.cell_size + self.left,
                                                          60 * self.cell_size + self.top, 4 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (47 * self.cell_size + self.left,
                                                          60 * self.cell_size + self.top, 3 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (49 * self.cell_size + self.left,
                                                          61 * self.cell_size + self.top, 1 * self.cell_size,
                                                          3 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (39 * self.cell_size + self.left,
                                                          62 * self.cell_size + self.top, 1 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (41 * self.cell_size + self.left,
                                                          62 * self.cell_size + self.top, 1 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (39 * self.cell_size + self.left,
                                                          63 * self.cell_size + self.top, 3 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (44 * self.cell_size + self.left,
                                                          62 * self.cell_size + self.top, 1 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (46 * self.cell_size + self.left,
                                                          62 * self.cell_size + self.top, 1 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (44 * self.cell_size + self.left,
                                                          63 * self.cell_size + self.top, 3 * self.cell_size,
                                                          1 * self.cell_size))  # здания

        pygame.draw.rect(screen, pygame.Color('orange'), (28 * self.cell_size + self.left,
                                                          61 * self.cell_size + self.top, 1 * self.cell_size,
                                                          3 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (28 * self.cell_size + self.left,
                                                          60 * self.cell_size + self.top, 3 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (32 * self.cell_size + self.left,
                                                          60 * self.cell_size + self.top, 3 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (34 * self.cell_size + self.left,
                                                          61 * self.cell_size + self.top, 1 * self.cell_size,
                                                          3 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (30 * self.cell_size + self.left,
                                                          62 * self.cell_size + self.top, 3 * self.cell_size,
                                                          2 * self.cell_size))  # здания

        pygame.draw.rect(screen, pygame.Color('orange'), (16 * self.cell_size + self.left,
                                                          53 * self.cell_size + self.top, 1 * self.cell_size,
                                                          4 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (17 * self.cell_size + self.left,
                                                          56 * self.cell_size + self.top, 10 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (26 * self.cell_size + self.left,
                                                          48 * self.cell_size + self.top, 1 * self.cell_size,
                                                          9 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (16 * self.cell_size + self.left,
                                                          48 * self.cell_size + self.top, 1 * self.cell_size,
                                                          4 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (16 * self.cell_size + self.left,
                                                          48 * self.cell_size + self.top, 3 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (20 * self.cell_size + self.left,
                                                          48 * self.cell_size + self.top, 7 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (18 * self.cell_size + self.left,
                                                          48 * self.cell_size + self.top, 1 * self.cell_size,
                                                          3 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (18 * self.cell_size + self.left,
                                                          52 * self.cell_size + self.top, 1 * self.cell_size,
                                                          3 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (19 * self.cell_size + self.left,
                                                          52 * self.cell_size + self.top, 2 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (19 * self.cell_size + self.left,
                                                          54 * self.cell_size + self.top, 2 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('brown'), (20 * self.cell_size + self.left,
                                                         53 * self.cell_size + self.top, 1 * self.cell_size,
                                                         self.cell_size))  # арка
        pygame.draw.rect(screen, pygame.Color('orange'), (22 * self.cell_size + self.left,
                                                          53 * self.cell_size + self.top, 2 * self.cell_size,
                                                          2 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (22 * self.cell_size + self.left,
                                                          49 * self.cell_size + self.top, 1 * self.cell_size,
                                                          3 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (24 * self.cell_size + self.left,
                                                          49 * self.cell_size + self.top, 1 * self.cell_size,
                                                          3 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('brown'), (23 * self.cell_size + self.left,
                                                         51 * self.cell_size + self.top, 1 * self.cell_size,
                                                         self.cell_size))  # арка
        pygame.draw.rect(screen, pygame.Color('brown'), (26 * self.cell_size + self.left,
                                                         52 * self.cell_size + self.top, 1 * self.cell_size,
                                                         self.cell_size))  # арка
        pygame.draw.rect(screen, pygame.Color('brown'), (21 * self.cell_size + self.left,
                                                         56 * self.cell_size + self.top, 1 * self.cell_size,
                                                         self.cell_size))  # арка

        pygame.draw.rect(screen, pygame.Color('orange'), (29 * self.cell_size + self.left,
                                                          48 * self.cell_size + self.top, 1 * self.cell_size,
                                                          9 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (32 * self.cell_size + self.left,
                                                          48 * self.cell_size + self.top, 1 * self.cell_size,
                                                          9 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (30 * self.cell_size + self.left,
                                                          48 * self.cell_size + self.top, 2 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (30 * self.cell_size + self.left,
                                                          56 * self.cell_size + self.top, 2 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('brown'), (30 * self.cell_size + self.left,
                                                         56 * self.cell_size + self.top, 1 * self.cell_size,
                                                         self.cell_size))  # арка

        pygame.draw.rect(screen, pygame.Color('orange'), (36 * self.cell_size + self.left,
                                                          48 * self.cell_size + self.top, 1 * self.cell_size,
                                                          9 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (37 * self.cell_size + self.left,
                                                          49 * self.cell_size + self.top, 1 * self.cell_size,
                                                          2 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (37 * self.cell_size + self.left,
                                                          54 * self.cell_size + self.top, 1 * self.cell_size,
                                                          2 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (38 * self.cell_size + self.left,
                                                          50 * self.cell_size + self.top, 1 * self.cell_size,
                                                          2 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (38 * self.cell_size + self.left,
                                                          53 * self.cell_size + self.top, 1 * self.cell_size,
                                                          2 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (39 * self.cell_size + self.left,
                                                          51 * self.cell_size + self.top, 1 * self.cell_size,
                                                          3 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('brown'), (39 * self.cell_size + self.left,
                                                         52 * self.cell_size + self.top, 1 * self.cell_size,
                                                         self.cell_size))  # арка
        pygame.draw.rect(screen, pygame.Color('orange'), (39 * self.cell_size + self.left,
                                                          48 * self.cell_size + self.top, 9 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (40 * self.cell_size + self.left,
                                                          49 * self.cell_size + self.top, 3 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (41 * self.cell_size + self.left,
                                                          50 * self.cell_size + self.top, 2 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (42 * self.cell_size + self.left,
                                                          51 * self.cell_size + self.top, 4 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (43 * self.cell_size + self.left,
                                                          52 * self.cell_size + self.top, 3 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (44 * self.cell_size + self.left,
                                                          53 * self.cell_size + self.top, 2 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (45 * self.cell_size + self.left,
                                                          54 * self.cell_size + self.top, 3 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (46 * self.cell_size + self.left,
                                                          55 * self.cell_size + self.top, 2 * self.cell_size,
                                                          2 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (47 * self.cell_size + self.left,
                                                          48 * self.cell_size + self.top, 1 * self.cell_size,
                                                          9 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('brown'), (47 * self.cell_size + self.left,
                                                         49 * self.cell_size + self.top, 1 * self.cell_size,
                                                         self.cell_size))  # арка
        pygame.draw.rect(screen, pygame.Color('orange'), (39 * self.cell_size + self.left,
                                                          56 * self.cell_size + self.top, 5 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (40 * self.cell_size + self.left,
                                                          55 * self.cell_size + self.top, 3 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (41 * self.cell_size + self.left,
                                                          54 * self.cell_size + self.top, 1 * self.cell_size,
                                                          1 * self.cell_size))  # здания

        pygame.draw.rect(screen, pygame.Color('orange'), (51 * self.cell_size + self.left,
                                                          60 * self.cell_size + self.top, 2 * self.cell_size,
                                                          4 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (53 * self.cell_size + self.left,
                                                          63 * self.cell_size + self.top, 1 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (53 * self.cell_size + self.left,
                                                          60 * self.cell_size + self.top, 2 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (56 * self.cell_size + self.left,
                                                          61 * self.cell_size + self.top, 5 * self.cell_size,
                                                          2 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (62 * self.cell_size + self.left,
                                                          61 * self.cell_size + self.top, 2 * self.cell_size,
                                                          3 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (51 * self.cell_size + self.left,
                                                          55 * self.cell_size + self.top, 2 * self.cell_size,
                                                          4 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (54 * self.cell_size + self.left,
                                                          55 * self.cell_size + self.top, 1 * self.cell_size,
                                                          4 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (56 * self.cell_size + self.left,
                                                          55 * self.cell_size + self.top, 1 * self.cell_size,
                                                          4 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (58 * self.cell_size + self.left,
                                                          55 * self.cell_size + self.top, 1 * self.cell_size,
                                                          4 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (60 * self.cell_size + self.left,
                                                          55 * self.cell_size + self.top, 1 * self.cell_size,
                                                          4 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (62 * self.cell_size + self.left,
                                                          55 * self.cell_size + self.top, 1 * self.cell_size,
                                                          4 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (51 * self.cell_size + self.left,
                                                          50 * self.cell_size + self.top, 2 * self.cell_size,
                                                          4 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (54 * self.cell_size + self.left,
                                                          50 * self.cell_size + self.top, 7 * self.cell_size,
                                                          4 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (62 * self.cell_size + self.left,
                                                          50 * self.cell_size + self.top, 2 * self.cell_size,
                                                          4 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (52 * self.cell_size + self.left,
                                                          46 * self.cell_size + self.top, 3 * self.cell_size,
                                                          3 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (56 * self.cell_size + self.left,
                                                          46 * self.cell_size + self.top, 3 * self.cell_size,
                                                          3 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (60 * self.cell_size + self.left,
                                                          46 * self.cell_size + self.top, 3 * self.cell_size,
                                                          3 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (51 * self.cell_size + self.left,
                                                          43 * self.cell_size + self.top, 4 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (56 * self.cell_size + self.left,
                                                          43 * self.cell_size + self.top, 4 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (51 * self.cell_size + self.left,
                                                          41 * self.cell_size + self.top, 1 * self.cell_size,
                                                          2 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (59 * self.cell_size + self.left,
                                                          41 * self.cell_size + self.top, 1 * self.cell_size,
                                                          2 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (53 * self.cell_size + self.left,
                                                          40 * self.cell_size + self.top, 2 * self.cell_size,
                                                          2 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (56 * self.cell_size + self.left,
                                                          40 * self.cell_size + self.top, 2 * self.cell_size,
                                                          2 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (51 * self.cell_size + self.left,
                                                          37 * self.cell_size + self.top, 1 * self.cell_size,
                                                          3 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (59 * self.cell_size + self.left,
                                                          37 * self.cell_size + self.top, 1 * self.cell_size,
                                                          3 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (51 * self.cell_size + self.left,
                                                          34 * self.cell_size + self.top, 1 * self.cell_size,
                                                          2 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (59 * self.cell_size + self.left,
                                                          34 * self.cell_size + self.top, 1 * self.cell_size,
                                                          2 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (52 * self.cell_size + self.left,
                                                          34 * self.cell_size + self.top, 3 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (56 * self.cell_size + self.left,
                                                          34 * self.cell_size + self.top, 3 * self.cell_size,
                                                          1 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (53 * self.cell_size + self.left,
                                                          36 * self.cell_size + self.top, 2 * self.cell_size,
                                                          3 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('orange'), (56 * self.cell_size + self.left,
                                                          36 * self.cell_size + self.top, 2 * self.cell_size,
                                                          3 * self.cell_size))  # здания
        pygame.draw.rect(screen, pygame.Color('brown'), (61 * self.cell_size + self.left,
                                                         53 * self.cell_size + self.top, 1 * self.cell_size,
                                                         self.cell_size)) # арка
        pygame.draw.rect(screen, pygame.Color('brown'), (53 * self.cell_size + self.left,
                                                         51 * self.cell_size + self.top, 1 * self.cell_size,
                                                         self.cell_size)) # арка
        pygame.draw.rect(screen, pygame.Color('brown'), (61 * self.cell_size + self.left,
                                                         62 * self.cell_size + self.top, 1 * self.cell_size,
                                                         self.cell_size)) # арка
        pygame.draw.rect(screen, pygame.Color('brown'), (51 * self.cell_size + self.left,
                                                         59 * self.cell_size + self.top, 1 * self.cell_size,
                                                         self.cell_size)) # арка
        pygame.draw.rect(screen, pygame.Color('brown'), (51 * self.cell_size + self.left,
                                                         54 * self.cell_size + self.top, 1 * self.cell_size,
                                                         self.cell_size)) # арка

        self.make_rect(screen, 'orange', 61, 0, 3, 4)
        self.make_rect(screen, 'dark blue', 63, 0, 1, 4)
        self.make_rect(screen, 'dark blue', 61, 0, 1, 4)
        self.make_rect(screen, 'blue', 62, 0, 1, 4)
        self.make_rect(screen, 'orange', 58, 9, 1, 2)
        self.make_rect(screen, 'orange', 59, 10, 1, 1)
        self.make_rect(screen, 'orange', 55, 9, 2, 4)
        self.make_rect(screen, 'orange', 58, 12, 2, 1)
        self.make_rect(screen, 'orange', 50, 11, 3, 1)
        self.make_rect(screen, 'orange', 50, 3, 1, 6)
        self.make_rect(screen, 'orange', 51, 7, 2, 2)
        self.make_rect(screen, 'orange', 50, 14, 2, 2)
        self.make_rect(screen, 'orange', 25, 23, 4, 3)
        self.make_rect(screen, 'orange', 30, 23, 1, 1)
        self.make_rect(screen, 'orange', 30, 24, 3, 2)
        self.make_rect(screen, 'orange', 34, 23, 1, 3)
        self.make_rect(screen, 'orange', 25, 12, 5, 2)
        self.make_rect(screen, 'orange', 30, 12, 1, 1)
        self.make_rect(screen, 'orange', 33, 12, 2, 2)
        self.make_rect(screen, 'orange', 35, 12, 3, 1)
        self.make_rect(screen, 'orange', 25, 4, 1, 4)
        self.make_rect(screen, 'orange', 27, 4, 3, 4)
        self.make_rect(screen, 'orange', 30, 7, 1, 1)
        self.make_rect(screen, 'orange', 33, 4, 2, 2)
        self.make_rect(screen, 'orange', 33, 7, 2, 1)
        self.make_rect(screen, 'orange', 36, 4, 1, 4)
        self.make_rect(screen, 'orange', 37, 7, 1, 1)

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def on_click(self, cell):
        pass

    def get_cell(self, mouse_pos):
        cell_x = (mouse_pos[0] - self.left) // self.cell_size
        cell_y = (mouse_pos[1] - self.top) // self.cell_size
        if cell_x < 0 or cell_x > self.wi or cell_y < 0 or cell_y > self.he:
            return None
        return cell_x, cell_y

    def get_click(self, mouse_pos, screen, all_sprites, event, board):
        global current_length
        global current_y
        global current_x
        global flag_move
        global previous_cell
        global current_a
        global current_b
        cell = self.get_cell(mouse_pos)
        if flag_move == 1 and mouse_pos[0] < 780 and mouse_pos[0] > 720 and mouse_pos[1] > 230 and mouse_pos[1] < 270:
            self.moving(screen, current_x, current_y, current_length, current_a, current_b)
            flag_move = 2
        elif (flag_move == 2 or flag_move == 3) and mouse_pos[0] > current_x - current_length * 10 and\
                mouse_pos[1] > current_y - current_length * 10 and\
                mouse_pos[0] < current_x + current_length * 10 + 10 and \
                mouse_pos[1] < current_y + current_length * 10 + 10:
            pygame.draw.rect(screen, (0, 255, 0), (cell[0] * 10 + 10, cell[1] * 10 + 10, 10, 10))
            pygame.draw.rect(screen, (255, 0, 0), (previous_cell[0] * 10 + 10, previous_cell[1] * 10 + 10, 10, 10))
            previous_cell = cell
            flag_move = 3
            fontObj = pygame.font.Font('freesansbold.ttf', 15)
            textSurfaceObj = fontObj.render(f"CHOOSE", True, (255, 0, 0), (0, 0, 0))
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (750, 300)
            screen.blit(textSurfaceObj, textRectObj)
        elif flag_move == 3 and mouse_pos[0] > 700 and mouse_pos[1] > 290 and mouse_pos[0] < 800 and mouse_pos[1] < 310:
            all_sprites.update(event, screen, board, 1, previous_cell)
            board.render(screen)
            pygame.draw.rect(screen, (0, 0, 0), (650, 0, 870 - 650, 650))
            flag_move = 0

    def moving(self, screen, x, y, length, a, b):
        pygame.draw.rect(screen, (255, 0, 0), (x - length * 10, y - length * 10, length * 20 + 10, 10 + length * 20))
        #for i in range(length):
         #   pygame.draw.rect(screen, (255, 0, 0), (x - length * 10 + i * 10, y - i * 10, 10, 10 + 20 * i))
        #pygame.draw.rect(screen, (255, 0, 0), (x, y - length * 10, 10, 10 + 20 * length))
        #for i in range(length):
         #   pygame.draw.rect(screen, (255, 0, 0), (x + length * 10 - i * 10, y - i * 10, 10, 10 + 20 * i))



class Peshka(pygame.sprite.Sprite):
    image = None

    def __init__(self, *group, x, y):
        super().__init__(*group)
        self.x = x
        self.y = y
        self.price = 4
        self.hp = 20
        self.close_attack = 1
        self.far_attack = 8
        self.strength_of_close_attack = 12
        self.strength_of_far_attack = 8
        self.number_of_solders = 1
        self.a = 1
        self.b = 1
        self.length_of_movement = 4
        self.image = load_image("Peshka.PNG")
        Peshka.image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def close_attack(self):
        pass

    def far_attack(self):
        pass

    def move(self):
        pass

    def transform(self):
        pass

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos) and args[3] == 0:
            haracteristica_geroev(args[1], self.price, self.hp, self.strength_of_close_attack, self.strength_of_far_attack,
                                  args[2], self.x, self.y, self.length_of_movement, self.a, self.b)
        elif args and args[3] == 1:
            global current_x
            global current_y
            if current_x == self.x and current_y == self.y:
                self.x = args[4][0] * 10 + 10
                self.y = args[4][1] * 10 + 10
                self.rect.x = args[4][0] * 10 + 10
                self.rect.y = args[4][1] * 10 + 10

class Sprinter(pygame.sprite.Sprite):
    image = None

    def __init__(self, *group, x, y):
        super().__init__(*group)
        self.x = x
        self.y = y
        self.price = 12
        self.hp = 24
        self.far_attack = None
        self.strength_of_far_attack = 12
        self.number_of_solders = 1
        self.a = 1
        self.b = 1
        self.length_of_movement = 8
        self.image = load_image("Sprinter.PNG")
        Sprinter.image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def spisok_deistvii(self):
        pass

    def far_attack(self):
        pass

    def move(self):
        pass

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            haracteristica_geroev(args[1], self.price, self.hp, "NO", self.strength_of_far_attack,
                                  args[2], self.x, self.y, self.length_of_movement, self.a, self.b)
        elif args and args[3] == 1:
            global current_x
            global current_y
            if current_x == self.x and current_y == self.y:
                self.x = args[4][0] * 10 + 10
                self.y = args[4][1] * 10 + 10
                self.rect.x = args[4][0] * 10 + 10
                self.rect.y = args[4][1] * 10 + 10


class Builder(pygame.sprite.Sprite):
    image = None

    def __init__(self, *group, x, y):
        super().__init__(*group)
        self.x = x
        self.y = y
        self.price = 16
        self.hp = 24
        self.close_attack = 2
        self.strength_of_close_attack = 8
        self.number_of_solders = 2
        self.a = 2
        self.b = 2
        self.length_of_movement = 4
        self.image = load_image("Builder.PNG")
        Builder.image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def spisok_deistvii(self):
        pass

    def close_attack(self):
        pass

    def move(self):
        pass

    def build(self):
        pass

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            haracteristica_geroev(args[1], self.price, self.hp, self.strength_of_close_attack, "NO",
                                  args[2], self.x, self.y, self.length_of_movement, self.a, self.b)
        elif args and args[3] == 1:
            global current_x
            global current_y
            if current_x == self.x and current_y == self.y:
                self.x = args[4][0] * 10 + 10
                self.y = args[4][1] * 10 + 10
                self.rect.x = args[4][0] * 10 + 10
                self.rect.y = args[4][1] * 10 + 10


class SuperCannon(pygame.sprite.Sprite):
    image = None

    def __init__(self, *group, x, y):
        super().__init__(*group)
        self.x = x
        self.y = y
        self.price = 60
        self.hp = 60
        self.far_attack = 20
        self.strength_of_far_attack = 32
        self.number_of_solders = 20
        self.a = 4
        self.b = 5
        self.length_of_movement = 2
        self.image = load_image("SuperCannon.PNG")
        SuperCannon.image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def spisok_deistvii(self):
        pass

    def far_attack(self):
        pass

    def move(self):
        pass

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            haracteristica_geroev(args[1], self.price, self.hp, "No", self.strength_of_far_attack,
                                  args[2], self.x, self.y, self.length_of_movement, self.a, self.b)
        elif args and args[3] == 1:
            global current_x
            global current_y
            if current_x == self.x and current_y == self.y:
                self.x = args[4][0] * 10 + 10
                self.y = args[4][1] * 10 + 10
                self.rect.x = args[4][0] * 10 + 10
                self.rect.y = args[4][1] * 10 + 10


class Tank(pygame.sprite.Sprite):
    image = None

    def __init__(self, *group, x, y):
        super().__init__(*group)
        self.x = x
        self.y = y
        self.price = 12
        self.hp = 32
        self.far_attack = 12
        self.strength_of_far_attack = 16
        self.number_of_solders = 3
        self.a = 2
        self.b = 2
        self.length_of_movement = 4
        self.image = load_image("Tank.PNG")
        Tank.image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def spisok_deistvii(self):
        pass

    def far_attack(self):
        pass

    def move(self):
        pass

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos) and args[3] == 0:
            haracteristica_geroev(args[1], self.price, self.hp, "NO",
                                  self.strength_of_far_attack,
                                  args[2], self.x, self.y, self.length_of_movement, self.a, self.b)
        elif args and args[3] == 1:
            global current_x
            global current_y
            if current_x == self.x and current_y == self.y:
                self.x = args[4][0] * 10 + 10
                self.y = args[4][1] * 10 + 10
                self.rect.x = args[4][0] * 10 + 10
                self.rect.y = args[4][1] * 10 + 10


class BigTank(pygame.sprite.Sprite):
    image = None

    def __init__(self, *group, x, y):
        super().__init__(*group)
        self.x = x
        self.y = y
        self.price = 20
        self.hp = 38
        self.far_attack = 16
        self.strength_of_far_attack = 20
        self.number_of_solders = 4
        self.a = 2
        self.b = 3
        self.length_of_movement = 3
        self.image = load_image("BigTank.PNG")
        BigTank.image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def spisok_deistvii(self):
        pass

    def far_attack(self):
        pass

    def move(self):
        pass

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            haracteristica_geroev(args[1], self.price, self.hp, "NO", self.strength_of_far_attack,
                                  args[2], self.x, self.y, self.length_of_movement, self.a, self.b)
        elif args and args[3] == 1:
            global current_x
            global current_y
            if current_x == self.x and current_y == self.y:
                self.x = args[4][0] * 10 + 10
                self.y = args[4][1] * 10 + 10
                self.rect.x = args[4][0] * 10 + 10
                self.rect.y = args[4][1] * 10 + 10


class Turel(pygame.sprite.Sprite):
    image = None

    def __init__(self, *group, x, y):
        super().__init__(*group)
        self.x = x
        self.y = y
        self.price = 6
        self.hp = 12
        self.far_attack = 6
        self.strength_of_far_attack = 8
        self.number_of_solders = 0
        self.a = 1
        self.b = 1
        self.length_of_movement = 0
        self.image = load_image("Turel.PNG")
        Turel.image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def spisok_deistvii(self):
        pass

    def close_attack(self):
        pass

    def move(self):
        pass

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            haracteristica_geroev(args[1], self.price, self.hp, "NO", self.strength_of_far_attack,
                                  args[2], self.x, self.y, self.length_of_movement, self.a, self.b)
        elif args and args[3] == 1:
            global current_x
            global current_y
            if current_x == self.x and current_y == self.y:
                self.x = args[4][0] * 10 + 10
                self.y = args[4][1] * 10 + 10
                self.rect.x = args[4][0] * 10 + 10
                self.rect.y = args[4][1] * 10 + 10


class Ore(pygame.sprite.Sprite):
    image = None

    def __init__(self, *group, x, y):
        super().__init__(*group)
        self.image = load_image2("Рудник.jpg")
        Ore.image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            haracteristica_tekstur(args[1], "Рудник", args[2])


class Mountain(pygame.sprite.Sprite):
    image = None

    def __init__(self, *group, x, y):
        super().__init__(*group)
        self.image = load_image2("IMG_7203 5.jpg")
        Mountain.image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            haracteristica_tekstur(args[1], "Гора", args[2])


class Building(pygame.sprite.Sprite):
    image = None

    def __init__(self, *group, x, y):
        super().__init__(*group)
        self.image = load_image2("1.jpg")
        Building.image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            haracteristica_tekstur(args[1], "Здание", args[2])


#class Park(Tile):
    #def __init__(self, wi, he):
     #   super().__init__(wi, he)
      #  self.color = pygame.Color(152, 255, 152)

class Barak(pygame.sprite.Sprite):
    image = None

    def __init__(self, *group, x, y):
        super().__init__(*group)
        self.image = load_image2("Барак.jpg")
        Barak.image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            haracteristica_tekstur(args[1], " Барак", args[2])

class Center(pygame.sprite.Sprite):
    image = None

    def __init__(self, *group, x, y):
        super().__init__(*group)
        self.image = load_image2("КомандныйЦентр.jpg")
        Center.image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            haracteristica_tekstur(args[1], " Командный Центр", args[2])

class Road(pygame.sprite.Sprite):
    image = None

    def __init__(self, *group, x, y):
        super().__init__(*group)
        self.image = load_image2("Асфальт.jpg")
        Road.image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Factory(pygame.sprite.Sprite):
    image = None

    def __init__(self, *group, x, y):
        super().__init__(*group)
        self.image = load_image2("Завод.jpg")
        Factory.image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            haracteristica_tekstur(args[1], "Завод", args[2])


def main():
    pygame.init()
    size = he, wi = 870, 661
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Ирга')
    board = Board(64, 64)
    board.set_view(10, 10, 10)
    all_sprites = pygame.sprite.Group()
    ind_rud = [(1, 1, 10), (1, 2, 10), (1, 3, 10), (1, 4, 10), (1, 5, 9), (1, 6, 9), (1, 7, 7), (1, 8, 7), (1, 9, 7),
               (1, 10, 7), (1, 11, 5), (1, 12, 5), (1, 13, 5), (1, 14, 5), (1, 15, 5), (1, 16, 5), (1, 17, 3),
               (1, 18, 3), (1, 19, 3), (1, 20, 3), (1, 21, 3), (1, 61, 4), (1, 62, 4), (1, 63, 4), (1, 64, 4),
               (17, 45, 4), (17, 46, 4), (17, 47, 4), (17, 48, 4), (45, 45, 4), (45, 46, 4), (45, 47, 4), (45, 48, 4),
               (19, 20, 6), (19, 21, 5), (19, 22, 3), (19, 23, 2), (22, 19, 5), (38, 21, 4), (40, 22, 4), (43, 23, 2),
               (45, 24, 1), (45, 25, 1), (57, 2, 4), (62, 5, 1), (62, 6, 1), (62, 7, 1), (60, 17, 5), (63, 16, 2)]
    for j in ind_rud:
        x1 = j[0]
        y1 = j[1]
        l = j[2]
        for i in range(l):
            Ore(all_sprites, x=(10 * x1 + i * 10), y=(10 * y1))

    ind_mount = [(21, 45, 24, 4), (17, 27, 32, 18), (17, 24, 9, 3), (30, 24, 1, 3), (34, 24, 1, 3), (32, 24, 2, 1),
                 (17, 17, 2, 7), (19, 17, 3, 3), (22, 17, 27, 2), (27, 19, 22, 2), (24, 21, 14, 3), (25, 20, 2, 1),
                 (22, 22, 2, 2), (21, 23, 1, 1), (38, 22, 2, 2), (36, 24, 9, 3), (40, 23, 3, 1), (46, 21, 3, 6),
                 (42, 21, 2, 1), (44, 21, 2, 2), (45, 23, 1, 1), (45, 26, 1, 1)]
    for j in ind_mount:
        x1 = j[0]
        y1 = j[1]
        l = j[2]
        l1 = j[3]
        for i in range(l):
            for q in range(l1):
                Mountain(all_sprites, x=(10 * x1 + i * 10), y=(10 * y1 + q * 10))
    #Barak(all_sprites, x=30, y=30)
    Center(all_sprites, x=60, y=610)
    Center(all_sprites, x=570, y=40)

    Peshka(all_sprites, x=110, y=110)
    Tank(all_sprites, x=110, y=320)
    Sprinter(all_sprites, x=110, y=130)
    SuperCannon(all_sprites, x=110, y=200)
    BigTank(all_sprites, x=110, y=250)
    Builder(all_sprites, x=110, y=370)
    Turel(all_sprites, x=110, y=450)
    #Factory(all_sprites, x=300, y=300)
    running = True
    board.render(screen)
    while running:
        all_sprites.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                all_sprites.update(event, screen, board, 0)
                board.get_click(event.pos, screen, all_sprites, event, board)
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()

flag_move = [0, 1]
current_length = 0
current_x = 0
current_y = 0
previous_cell = (0, 0)
current_a = 0
current_b = 0

if __name__ == '__main__':
    main()
