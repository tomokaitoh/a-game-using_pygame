import pygame
from setting import Settings

# 砖块类


class gameObject():
    TYPE_BLOCK = 0
    TYPE_SCORE = 1

    def __init__(self, screen, x, y, width, height, type):
        self.setting = Settings()
        self.width = width
        self.height = height
        self.type = type
        self.screen = screen
        self.x=x
        self.y=y
        self.rect=pygame.Rect(x,y,width,height)
        self.color = self.setting.color[type]

    def draw(self):
        if self.type==self.TYPE_BLOCK:
            pygame.draw.rect(self.screen, self.color, self.rect, 0)
        elif self.type==self.TYPE_SCORE:
            pygame.draw.circle(self.screen,self.color,(self.x,self.y),5)