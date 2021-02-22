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
        self.make_rect(screen, 'yellow', 0, 60, 4, 4)  # рудник
        self.make_rect(screen, 'green', 5, 61, 5, 3)  # пункт управления
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
        pygame.draw.rect(screen, pygame.Color('grey'), (16 * self.cell_size + self.left,
                                                         16 * self.cell_size + self.top, 32 * self.cell_size,
                                                         32 * self.cell_size))  # гора
        pygame.draw.rect(screen, pygame.Color('yellow'), (16 * self.cell_size + self.left,
                                                          44 * self.cell_size + self.top, self.cell_size * 4,
                                                          self.cell_size * 4))  # рудник
        pygame.draw.rect(screen, pygame.Color('yellow'), (44 * self.cell_size + self.left,
                                                          44 * self.cell_size + self.top, self.cell_size * 4,
                                                          self.cell_size * 4))  # рудник
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
        self.make_rect(screen, 'yellow', 56, 1, 4, 1)
        self.make_rect(screen, 'yellow', 61, 4, 1, 3)
        self.make_rect(screen, 'yellow', 62, 15, 2, 1)
        self.make_rect(screen, 'yellow', 59, 16, 5, 1)
        self.make_rect(screen, 'green', 56, 3, 4, 4)
        self.make_rect(screen, 'orange', 58, 9, 1, 2)
        self.make_rect(screen, 'orange', 59, 10, 1, 1)
        self.make_rect(screen, 'orange', 55, 9, 2, 4)
        self.make_rect(screen, 'orange', 58, 12, 2, 1)
        self.make_rect(screen, 'orange', 50, 11, 3, 1)
        self.make_rect(screen, 'orange', 50, 3, 1, 6)
        self.make_rect(screen, 'orange', 51, 7, 2, 2)
        self.make_rect(screen, 'orange', 50, 14, 2, 2)
        self.make_rect(screen, 'yellow', 0, 0, 10, 4)
        self.make_rect(screen, 'yellow', 0, 4, 9, 2)
        self.make_rect(screen, 'yellow', 0, 6, 7, 4)
        self.make_rect(screen, 'yellow', 0, 10, 5, 6)
        self.make_rect(screen, 'yellow', 0, 16, 3, 5)
        self.make_rect(screen, 'yellow', 18, 19, 2, 4)
        self.make_rect(screen, 'yellow', 20, 19, 1, 3)
        self.make_rect(screen, 'yellow', 21, 18, 2, 3)
        self.make_rect(screen, 'yellow', 23, 18, 1, 2)
        self.make_rect(screen, 'yellow', 24, 18, 2, 1)
        self.make_rect(screen, 'orange', 25, 23, 4, 3)
        self.make_rect(screen, 'orange', 30, 23, 1, 1)
        self.make_rect(screen, 'orange', 30, 24, 3, 2)
        self.make_rect(screen, 'orange', 34, 23, 1, 3)
        self.make_rect(screen, 'yellow', 37, 20, 4, 1)
        self.make_rect(screen, 'yellow', 39, 21, 4, 1)
        self.make_rect(screen, 'yellow', 42, 22, 2, 1)
        self.make_rect(screen, 'yellow', 44, 23, 1, 2)
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


class Tile(Board):
    def __init__(self, wi, he):
        super().__init__(wi, he)
        self.color = pygame.Color(255, 255, 255)

    def get_color(self):
        return self.color


class Ore(Tile):
    def __init__(self, wi, he):
        super().__init__(wi, he)
        self.color = pygame.Color(237, 160, 49)


class Mountain(Tile):
    def __init__(self, wi, he):
        super().__init__(wi, he)
        self.color = pygame.Color(120, 120, 120)


class Building(Tile):
    def __init__(self, wi, he):
        super().__init__(wi, he)
        self.color = pygame.Color(60, 60, 60)


class Park(Tile):
    def __init__(self, wi, he):
        super().__init__(wi, he)
        self.color = pygame.Color(152, 255, 152)


class Arch(Tile):
    def __init__(self, wi, he):
        super().__init__(wi, he)
        self.color = pygame.Color(80, 80, 80)


def main():
    pygame.init()
    size = he, wi = 870, 661
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Ирга')
    board = Board(64, 64)
    board.set_view(10, 10, 10)
    all_sprites = pygame.sprite.Group()
    Sprinter(all_sprites, x=30, y=30)
    Builder(all_sprites, x=50, y=50)
    SuperCannon(all_sprites, x=100, y=100)
    Tank(all_sprites, x=150, y=150)
    BigTank(all_sprites, x=200, y=200)
    Turel(all_sprites, x=250, y=250)
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