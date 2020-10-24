import pygame
from setting import Settings

# 砖块类


class gameObject():
    TYPE_BLOCK = 0

    def __init__(self, screen, x, y, width, height, type):
        self.setting = Settings()
        self.width = width
        self.height = height
        self.type = type
        self.screen = screen
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.color = self.setting.color[type]

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect, 0)
