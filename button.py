import pygame

# 按钮类


class Button():
    def __init__(self, screen, text, x, y, width, height, text_size=20, offset=0):
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.bg_color = (221, 218, 217)
        self.text_color = (0, 0, 0)
        self.text_size = text_size
        self.offset = offset

    def draw(self):
        pygame.draw.rect(self.screen, self.bg_color, self.rect, 0)
        pygame.draw.rect(
            self.screen, (153, 204, 255), self.rect, 1)
        self.screen.blit(pygame.font.SysFont("宋体", self.text_size).render(
            self.text, 1, self.text_color), (self.rect.centerx-0.25*len(self.text)*self.text_size+self.offset, self.rect.centery-0.5*self.text_size+3))

    def check_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.x < event.pos[0] and event.pos[0] < self.rect.right and self.rect.y < event.pos[1] and event.pos[1] < self.rect.bottom:
            return True
        else:
            return False
