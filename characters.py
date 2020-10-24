import pygame

# 玩家方块类


class Character():
    def __init__(self, setting, screen, x, y):
        self.screen = screen
        self.setting = setting
        self.rect = pygame.Rect(
            x, y, self.setting.character['size'], self.setting.character['size'])
        self.color = setting.character['color']
        self.speed = setting.character['speed']  # 水平移动速度
        self.jump_v = setting.character['jump_v']  # 起跳速度
        # 水平和竖直移动速度，正负代表方向
        self.direction = {
            'x': 0,
            'y': 0
        }
        # 重力大小
        self.gravity = setting.gravity
        # 方块是否在砖块上
        self.onBlock = False
        # 方块在哪个砖块上
        self.on_N_of_Block = 1

    def draw(self):
        pygame.draw.rect(
            self.screen, self.color, self.rect, 0)
        pygame.draw.rect(
            self.screen, (182, 220, 181), self.rect, 1)

    # 方块移动
    def move(self):
        self.rect.centerx += self.direction['x']*self.speed
        self.rect.centery += self.direction['y']*self.speed
        if(self.onBlock == False and self.direction['y'] < 10):
            self.direction['y'] += self.gravity
