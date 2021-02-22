import pygame
import os


def haracteristica_geroev(screen, price, hp, strength_of_close_attack, strength_of_far_attack):
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

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)


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

    def spisok_deistvii(self):
        pass

    def close_attack(self):
        pass

    def far_attack(self):
        pass

    def move(self):
        pass

    def transform(self):
        pass

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            haracteristica_geroev(args[1], self.price, self.hp, self.strength_of_close_attack, self.strength_of_far_attack)


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
            haracteristica_geroev(args[1], self.price, self.hp, "NO", self.strength_of_far_attack)


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
            haracteristica_geroev(args[1], self.price, self.hp, self.strength_of_close_attack, "NO")


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
            haracteristica_geroev(args[1], self.price, self.hp, "No", self.strength_of_far_attack)


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
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            haracteristica_geroev(args[1], self.price, self.hp, "NO", self.strength_of_far_attack)


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
            haracteristica_geroev(args[1], self.price, self.hp, "NO", self.strength_of_far_attack)


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
            haracteristica_geroev(args[1], self.price, self.hp, "NO", self.strength_of_far_attack)


class Ore(pygame.sprite.Sprite):
    image = None

    def __init__(self, *group, x, y):
        super().__init__(*group)
        self.image = load_image2("Рудник.jpg")
        Ore.image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Mountain(pygame.sprite.Sprite):
    image = None

    def __init__(self, *group, x, y):
        super().__init__(*group)
        self.image = load_image2("IMG_7203 5.jpg")
        Mountain.image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Building(pygame.sprite.Sprite):
    image = None

    def __init__(self, *group, x, y):
        super().__init__(*group)
        self.image = load_image2("1.jpg")
        Building.image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


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

class Center(pygame.sprite.Sprite):
    image = None

    def __init__(self, *group, x, y):
        super().__init__(*group)
        self.image = load_image2("КомандныйЦентр.jpg")
        Center.image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

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

    ind_road = [(1, 22, 16, 13)]
    for j in ind_road:
        x1 = j[0]
        y1 = j[1]
        l = j[2]
        l1 = j[3]
        for i in range(l):
            for q in range(l1):
                Road(all_sprites, x=(10 * x1 + i * 10 + 1), y=(10 * y1 + q * 10 + 1))
    #Barak(all_sprites, x=30, y=30)
    Center(all_sprites, x=60, y=610)
    Center(all_sprites, x=570, y=40)
    #Road(all_sprites, x=200, y=200)
    #Factory(all_sprites, x=300, y=300)
    running = True
    while running:
        all_sprites.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                all_sprites.update(event, screen)
        board.render(screen)
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    main()